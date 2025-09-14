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
