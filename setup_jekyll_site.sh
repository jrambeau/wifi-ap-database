#!/bin/bash
# =============================================================================
# Jekyll Site Setup Script for GitHub Pages Deployment
# =============================================================================
# This script sets up a complete Jekyll site structure for easy deployment
# =============================================================================

set -e

echo "🚀 Setting up Jekyll Site for GitHub Pages Deployment"
echo "================================================="

# Check if we're already in a git repo
if [ -d ".git" ]; then
    echo "✅ Git repository already exists"
else
    echo "📁 Initializing Git repository..."
    git init
    echo "*.xlsx" >> .gitignore
    echo "_site/" >> .gitignore
    echo ".sass-cache/" >> .gitignore
    echo ".jekyll-cache/" >> .gitignore
    echo ".jekyll-metadata" >> .gitignore
    echo "Gemfile.lock" >> .gitignore
fi

# Create Jekyll site structure
echo "🏗️  Creating Jekyll site structure..."

# Create _config.yml
cat > _config.yml << 'EOF'
title: "Wi-Fi Access Points Database"
description: "Comprehensive database of Wi-Fi Access Point specifications"
baseurl: "" # the subpath of your site, e.g. /blog
url: "" # the base hostname & protocol for your site

# Build settings
markdown: kramdown
highlighter: rouge
plugins:
  - jekyll-feed

# Collections
collections:
  data:
    output: false

# Exclude from processing
exclude:
  - README.md
  - Gemfile
  - Gemfile.lock
  - convert_excel_to_yaml.py
  - update_site.sh
  - "*.xlsx"
  - "*.backup_*"

# GitHub Pages settings
remote_theme: pages-themes/minimal@v0.2.0
plugins:
  - jekyll-remote-theme
EOF

# Create Gemfile
cat > Gemfile << 'EOF'
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "jekyll-remote-theme"

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
EOF

# Create _data directory and move yaml file
mkdir -p _data
if [ -f "ap_models.yaml" ]; then
    mv ap_models.yaml _data/
    echo "📁 Moved ap_models.yaml to _data/ directory"
fi

# Update ap_table.md to be the index page
cat > index.md << 'EOF'
---
layout: default
title: Wi-Fi Access Points Database
---

# Wi-Fi Access Points Specifications Database

Filter, search, and explore AP models from multiple vendors. Database is updated regularly with new models.

<!-- DataTable CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.4.1/css/responsive.dataTables.min.css">

<style>
.stats-box {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 15px;
    margin: 20px 0;
}
.stat-item {
    display: inline-block;
    margin: 5px 15px 5px 0;
    font-weight: bold;
}
#ap-table {
    font-size: 12px;
}
</style>

<div class="stats-box">
    <h3>📊 Database Statistics</h3>
    {% assign total_aps = site.data.ap_models | size %}
    {% assign manufacturers = site.data.ap_models | map: "Constructeur" | uniq | sort %}
    {% assign generations = site.data.ap_models | map: "Génération" | uniq | sort %}
    
    <div class="stat-item">🔢 Total APs: {{ total_aps }}</div>
    <div class="stat-item">🏭 Manufacturers: {{ manufacturers | size }}</div>
    <div class="stat-item">📡 Generations: {{ generations | size }}</div>
    <div class="stat-item">🕒 Last updated: {{ site.time | date: "%Y-%m-%d %H:%M" }}</div>
</div>

<div id="ap-table-container">
<table id="ap-table" class="display responsive nowrap" style="width:100%">
    <thead>
        <tr>
            {% assign first = site.data.ap_models[0] %}
            {% for col in first %}
            <th>{{ col[0] }}</th>
            {% endfor %}
        </tr>
    </thead>
    <tbody>
        {% for ap in site.data.ap_models %}
        <tr>
            {% for col in ap %}
            <td>{{ col[1] | default: "" }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </tbody>
</table>
</div>

<!-- DataTable JavaScript -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/responsive/2.4.1/js/dataTables.responsive.min.js"></script>

<script>
$(document).ready(function() {
    $('#ap-table').DataTable({
        responsive: true,
        pageLength: 25,
        lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
        order: [[ 0, "asc" ]],
        columnDefs: [
            { responsivePriority: 1, targets: [0, 1] }, // Manufacturer, Model
            { responsivePriority: 2, targets: [4, 5] }, // Indoor/Outdoor, Generation
            { responsivePriority: 3, targets: -1 } // Last column
        ],
        language: {
            search: "🔍 Search all columns:",
            lengthMenu: "Show _MENU_ entries per page",
            info: "Showing _START_ to _END_ of _TOTAL_ access points",
            infoEmpty: "No access points found",
            infoFiltered: "(filtered from _MAX_ total entries)"
        }
    });
});
</script>

---

### 🔄 How to Update This Database

1. **Edit Excel File**: Update `Axians_Lyon_Comparatif_AP_v1.0.xlsx` with new AP data
2. **Run Update Script**: `./update_site.sh`
3. **Commit Changes**: `git add . && git commit -m "Update AP database"`
4. **Deploy**: `git push origin main`

The site will automatically rebuild and deploy via GitHub Pages.

### 📈 Manufacturers in Database
{% for manufacturer in manufacturers %}
- **{{ manufacturer }}**: {{ site.data.ap_models | where: "Constructeur", manufacturer | size }} models
{% endfor %}
EOF

# Remove old ap_table.md if it exists
[ -f "ap_table.md" ] && rm ap_table.md

# Create a simple deployment script
cat > deploy.sh << 'EOF'
#!/bin/bash
# Simple deployment script

echo "🚀 Deploying Jekyll AP Database..."

# Check if there are changes
if git diff --quiet && git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "📝 Committing changes..."
    git add .
    read -p "Enter commit message (or press Enter for default): " commit_msg
    if [ -z "$commit_msg" ]; then
        commit_msg="Update AP database - $(date +'%Y-%m-%d %H:%M')"
    fi
    git commit -m "$commit_msg"
fi

echo "📤 Pushing to GitHub..."
git push origin main

echo "✅ Deployment complete!"
echo "🌐 Your site will be available at: https://USERNAME.github.io/REPOSITORY"
echo "⏱️  GitHub Pages builds usually take 1-2 minutes"
EOF

chmod +x deploy.sh

echo ""
echo "✅ Jekyll site structure created!"
echo ""
echo "🎯 Next Steps:"
echo "1. Create a GitHub repository for this project"
echo "2. git remote add origin https://github.com/USERNAME/REPOSITORY.git"
echo "3. git add ."
echo "4. git commit -m 'Initial Jekyll AP database setup'"
echo "5. git branch -M main"
echo "6. git push -u origin main"
echo "7. Enable GitHub Pages in repository settings"
echo ""
echo "📝 Files created:"
echo "   - _config.yml (Jekyll configuration)"
echo "   - Gemfile (Ruby dependencies)"
echo "   - index.md (Main page with AP table)"
echo "   - deploy.sh (Easy deployment script)"
echo "   - .gitignore (Git ignore rules)"
echo ""
echo "🔄 To update in the future:"
echo "   1. Edit Excel file"
echo "   2. ./update_site.sh"
echo "   3. ./deploy.sh"