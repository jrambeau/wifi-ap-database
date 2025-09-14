#!/bin/bash

# WiFi AP Database Update Script
# =============================
# This script updates the Jekyll site with new AP data from Excel

echo "🔄 WiFi AP Database Update"
echo "=========================="

# Check if English Excel file exists
if [ ! -f "wifi-ap-database.xlsx" ]; then
    echo "❌ English Excel file not found!"
    echo "💡 Please ensure 'wifi-ap-database.xlsx' exists"
    echo "💡 Or run: python translate_excel_headers.py to create it"
    exit 1
fi

# Run the conversion
echo "📊 Converting Excel to YAML..."
python convert_excel_to_yaml.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Conversion successful!"
    echo ""
    echo "🚀 Next steps:"
    echo "   1. Review the changes: git diff _data/ap_models.yaml"
    echo "   2. Commit changes: git add . && git commit -m 'Update AP database'"
    echo "   3. Deploy: git push origin main"
    echo ""
    echo "🌐 Your site will be live at: https://jrambeau.github.io/wifi-ap-database/"
else
    echo "❌ Conversion failed!"
    exit 1
fi