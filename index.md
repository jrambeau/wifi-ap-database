---
layout: default
title: Wi-Fi Access Points Database
---

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
    font-size: var(--table-font-size, 14px);
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
    overflow-y: auto; /* allow vertical scroll only here */
    overflow-x: hidden; /* prevent horizontal scroll at this level so sticky works */
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
    overflow-x: auto; /* single horizontal scroll context */
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
    font-size: var(--table-font-size, 14px);
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
    font-size: calc(var(--table-font-size, 14px) * 0.93); /* scales with controls */
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
/* Layout container adjustments for buttons + global search */
.dt-buttons, .dataTables_filter { display: inline-flex; align-items: center; gap: 8px; }
.dt-buttons { flex-wrap: wrap; }
.dataTables_filter { margin: 0 0 12px 8px; }
.dataTables_filter label { display: flex; align-items: center; gap: 6px; font-weight:500; color:#4a5568; }
.dataTables_filter input { margin-left: 0 !important; }
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
/* Inline search placement inside buttons bar */
.dt-buttons .dt-inline-search { display:inline-flex; align-items:center; margin-left:4px; }
.dt-buttons .dt-inline-search input { 
    font-family:'Inter',sans-serif; 
    font-size:13px; 
    padding:8px 12px; 
    border:2px solid #e2e8f0; 
    border-radius:6px; 
    background:#fff; 
    transition:border-color .2s ease; 
}
.dt-buttons .dt-inline-search input:focus { outline:none; border-color:#4f46e5; box-shadow:0 0 0 3px rgba(79,70,229,0.15); }
.compact-mode .dt-buttons .dt-inline-search input { padding:4px 8px; font-size:12px; }
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
/* --- Sticky first two columns (Vendor, Model) --- */
/* CSS variable updated dynamically to match actual first column width */
:root { 
    --sticky-col-1-width: 0px; 
    /* Refined aesthetic backgrounds for sticky columns */
    --sticky-col-bg: linear-gradient(90deg, #ffffff 0%, #f5f7fa 100%);
    --sticky-col-bg-alt: linear-gradient(90deg, #f9fafb 0%, #f1f5f9 100%);
    --sticky-col-bg-hover: linear-gradient(90deg, #f1f5f9 0%, #e2e8f0 100%);
}
#ap-table thead { position: sticky; top: 0; z-index: 20; }
#ap-table thead tr.filter-row { position: sticky; top: var(--sticky-header-height, 0px); z-index: 19; }
#ap-table thead tr.filter-row th { position: sticky; top: var(--sticky-header-height, 0px); }
#ap-table .sticky-col { position: sticky; left: 0; z-index: 5; }
#ap-table thead .sticky-col { z-index: 8; /* keep gradient from #ap-table thead th */ }
#ap-table thead tr.filter-row .sticky-col { z-index: 7; background: #f1f5f9; box-shadow:none; }
/* Neutral, subtle gradient backgrounds for sticky columns */
#ap-table tbody .sticky-col.sticky-col-1, 
#ap-table tbody .sticky-col.sticky-col-2 { 
    background: var(--sticky-col-bg); 
    transition: background 0.25s ease; 
}
#ap-table tbody tr:nth-child(even) .sticky-col.sticky-col-1, 
#ap-table tbody tr:nth-child(even) .sticky-col.sticky-col-2 { 
    background: var(--sticky-col-bg-alt); 
}
#ap-table tbody tr:hover .sticky-col.sticky-col-1, 
#ap-table tbody tr:hover .sticky-col.sticky-col-2 { 
    background: var(--sticky-col-bg-hover); 
}
#ap-table tbody .sticky-col { background: #ffffff; }
#ap-table tbody tr:nth-child(even) .sticky-col { background: #f8fafc; }
#ap-table tbody tr:hover .sticky-col { background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); }
/* Soft fade edge to emphasize separation */
/* No fade on filter row sticky cells */
#ap-table .sticky-col-1 { border-right: 1px solid #e2e8f0; }
#ap-table .sticky-col-2 { left: var(--sticky-col-1-width); border-right: 1px solid #e2e8f0; }

/* Compact mode adjustments */
.compact-mode #ap-table thead th { padding: 8px 8px; }
.compact-mode #ap-table thead tr.filter-row th { padding: 2px 4px; }
.compact-mode #ap-table thead tr.filter-row th input { padding: 2px 4px; font-size: 10px; }
.compact-mode #ap-table tbody td { padding: 4px 8px; }
.compact-mode #ap-table { }
.compact-mode .dataTables_wrapper .dataTables_filter input, 
.compact-mode .dataTables_wrapper .dataTables_length select { padding:4px 8px; font-size:12px; }
.compact-mode .dt-buttons .dt-button { padding:6px 10px !important; font-size:12px !important; }

/* Sticky header blur effect */
#ap-table thead { background: rgba(79,70,229,0.92); backdrop-filter: saturate(140%) blur(6px); -webkit-backdrop-filter:saturate(140%) blur(6px); }
#ap-table thead.scrolled { background: rgba(79,70,229,0.80); }
#ap-table thead th { transition: background 0.25s ease; }
#ap-table thead.scrolled th { background: linear-gradient(135deg, rgba(79,70,229,0.95) 0%, rgba(124,58,237,0.95) 100%); }
/* Remove all separator effects (shadows & fades) for a flat appearance */
#ap-table .sticky-col-1::after, #ap-table .sticky-col-2::after { display:none; }
/* Prevent probe row artifacts */
#ap-table tbody tr.width-probe .sticky-col { box-shadow: none !important; background: transparent !important; }
</style>

<div id="ap-table-container">
<table id="ap-table" class="display" style="width:100%">
    <thead>
        <tr>
            
            
            
            
            
            
            
            
            
            <th class="sticky-col sticky-col-1">Vendor</th>
            <th class="sticky-col sticky-col-2">Model</th>
            <th>Reference</th>
            <th>Antenna_Type</th>
            <th>Indoor_Outdoor</th>
            <th>Generation</th>
            <th>Product_Positioning</th>
            <th>Total_PHY_Serving_Radios</th>
            <th>Concurrent_Serving_Radios</th>
            <th>Serving_Radio_1</th>
            <th>Serving_Radio_2</th>
            <th>Serving_Radio_3</th>
            <th>Serving_Radio_4</th>
            <th>Dedicated_Scanning_Radio</th>
            <th>PoE_Class</th>
            <th>Max_PoE_Consumption_W</th>
            <th>Limited_Capabilities_PoE_bt_Class5_45W</th>
            <th>Limited_Capabilities_PoE_at_30W</th>
            <th>Limited_Capabilities_PoE_af_15W</th>
            <th>Ethernet1</th>
            <th>Ethernet2</th>
            <th>Weight_kg</th>
            <th>Dimensions_cm</th>
            <th>Geolocation_FTM_80211mc_80211az</th>
            <th>USB_Ports</th>
            <th>UWB</th>
            <th>GNSS</th>
            <th>Bluetooth</th>
            <th>Zigbee</th>
            <th>Minimum_Software_Version</th>
            <th>Public_Price_USD</th>
            <th>Public_Price_EUR</th>
            <th>Comments</th>







        </tr>
    </thead>
    <tbody>
        <!-- Width probe row: representative max-length samples to stabilize column widths -->
        <tr class="width-probe">
            <td class="sticky-col sticky-col-1">VeryLongVendorNameSample</td>
            <td class="sticky-col sticky-col-2">Model-Extreme-9999X-Pro-Max</td>
            <td>MANUF-REF-SUPER-LONG-IDENTIFIER-12345</td>
            <td>External High-Gain Omni Directional Antenna Pack</td>
            <td>Indoor/Outdoor Industrial Hardened</td>
            <td>Wi-Fi 7 / 802.11be Gen</td>
            <td>High Density Enterprise Hospitality Stadium</td>
            <td>4x Concurrent Multi-Radio Chains</td>
            <td>4x Concurrent Multi-Radio Chains</td>
            <td>4x4:4 2.4GHz MIMO</td>
            <td>8x8:8 5GHz MU-MIMO</td>
            <td>8x8:8 5GHz MU-MIMO</td>
            <td>8x8:8 6GHz MU-MIMO</td>
            <td>Dedicated Security / WIPS / Sensor Radio Included</td>
            <td>PoE++ Class 8</td>
            <td>45.5 W</td>
            <td>Reduced Performance Mode @45W</td>
            <td>Basic Operation Mode @30W</td>
            <td>Limited Features @15W</td>
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
            <td>Minimum Release 23.9.5</td>
            <td>9999 USD</td>
            <td>8999 EUR</td>
            <td>Sample longest realistic comments text to anchor width sizing baseline.</td>







        </tr>
        {% for ap in site.data.ap_models %}
        <tr>
            
            
            
            
            
            
            
            
            
            <td class="sticky-col sticky-col-1">{{ ap.Vendor | default: "" }}</td>
            <td class="sticky-col sticky-col-2">{{ ap.Model | default: "" }}</td>
            <td>{{ ap.Reference | default: "" }}</td>
            <td>{{ ap.Antenna_Type | default: "" }}</td>
            <td>{{ ap.Indoor_Outdoor | default: "" }}</td>
            <td>{{ ap.Generation | default: "" }}</td>
            <td>{{ ap.Product_Positioning | default: "" }}</td>
            <td>{{ ap.Total_PHY_Serving_Radios | default: "" }}</td>
            <td>{{ ap.Concurrent_Serving_Radios | default: "" }}</td>
            <td>{{ ap.Serving_Radio_1 | default: "" }}</td>
            <td>{{ ap.Serving_Radio_2 | default: "" }}</td>
            <td>{{ ap.Serving_Radio_3 | default: "" }}</td>
            <td>{{ ap.Serving_Radio_4 | default: "" }}</td>
            <td>{{ ap.Dedicated_Scanning_Radio | default: "" }}</td>
            <td>{{ ap.PoE_Class | default: "" }}</td>
            <td>{{ ap.Max_PoE_Consumption_W | default: "" }}</td>
            <td>{{ ap.Limited_Capabilities_PoE_bt_Class5_45W | default: "" }}</td>
            <td>{{ ap.Limited_Capabilities_PoE_at_30W | default: "" }}</td>
            <td>{{ ap.Limited_Capabilities_PoE_af_15W | default: "" }}</td>
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
            <td>{{ ap.Minimum_Software_Version | default: "" }}</td>
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
    // Default to compact mode
    document.body.classList.add('compact-mode');
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
            {
                extend: 'colvis',
                columns: ':not(.noVis)',
                text: 'Column visibility'
            },
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
            },
            {
                text: 'Compact/Roomy',
                className: 'dt-compact-toggle',
                action: function(e, dt, node, config){
                    document.body.classList.toggle('compact-mode');
                    if(typeof window.updateStickyOffsets === 'function') window.updateStickyOffsets();
                    if(typeof window.updateStickyHeaderHeight === 'function') window.updateStickyHeaderHeight();
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
            search: "Search all:",
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

    // Sticky header height calculation (header + its padding)
    function updateStickyHeaderHeight(){
        var headerRow = document.querySelector('#ap-table thead tr:not(.filter-row)');
        if(headerRow){
            var h = headerRow.getBoundingClientRect().height;
            if(h && h>0){
                document.documentElement.style.setProperty('--sticky-header-height', h + 'px');
            }
        }
    }
    updateStickyHeaderHeight();
    // Scroll listener to adjust header appearance
    var container = document.getElementById('ap-table-container');
    function handleScroll(){
        var thead = document.querySelector('#ap-table thead');
        if(!thead) return;
        if(container.scrollTop > 10){
            thead.classList.add('scrolled');
        } else {
            thead.classList.remove('scrolled');
        }
    }
    container.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
    $(window).on('resize', updateStickyHeaderHeight);
    table.on('draw.dt', function(){ updateStickyHeaderHeight(); });
    window.updateStickyHeaderHeight = updateStickyHeaderHeight;

        // Move the global search directly after the Compact/Roomy button
        var $wrapper = $('#ap-table').closest('.dataTables_wrapper');
        var $buttons = $wrapper.find('.dt-buttons');
        var $filter = $wrapper.find('div.dataTables_filter');
        var $compactBtn = $buttons.find('.dt-compact-toggle');
        if($buttons.length && $filter.length && $compactBtn.length){
            var $input = $filter.find('input');
            // Preserve existing DataTables bindings; just relocate the input
            $input.attr('placeholder','Search all...');
            var $inline = $('<span class="dt-inline-search" />').append($input);
            $inline.insertAfter($compactBtn);
            // Remove original filter wrapper (label + container)
            $filter.remove();
        }
    // Sticky columns offset calculation
    function updateStickyOffsets(){
        var firstDataCell = document.querySelector('#ap-table tbody tr:not(.width-probe) td.sticky-col-1');
        var headerCell = document.querySelector('#ap-table thead tr:not(.filter-row) th.sticky-col-1');
        var source = firstDataCell || headerCell;
        if(source){
            var w = source.getBoundingClientRect().width;
            if(w && w > 0){
                document.documentElement.style.setProperty('--sticky-col-1-width', w + 'px');
            }
        }
    }
    // Initial and event-based recalculations
    updateStickyOffsets();
    table.on('draw.dt column-visibility.dt', function(){
        updateStickyOffsets();
    });
    $(window).on('resize', function(){
        updateStickyOffsets();
    });

    // Expose for font resize function
    window.updateStickyOffsets = updateStickyOffsets;

});

// Font size controls
var minFont = 9, maxFont = 20;
function changeFontSize(delta) {
    var root = document.documentElement;
    var current = parseFloat(getComputedStyle(root).getPropertyValue('--table-font-size') || getComputedStyle(document.body).fontSize);
    var newSize = Math.max(minFont, Math.min(maxFont, current + delta));
    root.style.setProperty('--table-font-size', newSize + 'px');
    // Inputs/selects inherit; adjust if necessary
    var controls = document.querySelectorAll('.dataTables_wrapper .dataTables_filter input, .dataTables_wrapper .dataTables_length select');
    controls.forEach(function(el) { el.style.fontSize = newSize + 'px'; });
    // Force DataTables to recalculate column widths
    if ($.fn.dataTable) {
        var dt = $('#ap-table').DataTable();
        dt.columns.adjust().draw(false);
        if(typeof window.updateStickyOffsets === 'function') {
            window.updateStickyOffsets();
        }
        if(typeof window.updateStickyHeaderHeight === 'function') {
            window.updateStickyHeaderHeight();
        }
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
