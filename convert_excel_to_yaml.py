#!/usr/bin/env python3
"""
Excel to YAML Converter for Jekyll AP Specifications
==================================================

This script converts Excel files containing Access Point specifications 
to YAML format for Jekyll static site generation.

Usage:
    python3 convert_excel_to_yaml.py
    python3 convert_excel_to_yaml.py --excel custom_file.xlsx
    python3 convert_excel_to_yaml.py --backup
"""

import pandas as pd
import yaml
import argparse
import os
from datetime import datetime
import shutil
import sys
from typing import List, Tuple, Dict, Any

# Normalization map for legacy -> new column names
COLUMN_RENAMES = {
    'Manufacturer': 'Vendor',
    'Manufacturer_Reference': 'Reference',
    'Constructeur': 'Vendor',            # legacy French
    'Référence_Constructeur': 'Reference',
}

def normalize_column_names(columns: List[str]) -> List[str]:
    """Return a list of columns with legacy names mapped to new schema.
    Does not enforce uniqueness beyond first occurrence.
    """
    normalized = []
    for col in columns:
        normalized.append(COLUMN_RENAMES.get(col, col))
    return normalized

def migrate_yaml_keys(yaml_file: str, dry_run: bool = False) -> Tuple[bool, int]:
    """Migrate existing YAML file keys to new schema.
    Manufacturer -> Vendor, Manufacturer_Reference -> Reference.
    Returns (success flag, number of records changed).
    """
    if not os.path.exists(yaml_file):
        print(f"❌ YAML file not found for migration: {yaml_file}")
        return False, 0
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or []
        if not isinstance(data, list):
            print("⚠️  YAML root is not a list; aborting migration")
            return False, 0
        changed = 0
        for rec in data:
            if not isinstance(rec, dict):
                continue
            # Manufacturer -> Vendor
            if 'Manufacturer' in rec and 'Vendor' not in rec:
                rec['Vendor'] = rec.pop('Manufacturer')
                changed += 1
            # Manufacturer_Reference -> Reference
            if 'Manufacturer_Reference' in rec and 'Reference' not in rec:
                rec['Reference'] = rec.pop('Manufacturer_Reference')
                changed += 1
        if dry_run:
            print(f"🔎 Dry run: would migrate {changed} key occurrences")
            return True, changed
        # Backup before write
        backup_existing_yaml(yaml_file)
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print(f"✅ Migration complete. Updated {changed} key occurrences in {yaml_file}")
        return True, changed
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False, 0

