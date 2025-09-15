---
layout: default
title: Wi-Fi Access Points Database
---

<h1>Wi-Fi Access Points Specifications</h1>
<p>Filter, search, and explore AP models from multiple vendors. Database is updated regularly with new models.</p>

<!-- DataTable CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.4.1/css/buttons.dataTables.min.css">

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 14px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #2d3748;
}

/* Hidden probe row participates in layout sizing */
.width-probe { visibility: collapse; }
/* For browsers not honoring collapse fully */
tbody .width-probe td { padding:0 !important; border:none !important; font-size:0 !important; }
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
    background: #f8fafc;
    z-index: 1;
    padding: 16px 16px 120px 16px; /* extra bottom padding for pagination visibility */
    box-shadow: inset 0 0 20px rgba(0,0,0,0.1);
}

/* Ensure horizontal scroll works properly */
.dataTables_wrapper {
    width: 100%;
    overflow-x: auto;
    padding-bottom: 40px; /* ensure internal controls not cut off */
}

/* Additional safety space specifically for pagination bar */
.dataTables_wrapper .dataTables_paginate {
    margin-bottom: 20px;
}

/* Handle mobile safe-area (iOS notch) */
@supports (padding: max(0px)) {
  #ap-table-container { padding-bottom: calc(120px + env(safe-area-inset-bottom)); }
}

.dataTables_scroll {
    overflow-x: auto;
}
#ap-table {
    margin: 0 !important;
    font-size: 14px;
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    border-spacing: 0 !important;
    border-collapse: separate !important;
}

#ap-table thead th {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    font-weight: 600;
    padding: 16px 12px;
    text-align: left;
    border: none;
    font-size: 13px;
    letter-spacing: 0.025em;
    text-transform: uppercase;
    white-space: nowrap;
}

#ap-table tbody td {
    padding: 12px;
    border-bottom: 1px solid #e2e8f0;
    font-weight: 400;
    color: #4a5568;
    vertical-align: middle;
    white-space: nowrap;
}
#ap-table tbody tr:hover {
    background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
    transform: translateY(-1px);
    transition: all 0.2s ease;
}
#ap-table tbody tr:nth-child(even) {
    background: #f8fafc;
}

/* Control buttons styling */
.control-buttons {
    margin: 20px 0;
    text-align: center;
}

.font-btn {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    border: none;
    padding: 8px 16px;
    margin: 0 5px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.font-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.font-btn:active {
    transform: translateY(0);
}

/* DataTables integrated buttons styling */
.dt-buttons .dt-button {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
    color: #fff !important;
    border: none !important;
    padding: 8px 14px !important;
    margin: 0 6px 12px 0 !important;
    border-radius: 6px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
    transition: all 0.2s ease !important;
}
.dt-buttons .dt-button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
}
.dt-buttons .dt-button:active {
    transform: translateY(0) !important;
}

/* Specific font buttons (optional distinct style) */
.dt-font-btn {
    letter-spacing: 0.5px;
}

h1 {
    margin: 0 0 16px 0;
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
}
p {
    margin: 0 0 20px 0;
    font-size: 16px;
    text-align: center;
    color: #64748b;
    font-weight: 400;
}
.dataTables_wrapper .dataTables_filter input,
.dataTables_wrapper .dataTables_length select {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    padding: 8px 12px;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    background: white;
    transition: border-color 0.2s ease;
}
.dataTables_wrapper .dataTables_filter input:focus,
.dataTables_wrapper .dataTables_length select:focus {
    outline: none;
    border-color: #4f46e5;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}
.dataTables_wrapper .dataTables_info,
.dataTables_wrapper .dataTables_paginate {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    color: #64748b;
}
.dataTables_wrapper .dataTables_paginate .paginate_button {
    background: white;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
    color: #4a5568 !important;
    font-weight: 500;
    margin: 0 2px;
    padding: 6px 12px;
    transition: all 0.2s ease;
}
.dataTables_wrapper .dataTables_paginate .paginate_button:hover {
    background: #4f46e5 !important;
    border-color: #4f46e5 !important;
    color: white !important;
}
.dataTables_wrapper .dataTables_paginate .paginate_button.current {
    background: #4f46e5 !important;
    border-color: #4f46e5 !important;
    color: white !important;
}
.dt-buttons {
    margin-bottom: 16px;
}
.dt-button {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
    border: none !important;
    color: white !important;
    padding: 10px 16px !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    margin: 0 8px 0 0 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}
.dt-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important;
}
/* Column filter row */
thead tr.filter-row th {
    background: #eef2ff;
    padding: 4px 6px;
    border-bottom: 2px solid #cbd5e1;
}
thead tr.filter-row th input {
    width: 100%;
    box-sizing: border-box;
    padding: 4px 6px;
    font-size: 11px;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    background: #fff;
    font-family: 'Inter', sans-serif;
}
thead tr.filter-row th input:focus {
    outline: none;
    border-color: #6366f1;
    box-shadow: 0 0 0 2px rgba(99,102,241,0.25);
}
.stats-box {
    background: rgba(255, 255, 255, 0.9);
    border: none;
    border-radius: 12px;
    padding: 20px;
    margin: 0 0 24px 0;
    font-size: 14px;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}
