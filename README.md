# Jekyll AP Database - Easy Update Guide

This repository contains a Jekyll-powered website for browsing and comparing Wi-Fi Access Point specifications.

## 📁 Files Overview

- `Axians_Lyon_Comparatif_AP_v1.0.xlsx` - **Main data source** (edit this to add new APs)
- `ap_models.yaml` - Generated YAML data file (used by Jekyll)
- `ap_table.md` - Jekyll page template for the AP table
- `convert_excel_to_yaml.py` - Python conversion script
- `update_site.sh` - **Easy update script** (recommended)

## 🚀 How to Add New Access Points (Easy Method)

### Option 1: Using the Update Script (Recommended)

1. **Edit the Excel file**:
   - Open `Axians_Lyon_Comparatif_AP_v1.0.xlsx`
   - Add new rows with AP specifications
   - Save the file

2. **Run the update script**:
   ```bash
   ./update_site.sh
   ```

3. **Test locally** (if you have Jekyll installed):
   ```bash
   bundle exec jekyll serve
   ```

4. **Deploy**:

   **🎯 Choose Your Deployment Method:**

   ### Option A: GitHub Pages (Recommended - Free)
   ```bash
   # First time setup (run once)
   ./setup_jekyll_site.sh
   
   # Create GitHub repository and connect
   git remote add origin https://github.com/USERNAME/REPOSITORY.git
   git push -u origin main
   
   # Enable GitHub Pages in repository settings
   # Future updates:
   ./deploy.sh
   ```

   ### Option B: Manual Git Deployment
   ```bash
   git add .
   git commit -m "Add new AP models: [ModelName1, ModelName2]"
   git push
   ```

   ### Option C: Other Hosting (Netlify, Vercel, etc.)
   ```bash
   # Build the site locally
   bundle exec jekyll build
   # Upload _site/ folder to your hosting provider
   ```

### Option 2: Manual Python Script

```bash
# Convert Excel to YAML with backup
python3 convert_excel_to_yaml.py

# Or without backup
python3 convert_excel_to_yaml.py --no-backup

# Validate YAML syntax
python3 convert_excel_to_yaml.py --validate

# Show database statistics
python3 convert_excel_to_yaml.py --stats
```

## 📊 Quick Commands

```bash
# Show current database stats
./update_site.sh stats

# Validate current YAML
./update_site.sh validate

# Full update with backup
./update_site.sh backup

# Update without backup
./update_site.sh no-backup
```

## 📝 Excel File Format

The Excel file should contain these columns:

| Column | Description | Example |
|--------|-------------|---------|
| Constructeur | Manufacturer | Cisco, Aruba, Mist |
| Modèle | Model number | CW9178I, AP-505 |
| Référence constructeur | Part number | C9120AXI-E |
| Type Ant | Antenna type | Internal : omni downtilt |
| Indoor/Outdoor | Usage type | Indoor, Outdoor |
| Génération | Wi-Fi generation | Wi-Fi 6, Wi-Fi 6E, Wi-Fi 7 |
| ... | (32 columns total) | ... |

## 🔧 Troubleshooting

### Common Issues:

1. **"Excel file not found"**:
   - Make sure `Axians_Lyon_Comparatif_AP_v1.0.xlsx` exists
   - Check the filename matches exactly

2. **"YAML syntax error"**:
   - Run `./update_site.sh validate` to check current file
   - Check for special characters in Excel data

3. **"Python dependencies missing"**:
   ```bash
   pip3 install pandas openpyxl pyyaml
   ```

4. **"Permission denied"**:
   ```bash
   chmod +x update_site.sh
   ```

### Getting Help:

```bash
# Show script help
./update_site.sh help

# Show Python script help
python3 convert_excel_to_yaml.py --help
```

## � Deployment Guide - How It Actually Works

### Current Status: **Files Only** → Need to Set Up Hosting

Your AP database currently exists as **data files and scripts**. To make it a live website, you need to choose a deployment method:

### 🎯 **Deployment Options:**

#### **Option 1: GitHub Pages (Recommended - Free & Easy)**

**What it is:** GitHub automatically builds and hosts Jekyll sites for free.

**Setup (one-time):**
```bash
# 1. Set up Jekyll site structure
./setup_jekyll_site.sh

# 2. Create GitHub repository at github.com
# 3. Connect local folder to GitHub
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git add .
git commit -m "Initial Jekyll AP database setup"
git push -u origin main

# 4. Enable GitHub Pages in repository Settings → Pages → Source: Deploy from a branch
```

**Future updates:**
```bash
# Edit Excel → Run update → Deploy
./update_site.sh
./deploy.sh  # One command to commit and push
```

**Result:** Your site will be live at `https://USERNAME.github.io/REPOSITORY`

#### **Option 2: Internal Company Server**

**What it is:** Host on your company's web server.

**How it works:**
```bash
# Build the static site
bundle exec jekyll build

# Copy _site/ folder contents to your web server
# Site files go to: /var/www/html/ or similar
```

#### **Option 3: Cloud Hosting (Netlify, Vercel)**

**What it is:** Modern hosting platforms with automatic deployments.

**How it works:**
1. Connect your GitHub repository to Netlify/Vercel
2. They automatically build and deploy when you push changes
3. Often faster than GitHub Pages

#### **Option 4: Simple File Hosting**

**What it is:** Just serve the HTML files (no Jekyll processing).

**How it works:**
```bash
# Generate static HTML from current data
bundle exec jekyll build --disable-disk-cache

# Upload _site/ folder to any web hosting
# Works with: shared hosting, AWS S3, etc.
```

### 🔄 Deployment Summary

| Method | Complexity | Cost | Auto-Deploy | Best For |
|--------|------------|------|-------------|----------|
| GitHub Pages | Low | Free | Yes | Public/internal repos |
| Company Server | Medium | Varies | No | Corporate environments |
| Netlify/Vercel | Low | Free tier | Yes | Modern workflows |
| Simple Hosting | Low | Low cost | No | Basic needs |

## 🔄 Automation Ideas

1. **Git Hooks**: Set up pre-commit hooks to auto-convert Excel files
2. **CI/CD**: Use GitHub Actions to auto-deploy when Excel files change
3. **Web Interface**: Create a simple web form for non-technical users
4. **Email Integration**: Accept Excel files via email and auto-process

### Advanced Features:

- **Data validation**: Check for required fields, valid formats
- **Duplicate detection**: Prevent duplicate AP models
- **Price tracking**: Track price changes over time
- **Vendor APIs**: Auto-fetch specifications from vendor APIs

## 📈 Current Database Stats

Run `./update_site.sh stats` to see:
- Total number of APs
- Breakdown by manufacturer
- Wi-Fi generation distribution
- Indoor/Outdoor distribution

## 🎯 Quick Workflow Summary

**For adding new APs:**
1. Edit Excel → 2. Run `./update_site.sh` → 3. Test → 4. Deploy

**That's it!** 🎉