#!/bin/bash
# =============================================================================
# Quick Update Script for Jekyll AP Database
# =============================================================================
# This script provides easy ways to update the Jekyll site with new AP data
# 
# Usage:
#   ./update_site.sh           # Convert Excel to YAML and show stats
#   ./update_site.sh backup    # Create backup and convert
#   ./update_site.sh validate  # Just validate current YAML
#   ./update_site.sh stats     # Show database statistics
# =============================================================================

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo -e "${BLUE}🚀 Jekyll AP Database Update Tool${NC}"
echo "=============================================="

# Function to check if required files exist
check_requirements() {
    if [ ! -f "convert_excel_to_yaml.py" ]; then
        echo -e "${RED}❌ Error: convert_excel_to_yaml.py not found${NC}"
        exit 1
    fi
    
    if [ ! -f "Axians_Lyon_Comparatif_AP_v1.0.xlsx" ]; then
        echo -e "${RED}❌ Error: Excel file 'Axians_Lyon_Comparatif_AP_v1.0.xlsx' not found${NC}"
        echo -e "${YELLOW}💡 Make sure to update the Excel file with new AP data first${NC}"
        exit 1
    fi
}

# Function to convert and update
update_database() {
    local create_backup=$1
    
    echo -e "${YELLOW}🔄 Converting Excel to YAML...${NC}"
    
    if [ "$create_backup" = "true" ]; then
        python3 convert_excel_to_yaml.py
    else
        python3 convert_excel_to_yaml.py --no-backup
    fi
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Database updated successfully!${NC}"
        echo -e "${BLUE}📝 Next steps:${NC}"
        echo "   1. Review the changes in ap_models.yaml"
        echo "   2. Test the Jekyll site locally: bundle exec jekyll serve"
        echo "   3. Commit and push to deploy: git add . && git commit -m 'Update AP database' && git push"
    else
        echo -e "${RED}❌ Update failed!${NC}"
        exit 1
    fi
}

# Function to validate YAML
validate_yaml() {
    echo -e "${YELLOW}🔍 Validating YAML syntax...${NC}"
    python3 convert_excel_to_yaml.py --validate
}

# Function to show statistics
show_stats() {
    echo -e "${YELLOW}📊 Showing database statistics...${NC}"
    python3 convert_excel_to_yaml.py --stats
}

# Function to show help
show_help() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  (none)     Convert Excel to YAML with backup (default)"
    echo "  backup     Same as default - convert with backup"
    echo "  no-backup  Convert without creating backup"
    echo "  validate   Validate current YAML syntax only"
    echo "  stats      Show database statistics only"
    echo "  help       Show this help message"
    echo ""
    echo "Quick workflow for adding new APs:"
    echo "  1. Edit 'Axians_Lyon_Comparatif_AP_v1.0.xlsx' (add new rows)"
    echo "  2. Run: ./update_site.sh"
    echo "  3. Test Jekyll site locally"
    echo "  4. Commit and deploy"
}

# Main logic
case "${1:-default}" in
    "backup"|"default")
        check_requirements
        update_database true
        ;;
    "no-backup")
        check_requirements
        update_database false
        ;;
    "validate")
        validate_yaml
        ;;
    "stats")
        show_stats
        ;;
    "help"|"-h"|"--help")
        show_help
        ;;
    *)
        echo -e "${RED}❌ Unknown command: $1${NC}"
        echo ""
        show_help
        exit 1
        ;;
esac