def backup_existing_yaml(yaml_file):
    """Create a backup of the existing YAML file with timestamp"""
    if os.path.exists(yaml_file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Store backup in a separate directory to avoid cluttering _data
        backup_dir = "backups"
        os.makedirs(backup_dir, exist_ok=True)
        yaml_filename = os.path.basename(yaml_file)
        backup_file = os.path.join(backup_dir, f"{yaml_filename}.backup_{timestamp}")
        shutil.copy2(yaml_file, backup_file)
        print(f"📁 Backup created: {backup_file}")
        return backup_file
    return None

def analyze_column_changes(new_columns, yaml_file):
    """Analyze changes in column structure compared to existing YAML"""
    changes = {
        'added': [],
        'removed': [],
        'renamed': [],
        'unchanged': []
    }
    
    # Get existing columns from YAML if it exists
    existing_columns = set()
    if os.path.exists(yaml_file):
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            if data and len(data) > 0:
                existing_columns = set(data[0].keys())
        except Exception as e:
            print(f"⚠️  Could not read existing YAML: {e}")
    
    new_columns_set = set(new_columns)
    
    # Detect changes
    changes['added'] = list(new_columns_set - existing_columns)
    changes['removed'] = list(existing_columns - new_columns_set)
    changes['unchanged'] = list(new_columns_set & existing_columns)
    
    # Simple rename detection (if one removed and one added, might be rename)
    if len(changes['removed']) == 1 and len(changes['added']) == 1:
        changes['renamed'] = [(changes['removed'][0], changes['added'][0])]
        changes['removed'] = []
        changes['added'] = []
    
    return changes

def update_jekyll_template(columns, template_file="index.md"):
    """Update Jekyll template with new column structure"""
    try:
        # Read current template
        with open(template_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generate new table headers
        headers = '\n'.join([f'            <th>{col.replace("_", " ")}</th>' for col in columns])
        
        # Generate new table data cells
        cells = '\n'.join([f'            <td>{{{{ ap.{col} | default: "" }}}}</td>' for col in columns])
        
        # Find and replace the table structure
        import re
        
        # Replace headers
        header_pattern = r'(<thead>\s*<tr>\s*)(.*?)(\s*</tr>\s*</thead>)'
        new_headers = f'\\1\n{headers}\n\\3'
        content = re.sub(header_pattern, new_headers, content, flags=re.DOTALL)
        
        # Replace data cells
        cell_pattern = r'({% for ap in site\.data\.ap_models %}\s*<tr>\s*)(.*?)(\s*</tr>\s*{% endfor %})'
        new_cells = f'\\1\n{cells}\n\\3'
        content = re.sub(cell_pattern, new_cells, content, flags=re.DOTALL)
        
        # Write updated template
        with open(template_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated Jekyll template: {template_file}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to update template: {e}")
        return False

def print_column_changes(changes):
    """Print a summary of column changes"""
    if any(changes[key] for key in ['added', 'removed', 'renamed']):
        print(f"\n🔄 Column Structure Changes Detected:")
        
        if changes['renamed']:
            for old, new in changes['renamed']:
                print(f"   📝 Renamed: '{old}' → '{new}'")
        
        if changes['added']:
            for col in changes['added']:
                print(f"   ➕ Added: '{col}'")
        
        if changes['removed']:
            for col in changes['removed']:
                print(f"   ➖ Removed: '{col}'")
        
        print(f"   ✅ Unchanged: {len(changes['unchanged'])} columns")
        
        if changes['added'] or changes['removed'] or changes['renamed']:
            print(f"\n⚠️  Template Update Required:")
            print(f"     The Jekyll template (index.md) may need updates")
            print(f"     to reflect these column changes.")
    else:
        print(f"✅ No column structure changes detected")

def clean_data(value):
    """Clean and normalize data values"""
    if pd.isna(value):
        return ""  # Return empty string instead of ".nan"
    if isinstance(value, str):
        return value.strip()
    return value

def convert_excel_to_yaml(excel_file, yaml_file, create_backup=True):
    """
    Convert Excel file to YAML format suitable for Jekyll
    
    Args:
        excel_file (str): Path to Excel file
        yaml_file (str): Path to output YAML file
        create_backup (bool): Whether to create backup of existing YAML
    """
    try:
        print(f"🔄 Reading Excel file: {excel_file}")
        
        # Read Excel file
        df = pd.read_excel(excel_file)
        # Normalize column names to new schema where needed
        original_columns = list(df.columns)
        new_columns = normalize_column_names(original_columns)
        if new_columns != original_columns:
            rename_map = {orig: new for orig, new in zip(original_columns, new_columns) if orig != new}
            if rename_map:
                df.rename(columns=rename_map, inplace=True)
                print(f"📝 Normalized columns: {', '.join([f'{k}->{v}' for k,v in rename_map.items()])}")
        print(f"📊 Found {len(df)} access point records")
        print(f"📋 Columns: {len(df.columns)} fields")
        
        # Analyze column changes
        changes = analyze_column_changes(list(df.columns), yaml_file)
        print_column_changes(changes)
        
        # Create backup if requested
        if create_backup:
            backup_existing_yaml(yaml_file)
        
        # Convert DataFrame to list of dictionaries
        data = []
        for _, row in df.iterrows():
            ap_record = {}
            for column in df.columns:
                ap_record[column] = clean_data(row[column])
            data.append(ap_record)
        
        # Write to YAML file
        print(f"💾 Writing YAML file: {yaml_file}")
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print(f"✅ Successfully converted {len(data)} records to {yaml_file}")
        print(f"🌐 Jekyll site can now be updated with new AP data")
        
        return True, list(df.columns), changes
        
    except FileNotFoundError:
        print(f"❌ Error: Excel file '{excel_file}' not found")
        return False, [], {}
    except Exception as e:
        print(f"❌ Error during conversion: {str(e)}")
        return False, [], {}

def validate_yaml_syntax(yaml_file):
    """Validate YAML syntax"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        print(f"✅ YAML syntax validation passed: {yaml_file}")
        return True
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ YAML file not found: {yaml_file}")
        return False

def show_statistics(yaml_file):
    """Show statistics about the AP data"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if not data:
            print("📊 No data found in YAML file")
            return
        
        print(f"\n📊 AP Database Statistics:")
        print(f"   Total APs: {len(data)}")
        
        # Count by manufacturer
        manufacturers = {}
        generations = {}
        indoor_outdoor = {}
        
        for ap in data:
            # Vendor backward compatibility (Manufacturer / Constructeur)
            vendor = ap.get('Vendor', ap.get('Manufacturer', ap.get('Constructeur', 'Unknown')))
            if isinstance(vendor, str):
                vendor = vendor.strip()
            manufacturers[vendor] = manufacturers.get(vendor, 0) + 1
            
            # Generations
            generation = ap.get('Generation', ap.get('Génération', 'Unknown'))
            generations[generation] = generations.get(generation, 0) + 1
            
            # Indoor/Outdoor
            location = ap.get('Indoor_Outdoor', ap.get('Indoor/Outdoor', 'Unknown'))
            indoor_outdoor[location] = indoor_outdoor.get(location, 0) + 1
        
        print(f"   Manufacturers: {', '.join([f'{k}({v})' for k,v in sorted(manufacturers.items(), key=lambda x: str(x[0]))])}")
        print(f"   Wi-Fi Generations: {', '.join([f'{k}({v})' for k,v in sorted(generations.items(), key=lambda x: str(x[0]))])}")
        print(f"   Indoor/Outdoor: {', '.join([f'{k}({v})' for k,v in sorted(indoor_outdoor.items(), key=lambda x: str(x[0]))])}")
        
    except Exception as e:
        print(f"❌ Error reading statistics: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert Excel AP specifications to YAML for Jekyll')
    parser.add_argument('--excel', default='wifi-ap-database.xlsx', 
                        help='Excel file to convert (default: wifi-ap-database.xlsx)')
    parser.add_argument('--output', default='_data/ap_models.yaml', 
                        help='Output YAML file (default: _data/ap_models.yaml)')
    parser.add_argument('--no-backup', action='store_true', 
                        help='Skip creating backup of existing YAML file')
    parser.add_argument('--update-template', action='store_true', 
                        help='Automatically update Jekyll template when columns change')
    parser.add_argument('--validate', action='store_true', 
                        help='Only validate existing YAML file syntax')
    parser.add_argument('--stats', action='store_true', 
                        help='Show statistics about the AP database')
    parser.add_argument('--migrate-yaml', action='store_true',
                        help='Migrate existing YAML keys (Manufacturer->Vendor, Manufacturer_Reference->Reference)')
    parser.add_argument('--migrate-dry-run', action='store_true',
                        help='Show what would change in migration without writing')
    
    args = parser.parse_args()
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("🔧 Excel to YAML Converter for Jekyll AP Database")
    print("=" * 50)
    
    # Validate only mode
    if args.validate:
        if validate_yaml_syntax(args.output):
            show_statistics(args.output)
        sys.exit(0)
    
    # Stats only mode
    if args.stats:
        show_statistics(args.output)
        sys.exit(0)

    # Migration only mode
    if args.migrate_yaml:
        migrate_yaml_keys(args.output, dry_run=args.migrate_dry_run)
        sys.exit(0)
    
    # Main conversion
    result = convert_excel_to_yaml(
        excel_file=args.excel,
        yaml_file=args.output,
        create_backup=not args.no_backup
    )
    
    if result and len(result) == 3:
        success, columns, changes = result
        
        # Update template if requested and changes detected
        if args.update_template and (changes['added'] or changes['removed'] or changes['renamed']):
            print(f"\n🔄 Updating Jekyll template...")
            update_jekyll_template(columns)
        
        # Validate the generated YAML
        if validate_yaml_syntax(args.output):
            show_statistics(args.output)
            print(f"\n🚀 Next steps:")
            print(f"   1. Review the generated {args.output}")
            if args.update_template and (changes['added'] or changes['removed'] or changes['renamed']):
                print(f"   2. Review the updated index.md template")
                print(f"   3. Commit changes to your Jekyll repository")
                print(f"   4. Deploy your updated site")
            else:
                print(f"   2. Commit changes to your Jekyll repository")
                print(f"   3. Deploy your updated site")
        else:
            print(f"⚠️  YAML file generated but contains syntax errors")
            sys.exit(1)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
