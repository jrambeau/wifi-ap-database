#!/usr/bin/env pwsh
# Update AP Database Script
# This script automates the process of updating the AP database from Excel

# Function to show colored output
function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

# Create timestamp for backups
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

Write-ColorOutput Green "🚀 Starting AP Database Update Process..."
Write-ColorOutput Green "============================================="

# 1. Create backups
Write-ColorOutput Cyan "📑 Creating backups..."
if (Test-Path "wifi-ap-database.xlsx") {
    Copy-Item "wifi-ap-database.xlsx" "backups/wifi-ap-database.backup_$timestamp.xlsx"
}
if (Test-Path "index.md") {
    Copy-Item "index.md" "backups/index.md.backup_$timestamp"
}
if (Test-Path "_data/ap_models.yaml") {
    Copy-Item "_data/ap_models.yaml" "backups/ap_models.yaml.backup_$timestamp"
}

# 2. Update YAML data
Write-ColorOutput Cyan "📊 Updating YAML data..."
python convert_excel_to_yaml.py --excel wifi-ap-database.xlsx --no-backup
if ($LASTEXITCODE -ne 0) {
    Write-ColorOutput Red "❌ Error updating YAML data. Please check the Excel file and try again."
    exit 1
}

# 3. Update table structure
Write-ColorOutput Cyan "🔄 Updating table structure..."
python update_table_only.py
if ($LASTEXITCODE -ne 0) {
    Write-ColorOutput Red "❌ Error updating table structure. Please check the files and try again."
    exit 1
}

# 4. Git operations
Write-ColorOutput Cyan "📝 Checking Git status..."
$status = git status --porcelain
if ($status) {
    Write-ColorOutput Yellow "Changes detected. Proceeding with commit..."
    
    # Stage the changes
    git add _data/ap_models.yaml index.md
    
    # Commit with current date
    $date = Get-Date -Format "yyyy-MM-dd HH:mm"
    git commit -m "Update AP database - $date"
    
    # Push to GitHub
    Write-ColorOutput Cyan "📤 Pushing changes to GitHub..."
    git push origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-ColorOutput Green "✅ Successfully updated and deployed AP database!"
        Write-ColorOutput Yellow "🌐 The website will be updated in a few minutes."
    } else {
        Write-ColorOutput Red "❌ Error pushing changes to GitHub. Please check your connection and try again."
    }
} else {
    Write-ColorOutput Yellow "ℹ️ No changes detected in the database."
}