.stats-box h3 {
    margin: 0 0 12px 0;
    font-size: 1.25rem;
    font-weight: 600;
    color: #2d3748;
}
.stat-item {
    display: inline-block;
    margin: 6px 16px 6px 0;
    font-weight: 500;
    color: #4a5568;
    background: #edf2f7;
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 13px;
}

/* DataTables column alignment fixes */
.dataTables_wrapper {
    width: 100%;
    overflow-x: auto;
}

/* Force header and body to use same table structure */
.dataTables_scrollHead,
.dataTables_scrollBody {
    overflow-x: auto;
}

.dataTables_scrollHeadInner {
    overflow-x: auto;
}

.dataTables_scrollBody table {
    border-top: none !important;
    margin: 0 !important;
}

/* Remove any borders between header and body */
div.dataTables_scrollHead table.dataTable {
    margin-bottom: 0 !important;
    border-bottom: none !important;
}

div.dataTables_scrollBody table {
    margin-top: 0 !important;
    border-top: none !important;
}
</style>

## 📱 WiFi Access Points Database

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
            <th>Indoor Outdoor</th>
            <th>Generation</th>
            <th>Protocol</th>
            <th>Product Positioning</th>
            <th>Concurrent PHY Radios</th>
            <th>Radio 2 4 GHz</th>
            <th>Radio 5 GHz</th>
            <th>Radio 6 GHz</th>
            <th>Dedicated Scanning Radio</th>
            <th>PoE Class</th>
            <th>Max PoE Consumption W</th>
            <th>Limited Capabilities PoE Plus 30W</th>
            <th>Limited Capabilities PoE 15W</th>
            <th>Ethernet1</th>
            <th>Ethernet2</th>
            <th>Weight kg</th>
            <th>Dimensions cm</th>
            <th>Geolocation FTM 80211mc 80211az</th>
            <th>USB Ports</th>
            <th>UWB</th>
            <th>GNSS</th>
            <th>Bluetooth</th>
            <th>Zigbee</th>
            <th>Cloud Compatible</th>
            <th>Minimum Version</th>
            <th>Public Price USD</th>
            <th>Public Price EUR</th>
            <th>Comments</th>


        </tr>
        <tr class="filter-row">
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
            <th><input type="text" placeholder="Filter" /></th>
        </tr>
    </thead>
    <tbody>
        <!-- Width probe row: representative max-length samples to stabilize column widths -->
        <tr class="width-probe">
            <td>VeryLongManufacturerNameSample</td>
            <td>Model-Extreme-9999X-Pro-Max</td>
            <td>MANUF-REF-SUPER-LONG-IDENTIFIER-12345</td>
            <td>External High-Gain Omni Directional Antenna Pack</td>
            <td>Indoor/Outdoor Industrial Hardened</td>
            <td>Wi-Fi 7 / 802.11be Gen</td>
            <td>802.11a/b/g/n/ac/ax/be Tri-Band</td>
            <td>High Density Enterprise Hospitality Stadium</td>
            <td>4x Concurrent Multi-Radio Chains</td>
            <td>4x4:4 2.4GHz MIMO</td>
            <td>8x8:8 5GHz MU-MIMO</td>
            <td>8x8:8 6GHz MU-MIMO</td>
            <td>Dedicated Security / WIPS / Sensor Radio Included</td>
            <td>PoE++ Class 8</td>
            <td>45.5 W</td>
            <td>Reduced Performance Mode @30W</td>
            <td>Basic Operation Mode @15W</td>
            <td>1 x 10G SFP+/RJ45 Combo</td>
            <td>1 x 2.5G Ethernet Port</td>
            <td>1.250 kg</td>
            <td>28 x 28 x 6.5 cm</td>
            <td>FTM + 802.11mc + 802.11az Enabled</td>
            <td>USB-C + USB-A</td>
            <td>Yes (UWB)</td>
            <td>Multi-Constellation GNSS</td>
            <td>BLE 5.4 Long Range</td>
            <td>Zigbee 3.0 Thread</td>
            <td>Cloud + On-Prem Controller Compatible</td>
            <td>Minimum Release 23.9.5</td>
            <td>9999 USD</td>
            <td>8999 EUR</td>
            <td>Sample longest realistic comments text to anchor width sizing baseline.</td>
        </tr>
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
            <td>{{ ap.GNSS | default: "" }}</td>
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
<script src="https://cdn.datatables.net/buttons/2.4.1/js/dataTables.buttons.min.js"></script>
<script src="https://cdn.datatables.net/buttons/2.4.1/js/buttons.colVis.min.js"></script>

