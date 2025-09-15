---
layout: default
title: Wi-Fi Access Points Database
---

<h1>Wi-Fi Access Points Specifications</h1>
<p>Filter, search, and explore AP models from multiple vendors. Database is updated regularly with new models.</p>

<!-- DataTable CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.4.1/css/responsive.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.4.1/css/buttons.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/colreorder/1.7.0/css/colReorder.dataTables.min.css">

<style>
body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-size: 13px;
}
.font-size-btns {
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}
#ap-table-container {
    width: 100vw;
    height: 100vh;
    overflow: auto;
    position: fixed;
    top: 0;
    left: 0;
    background: #f5f5f5;
    z-index: 1;
    padding: 8px 4px 4px 4px;
}
#ap-table {
    margin: 0;
    width: 100% !important;
    font-size: 12px;
    table-layout: fixed;
}
h1 {
    margin: 12px 0 8px 0;
    font-size: 1.3em;
}
p {
    margin: 4px 0 12px 0;
    font-size: 1em;
}
.dataTables_wrapper .dataTables_filter input,
.dataTables_wrapper .dataTables_length select {
    font-size: 12px;
    padding: 2px 4px;
}
.stats-box {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 10px;
    margin: 8px 0;
    font-size: 11px;
}
.stat-item {
    display: inline-block;
    margin: 3px 10px 3px 0;
    font-weight: bold;
}
</style>

<div class="stats-box">
    <h3>📊 Database Statistics</h3>
    {% assign total_aps = site.data.ap_models | size %}
    
    <div class="stat-item">🔢 Total APs: {{ total_aps }}</div>
    <div class="stat-item">🕒 Last updated: {{ site.time | date: "%Y-%m-%d %H:%M" }}</div>
</div>

