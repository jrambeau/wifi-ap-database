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

def backup_existing_yaml(yaml_file):
    """Create a backup of the existing YAML file with timestamp"""
    if os.path.exists(yaml_file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{yaml_file}.backup_{timestamp}"
        shutil.copy2(yaml_file, backup_file)
        print(f"📁 Backup created: {backup_file}")
        return backup_file
    return None

def clean_data(value):
    """Clean and normalize data values"""
    if pd.isna(value):
        return ".nan"
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
        print(f"📊 Found {len(df)} access point records")
        print(f"📋 Columns: {len(df.columns)} fields")
        
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
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: Excel file '{excel_file}' not found")
        return False
    except Exception as e:
        print(f"❌ Error during conversion: {str(e)}")
        return False

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
            # Manufacturers
            manufacturer = ap.get('Constructeur', 'Unknown').strip()
            manufacturers[manufacturer] = manufacturers.get(manufacturer, 0) + 1
            
            # Generations
            generation = ap.get('Génération', 'Unknown')
            generations[generation] = generations.get(generation, 0) + 1
            
            # Indoor/Outdoor
            location = ap.get('Indoor/Outdoor', 'Unknown')
            indoor_outdoor[location] = indoor_outdoor.get(location, 0) + 1
        
        print(f"   Manufacturers: {', '.join([f'{k}({v})' for k,v in sorted(manufacturers.items(), key=lambda x: str(x[0]))])}")
        print(f"   Wi-Fi Generations: {', '.join([f'{k}({v})' for k,v in sorted(generations.items(), key=lambda x: str(x[0]))])}")
        print(f"   Indoor/Outdoor: {', '.join([f'{k}({v})' for k,v in sorted(indoor_outdoor.items(), key=lambda x: str(x[0]))])}")
        
    except Exception as e:
        print(f"❌ Error reading statistics: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert Excel AP specifications to YAML for Jekyll')
    parser.add_argument('--excel', default='Axians_Lyon_Comparatif_AP_v1.0.xlsx', 
                        help='Excel file to convert (default: Axians_Lyon_Comparatif_AP_v1.0.xlsx)')
    parser.add_argument('--output', default='_data/ap_models.yaml', 
                        help='Output YAML file (default: _data/ap_models.yaml)')
    parser.add_argument('--no-backup', action='store_true', 
                        help='Skip creating backup of existing YAML file')
    parser.add_argument('--validate', action='store_true', 
                        help='Only validate existing YAML file syntax')
    parser.add_argument('--stats', action='store_true', 
                        help='Show statistics about the AP database')
    
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
    
    # Main conversion
    success = convert_excel_to_yaml(
        excel_file=args.excel,
        yaml_file=args.output,
        create_backup=not args.no_backup
    )
    
    if success:
        # Validate the generated YAML
        if validate_yaml_syntax(args.output):
            show_statistics(args.output)
            print(f"\n🚀 Next steps:")
            print(f"   1. Review the generated {args.output}")
            print(f"   2. Commit changes to your Jekyll repository")
            print(f"   3. Deploy your updated site")
        else:
            print(f"⚠️  YAML file generated but contains syntax errors")
            sys.exit(1)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