<script>
$(document).ready(function() {
    // Initialize DataTable with buttons but minimal other features
    var table = $('#ap-table').DataTable({
        // Core settings
        paging: true,
        searching: true,
        info: true,
        ordering: true,
        
        // Layout control - bring back buttons
        dom: 'Bfrtip',
        buttons: [
            'colvis',
            {
                text: 'A-',
                className: 'dt-font-btn dt-font-dec',
                action: function (e, dt, node, config) { changeFontSize(-1); }
            },
            {
                text: 'A+',
                className: 'dt-font-btn dt-font-inc',
                action: function (e, dt, node, config) { changeFontSize(1); }
            },
            {
                text: 'Clear Filters',
                className: 'dt-clear-filters',
                action: function(e, dt, node, config){
                    $('#ap-table thead tr.filter-row th input').val('');
                    dt.columns().every(function(){ this.search(''); });
                    dt.draw();
                }
            }
        ],
        orderCellsTop: true,
        initComplete: function(){
            var api = this.api();
            // Attach events to each filter input
            api.columns().every(function(colIdx){
                var column = this;
                var input = $(api.table().header()).find('tr.filter-row th').eq(colIdx).find('input');
                if(!input.length) return;
                input.on('keyup change clear', function(){
                    var val = this.value;
                    if(column.search() !== val){
                        column.search(val, false, true).draw();
                    }
                });
            });
        },
        
        autoWidth: false,
        
        // Pagination
        pageLength: 25,
        lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
        
        // Default sort
        order: [[ 0, "asc" ]],
        
        // Language
        language: {
            search: "🔍 Search:",
            lengthMenu: "Show _MENU_ entries per page",
            info: "Showing _START_ to _END_ of _TOTAL_ access points",
            infoEmpty: "No access points found",
            infoFiltered: "(filtered from _MAX_ total access points)",
            zeroRecords: "No matching access points found",
            paginate: {
                first: "« First",
                last: "Last »",
                next: "Next ›",
                previous: "‹ Previous"
            }
        },
        // Adjust displayed counts to exclude probe row
        infoCallback: function(settings, start, end, max, total, pre) {
            // Subtract the single probe row from counts if present
            var adjustedTotal = total > 0 ? total - 1 : 0;
            var adjustedMax = max > 0 ? max - 1 : 0;
            // Adjust start/end if they include the probe row (which is always first)
            var displayStart = start > 1 ? start - 1 : start;
            var displayEnd = end - 1;
            if (displayEnd < 0) displayEnd = 0;
            if (displayStart === 1 && adjustedTotal === 0) {
                return 'No access points found';
            }
            return 'Showing ' + displayStart + ' to ' + displayEnd + ' of ' + adjustedTotal + ' access points';
        },
        
        // Column definitions - ensure no special behavior
        columnDefs: [
            {
                targets: '_all',
                orderable: true,
                className: 'no-wrap'
            }
        ]
    });

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
</script>

---

## 🔄 How to Update This Database

1. **Edit Excel File**: Update `wifi-ap-database.xlsx` with new AP data
2. **Run Update Script**: `./update_database.sh`
3. **Commit Changes**: `git add . && git commit -m "Update AP database"`
4. **Deploy**: `git push origin main`

The site will automatically rebuild and deploy via GitHub Pages.
