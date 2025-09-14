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
    
    <div class="stat-item">🔢 Total APs: {{ total_aps }}</div>
    <div class="stat-item">🕒 Last updated: {{ site.time | date: "%Y-%m-%d %H:%M" }}</div>
</div>

<div id="ap-table-container">
<table id="ap-table" class="display responsive nowrap" style="width:100%">
    <thead>
        <tr>
            <th>Constructeur</th>
            <th>Modèle</th>
            <th>Référence constructeur</th>
            <th>Type Ant</th>
            <th>Indoor/Outdoor</th>
            <th>Génération</th>
            <th>Protocole</th>
            <th>Positionnement gamme</th>
            <th>Nbre de radios PHY simultanées</th>
            <th>Radio 2,4 GHz</th>
            <th>Radio 5 GHz</th>
            <th>Radio 6 GHz</th>
            <th>Dedicated scanning radio</th>
            <th>Classe PoE</th>
            <th>Consomation max PoE (W)</th>
            <th>Capacités limitées en PoE+ 30W</th>
            <th>Capacités limitées en PoE 15W</th>
            <th>Ethernet1</th>
            <th>Ethernet2</th>
            <th>Poids (kg)</th>
            <th>Dimensions (cm)</th>
            <th>Geoloc FTM (.11mc, .11az)</th>
            <th>Ports USB</th>
            <th>UWB</th>
            <th>GPS</th>
            <th>Bluetooth</th>
            <th>Zigbee</th>
            <th>Compatible Cloud</th>
            <th>Version Minimum</th>
            <th>Prix public ($)</th>
            <th>Prix public (Euros)</th>
            <th>Commentaire</th>
        </tr>
    </thead>
    <tbody>
        {% for ap in site.data.ap_models %}
        <tr>
            <td>{{ ap.Constructeur | default: "" }}</td>
            <td>{{ ap.Modèle | default: "" }}</td>
            <td>{{ ap["Référence constructeur"] | default: "" }}</td>
            <td>{{ ap["Type Ant"] | default: "" }}</td>
            <td>{{ ap["Indoor/Outdoor"] | default: "" }}</td>
            <td>{{ ap.Génération | default: "" }}</td>
            <td>{{ ap.Protocole | default: "" }}</td>
            <td>{{ ap["Positionnement gamme"] | default: "" }}</td>
            <td>{{ ap["Nbre de radios PHY simultanées"] | default: "" }}</td>
            <td>{{ ap["Radio 2,4 GHz"] | default: "" }}</td>
            <td>{{ ap["Radio 5 GHz"] | default: "" }}</td>
            <td>{{ ap["Radio 6 GHz"] | default: "" }}</td>
            <td>{{ ap["Dedicated scanning radio"] | default: "" }}</td>
            <td>{{ ap["Classe PoE"] | default: "" }}</td>
            <td>{{ ap["Consomation max PoE (W)"] | default: "" }}</td>
            <td>{{ ap["Capacités limitées en PoE+ 30W"] | default: "" }}</td>
            <td>{{ ap["Capacités limitées en PoE 15W"] | default: "" }}</td>
            <td>{{ ap.Ethernet1 | default: "" }}</td>
            <td>{{ ap.Ethernet2 | default: "" }}</td>
            <td>{{ ap["Poids (kg)"] | default: "" }}</td>
            <td>{{ ap["Dimensions (cm)"] | default: "" }}</td>
            <td>{{ ap["Geoloc FTM (.11mc, .11az)"] | default: "" }}</td>
            <td>{{ ap["Ports USB"] | default: "" }}</td>
            <td>{{ ap.UWB | default: "" }}</td>
            <td>{{ ap.GPS | default: "" }}</td>
            <td>{{ ap.Bluetooth | default: "" }}</td>
            <td>{{ ap.Zigbee | default: "" }}</td>
            <td>{{ ap["Compatible Cloud"] | default: "" }}</td>
            <td>{{ ap["Version Minimum"] | default: "" }}</td>
            <td>{{ ap["Prix public ($)"] | default: "" }}</td>
            <td>{{ ap["Prix public (Euros)"] | default: "" }}</td>
            <td>{{ ap.Commentaire | default: "" }}</td>
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

## 🔄 How to Update This Database

1. **Edit Excel File**: Update `Axians_Lyon_Comparatif_AP_v1.0.xlsx` with new AP data
2. **Run Update Script**: `./update_site.sh`
3. **Commit Changes**: `git add . && git commit -m "Update AP database"`
4. **Deploy**: `git push origin main`

The site will automatically rebuild and deploy via GitHub Pages.
