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
    padding: 16px;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.1);
}

/* Ensure horizontal scroll works properly */
.dataTables_wrapper {
    width: 100%;
    overflow-x: auto;
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
    table-layout: fixed; /* Prevent recalculation of widths on sort */
    width: 3000px; /* Large enough fixed width for all columns */
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
}

/* Equal width distribution prevents shifting */
#ap-table thead th, #ap-table tbody td {
    width: 95px; /* uniform width */
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Allow scroll if viewport narrower */
#ap-table-container { overflow-x: auto; }
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
            
            
            <th title="Manufacturer">Manufacturer</th>
            <th title="Model">Model</th>
            <th title="Manufacturer Reference">Manufacturer Reference</th>
            <th title="Antenna Type">Antenna Type</th>
            <th title="Indoor or Outdoor category">Indoor Outdoor</th>
            <th title="Generation">Generation</th>
            <th title="Protocol / Wi-Fi standard">Protocol</th>
            <th title="Product positioning / target market">Product Positioning</th>
            <th title="Number of concurrent PHY radios">Concurrent PHY Radios</th>
            <th title="2.4 GHz radio details">Radio 2 4 GHz</th>
            <th title="5 GHz radio details">Radio 5 GHz</th>
            <th title="6 GHz radio details">Radio 6 GHz</th>
            <th title="Dedicated scanning / security radio">Dedicated Scanning Radio</th>
            <th title="PoE Class">PoE Class</th>
            <th title="Maximum PoE power consumption (Watts)">Max PoE Consumption W</th>
            <th title="Capabilities when limited to 30W PoE+">Limited Capabilities PoE Plus 30W</th>
            <th title="Capabilities when limited to 15W PoE">Limited Capabilities PoE 15W</th>
            <th title="Ethernet Port 1 details">Ethernet1</th>
            <th title="Ethernet Port 2 details">Ethernet2</th>
            <th title="Weight (kg)">Weight kg</th>
            <th title="Physical dimensions (cm)">Dimensions cm</th>
            <th title="Geolocation FTM / 802.11mc / 802.11az support">Geolocation FTM 80211mc 80211az</th>
            <th title="USB Ports availability">USB Ports</th>
            <th title="Ultra WideBand support">UWB</th>
            <th title="GNSS capability">GNSS</th>
            <th title="Bluetooth support">Bluetooth</th>
            <th title="Zigbee support">Zigbee</th>
            <th title="Cloud management compatibility">Cloud Compatible</th>
            <th title="Minimum firmware/software version">Minimum Version</th>
            <th title="Public list price in USD">Public Price USD</th>
            <th title="Public list price in EUR">Public Price EUR</th>
            <th title="Additional comments">Comments</th>


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
                action: function (e, dt, node, config) {
                    changeFontSize(-1);
                }
            },
            {
                text: 'A+',
                className: 'dt-font-btn dt-font-inc',
                action: function (e, dt, node, config) {
                    changeFontSize(1);
                }
            }
        ],
        
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
        
        // Column definitions - ensure no special behavior
        columnDefs: [
            {
                targets: '_all',
                orderable: true,
                className: 'no-wrap'
            }
        ]
    });

    // Lock column widths after first draw
    var locked = false;
    function lockWidths() {
        if (locked) return;
        var headerCells = $('#ap-table thead th');
        headerCells.each(function(index) {
            var w = $(this).outerWidth();
            // Apply width to header and all cells in column
            $(this).css('width', w + 'px');
            $('#ap-table tbody tr').each(function() {
                var cell = $(this).find('td').eq(index);
                cell.css('width', w + 'px');
            });
        });
        locked = true;
    }
    table.on('draw', function(){ lockWidths(); });
    lockWidths();

    // Maintain widths on events that could trigger recalculation
    table.on('order.dt search.dt page.dt', function(){
        $('#ap-table thead th, #ap-table tbody td').each(function(){
            var w = $(this).outerWidth();
            $(this).css('width', w + 'px');
        });
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
