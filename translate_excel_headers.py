#!/usr/bin/env python3
"""
Translate Excel Column Headers from French to English
===================================================

This script reads the French Excel file and creates a new version with English column headers.
"""

import pandas as pd
import os
from datetime import datetime

# Translation mapping from French to English column names
COLUMN_TRANSLATIONS = {
    "Constructeur": "Manufacturer",
    "Modèle": "Model", 
    "Référence constructeur": "Manufacturer_Reference",
    "Type Ant": "Antenna_Type",
    "Indoor/Outdoor": "Indoor_Outdoor",
    "Génération": "Generation",
    "Protocole": "Protocol",
    "Positionnement gamme": "Product_Positioning",
    "Nbre de radios PHY simultanées": "Concurrent_PHY_Radios",
    "Radio 2,4 GHz": "Radio_2_4_GHz",
    "Radio 5 GHz": "Radio_5_GHz", 
    "Radio 6 GHz": "Radio_6_GHz",
    "Dedicated scanning radio": "Dedicated_Scanning_Radio",
    "Classe PoE": "PoE_Class",
    "Consomation max PoE (W)": "Max_PoE_Consumption_W",
    "Capacités limitées en PoE+ 30W": "Limited_Capabilities_PoE_Plus_30W",
    "Capacités limitées en PoE 15W": "Limited_Capabilities_PoE_15W",
    "Ethernet1": "Ethernet1",
    "Ethernet2": "Ethernet2",
    "Poids (kg)": "Weight_kg",
    "Dimensions (cm)": "Dimensions_cm",
    "Geoloc FTM (.11mc, .11az)": "Geolocation_FTM_80211mc_80211az",
    "Ports USB": "USB_Ports",
    "UWB": "UWB",
    "GPS": "GPS",
    "Bluetooth": "Bluetooth",
    "Zigbee": "Zigbee",
    "Compatible Cloud": "Cloud_Compatible",
    "Version Minimum": "Minimum_Version",
    "Prix public ($)": "Public_Price_USD",
    "Prix public (Euros)": "Public_Price_EUR",
    "Commentaire": "Comments"
}

def translate_excel_headers(input_file, output_file):
    """
    Read Excel file and create new version with English column headers
    """
    try:
        print(f"🔄 Reading Excel file: {input_file}")
        
        # Read Excel file
        df = pd.read_excel(input_file)
        print(f"📊 Found {len(df)} access point records")
        print(f"📋 Original columns: {len(df.columns)} fields")
        
        # Create translation mapping
        print(f"\n🌐 Translating column headers:")
        translated_columns = {}
        for col in df.columns:
            if col in COLUMN_TRANSLATIONS:
                new_name = COLUMN_TRANSLATIONS[col]
                translated_columns[col] = new_name
                print(f"  ✅ '{col}' → '{new_name}'")
            else:
                # Keep original if no translation found
                translated_columns[col] = col
                print(f"  ⚠️  '{col}' (no translation, keeping original)")
        
        # Apply translations
        df = df.rename(columns=translated_columns)
        
        # Save to new Excel file
        print(f"\n💾 Writing translated Excel file: {output_file}")
        df.to_excel(output_file, index=False)
        
        print(f"✅ Successfully created English Excel file with {len(df)} records")
        print(f"📋 New columns: {list(df.columns)}")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: Excel file '{input_file}' not found")
        return False
    except Exception as e:
        print(f"❌ Error during translation: {str(e)}")
        return False

def main():
    input_file = "Axians_Lyon_Comparatif_AP_v1.0.xlsx"
    output_file = "Axians_Lyon_Comparatif_AP_v1.0_English.xlsx"
    
    print("=" * 60)
    print("Excel Column Header Translation: French → English")
    print("=" * 60)
    
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        return
    
    # Create backup timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    success = translate_excel_headers(input_file, output_file)
    
    if success:
        print(f"\n🎉 Translation complete!")
        print(f"📁 Original file: {input_file} (preserved)")
        print(f"📁 English file: {output_file} (new)")
        print(f"\n💡 Next steps:")
        print(f"   1. Review the English Excel file")
        print(f"   2. Run: python convert_excel_to_yaml.py --excel {output_file}")
        print(f"   3. Deploy the updated site")

if __name__ == "__main__":
    main()