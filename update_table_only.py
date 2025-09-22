#!/usr/bin/env python3
import pandas as pd
import re

def update_table_structure(index_file, excel_file):
    """
    Update only the table columns in index.md while preserving all other functionality
    """
    # Read the Excel file to get column names
    df = pd.read_excel(excel_file)
    columns = list(df.columns)
    
    # Read the current index.md
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate new table headers HTML
    headers = '\n'.join([f'            <th>{col.replace("_", " ")}</th>' for col in columns])
    
    # Generate new table cells HTML
    cells = '\n'.join([f'            <td>{{{{ ap.{col} | default: "" }}}}</td>' for col in columns])
    
    # Update probe row with representative data
    probe_cells = []
    sample_data = {
        'Vendor': 'VeryLongVendorNameSample',
        'Model': 'Model-Extreme-9999X-Pro-Max',
        'Reference': 'MANUF-REF-SUPER-LONG-IDENTIFIER-12345',
        'Antenna_Type': 'External High-Gain Omni Directional Antenna Pack',
        'Indoor_Outdoor': 'Indoor/Outdoor Industrial Hardened',
        'Generation': 'Wi-Fi 7 / 802.11be Gen',
        'Protocol': '802.11a/b/g/n/ac/ax/be Tri-Band',
        'Product_Positioning': 'High Density Enterprise Hospitality Stadium',
        'Concurrent_PHY_Radios': '4x Concurrent Multi-Radio Chains',
        'Radio_2_4_GHz': '4x4:4 2.4GHz MIMO',
        'Radio_5_GHz': '8x8:8 5GHz MU-MIMO',
        'Radio_6_GHz': '8x8:8 6GHz MU-MIMO',
        'Dedicated_Scanning_Radio': 'Dedicated Security / WIPS / Sensor Radio Included',
        'PoE_Class': 'PoE++ Class 8',
        'Max_PoE_Consumption_W': '45.5 W',
        'Limited_Capabilities_PoE_bt_Class5_45W': 'Reduced Performance Mode @45W',
        'Limited_Capabilities_PoE_at_30W': 'Basic Operation Mode @30W',
        'Limited_Capabilities_PoE_af_15W': 'Limited Features @15W',
        'Ethernet1': '1 x 10G SFP+/RJ45 Combo',
        'Ethernet2': '1 x 2.5G Ethernet Port',
        'Weight_kg': '1.250 kg',
        'Dimensions_cm': '28 x 28 x 6.5 cm',
        'Geolocation_FTM_80211mc_80211az': 'FTM + 802.11mc + 802.11az Enabled',
        'USB_Ports': 'USB-C + USB-A',
        'UWB': 'Yes (UWB)',
        'GNSS': 'Multi-Constellation GNSS',
        'Bluetooth': 'BLE 5.4 Long Range',
        'Zigbee': 'Zigbee 3.0 Thread',
        'Cloud_Compatible': 'Cloud + On-Prem Controller Compatible',
        'Minimum_Version': 'Minimum Release 23.9.5',
        'Public_Price_USD': '9999 USD',
        'Public_Price_EUR': '8999 EUR',
        'Comments': 'Sample longest realistic comments text to anchor width sizing baseline.'
    }
    
    for col in columns:
        value = sample_data.get(col, f"Sample {col.replace('_', ' ')}")
        if col in ['Vendor', 'Model']:
            probe_cells.append(f'            <td class="sticky-col sticky-col-{1 if col == "Vendor" else 2}">{value}</td>')
        else:
            probe_cells.append(f'            <td>{value}</td>')
    
    probe_row = '\n'.join(probe_cells)
    
    # Find and replace the header section
    header_pattern = r'(<thead>\s*<tr>\s*)(.*?)(\s*</tr>\s*</thead>)'
    new_headers = f'\\1\n{headers}\n\\3'
    content = re.sub(header_pattern, new_headers, content, flags=re.DOTALL)
    
    # Find and replace the cells section
    cell_pattern = r'({% for ap in site\.data\.ap_models %}\s*<tr>\s*)(.*?)(\s*</tr>\s*{% endfor %})'
    new_cells = f'\\1\n{cells}\n\\3'
    content = re.sub(cell_pattern, new_cells, content, flags=re.DOTALL)
    
    # Find and replace the probe row
    probe_pattern = r'(<tr class="width-probe">\s*)(.*?)(\s*</tr>)'
    new_probe = f'\\1\n{probe_row}\n\\3'
    content = re.sub(probe_pattern, new_probe, content, flags=re.DOTALL)
    
    # Write the updated content back
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated table structure in {index_file}")
    print(f"📊 Added {len(columns)} columns")
    print(f"🔄 Remember to test all functionality before committing")

if __name__ == "__main__":
    update_table_structure("index.md", "wifi-ap-database-copy.xlsx")