<div id="ap-table-container">
<table id="ap-table" class="display" style="width:100%">
    <thead>
        <tr>
            <th>Manufacturer</th>
            <th>Model</th>
            <th>Manufacturer Reference</th>
            <th>Antenna Type</th>
            <th>Indoor/Outdoor</th>
            <th>Generation</th>
            <th>Protocol</th>
            <th>Product Positioning</th>
            <th>Concurrent PHY Radios</th>
            <th>Radio 2.4 GHz</th>
            <th>Radio 5 GHz</th>
            <th>Radio 6 GHz</th>
            <th>Dedicated Scanning Radio</th>
            <th>PoE Class</th>
            <th>Max PoE Consumption (W)</th>
            <th>Limited Capabilities PoE+ 30W</th>
            <th>Limited Capabilities PoE 15W</th>
            <th>Ethernet1</th>
            <th>Ethernet2</th>
            <th>Weight (kg)</th>
            <th>Dimensions (cm)</th>
            <th>Geolocation FTM</th>
            <th>USB Ports</th>
            <th>UWB</th>
            <th>GPS</th>
            <th>Bluetooth</th>
            <th>Zigbee</th>
            <th>Cloud Compatible</th>
            <th>Minimum Version</th>
            <th>Public Price (USD)</th>
            <th>Public Price (EUR)</th>
            <th>Comments</th>
        </tr>
    </thead>
    <tbody>
        {% for ap in site.data.ap_models %}
        <tr>
            <td>{{ ap.Manufacturer | default: "" }}</td>
            <td>{{ ap.Model | default: "" }}</td>
            <td>{{ ap.Manufacturer_Reference | default: "" }}</td>
            <td>{{ ap.Antenna_Type | default: "" }}</td>
            <td>{{ ap.Indoor_Outdoor | default: "" }}</td>
            <td>{{ ap.Generation | default: "" }}</td>
            <td>{{ ap.Protocol | default: "" }}</td>
            <td>{{ ap.Product_Positioning | default: "" }}</td>
            <td>{{ ap.Concurrent_PHY_Radios | default: "" }}</td>
            <td>{{ ap.Radio_2_4_GHz | default: "" }}</td>
            <td>{{ ap.Radio_5_GHz | default: "" }}</td>
            <td>{{ ap.Radio_6_GHz | default: "" }}</td>
            <td>{{ ap.Dedicated_Scanning_Radio | default: "" }}</td>
            <td>{{ ap.PoE_Class | default: "" }}</td>
            <td>{{ ap.Max_PoE_Consumption_W | default: "" }}</td>
            <td>{{ ap.Limited_Capabilities_PoE_Plus_30W | default: "" }}</td>
            <td>{{ ap.Limited_Capabilities_PoE_15W | default: "" }}</td>
            <td>{{ ap.Ethernet1 | default: "" }}</td>
            <td>{{ ap.Ethernet2 | default: "" }}</td>
            <td>{{ ap.Weight_kg | default: "" }}</td>
            <td>{{ ap.Dimensions_cm | default: "" }}</td>
            <td>{{ ap.Geolocation_FTM_80211mc_80211az | default: "" }}</td>
            <td>{{ ap.USB_Ports | default: "" }}</td>
            <td>{{ ap.UWB | default: "" }}</td>
            <td>{{ ap.GPS | default: "" }}</td>
            <td>{{ ap.Bluetooth | default: "" }}</td>
            <td>{{ ap.Zigbee | default: "" }}</td>
            <td>{{ ap.Cloud_Compatible | default: "" }}</td>
            <td>{{ ap.Minimum_Version | default: "" }}</td>
            <td>{{ ap.Public_Price_USD | default: "" }}</td>
            <td>{{ ap.Public_Price_EUR | default: "" }}</td>
            <td>{{ ap.Comments | default: "" }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
</div>

<!-- jQuery and DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/responsive/2.4.1/js/dataTables.responsive.min.js"></script>
<script src="https://cdn.datatables.net/buttons/2.4.1/js/dataTables.buttons.min.js"></script>
<script src="https://cdn.datatables.net/buttons/2.4.1/js/buttons.colVis.min.js"></script>
<script src="https://cdn.datatables.net/colreorder/1.7.0/js/dataTables.colReorder.min.js"></script>

<script>
$(document).ready(function() {
    // Use DataTables with enhanced features
    $('#ap-table').css('table-layout', 'fixed');
    var table = $('#ap-table').DataTable({
        paging: true,
        searching: true,
        info: true,
        responsive: false,
        colReorder: true,
        dom: 'Bfrtip',
        buttons: [
            'colvis',
            {
                text: '<span id="font-size-controls"><button onclick="changeFontSize(-1)">A-</button> <button onclick="changeFontSize(1)">A+</button></span>',
                className: 'font-size-btns',
                action: function () {}
            }
        ],
        scrollX: true,
        pageLength: 25,
        lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
        order: [[ 0, "asc" ]],
        columnDefs: [
            { responsivePriority: 1, targets: [0, 1] }, // Manufacturer, Model
            { responsivePriority: 2, targets: [4, 5] }, // Indoor/Outdoor, Generation
        ],
        language: {
            search: "🔍 Search all columns:",
            lengthMenu: "Show _MENU_ entries per page",
            info: "Showing _START_ to _END_ of _TOTAL_ access points",
            infoEmpty: "No access points found",
            infoFiltered: "(filtered from _MAX_ total entries)"
        }
    });
    
    table.on('draw', function() {
        table.columns.adjust();
    });
    $(window).on('resize', function() {
        table.columns.adjust();
    });
    table.columns.adjust();
});

// Font size controls
var minFont = 9, maxFont = 20;
function changeFontSize(delta) {
    var table = document.getElementById('ap-table');
    var style = window.getComputedStyle(table, null).getPropertyValue('font-size');
    var current = parseFloat(style);
    var newSize = Math.max(minFont, Math.min(maxFont, current + delta));
    // Set font size on the table and wrapper
    table.style.fontSize = newSize + 'px';
    var wrapper = document.getElementById('ap-table-container');
    if (wrapper) wrapper.style.fontSize = newSize + 'px';
    // Remove any explicit font-size on th/td to let inherit from table
    var ths = table.querySelectorAll('th');
    var tds = table.querySelectorAll('td');
    ths.forEach(function(el) { el.style.fontSize = null; });
    tds.forEach(function(el) { el.style.fontSize = null; });
    // Also update filter and length controls
    var controls = document.querySelectorAll('.dataTables_wrapper .dataTables_filter input, .dataTables_wrapper .dataTables_length select');
    controls.forEach(function(el) { el.style.fontSize = newSize + 'px'; });
    // Force DataTables to recalculate column widths
    if ($.fn.dataTable) {
        $('#ap-table').DataTable().columns.adjust().draw(false);
    }
}
</script>

---

## 🔄 How to Update This Database

1. **Edit Excel File**: Update `wifi-ap-database.xlsx` with new AP data
2. **Run Update Script**: `./update_database.sh`
3. **Commit Changes**: `git add . && git commit -m "Update AP database"`
4. **Deploy**: `git push origin main`

The site will automatically rebuild and deploy via GitHub Pages.
