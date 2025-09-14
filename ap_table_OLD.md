---
layout: default
title: Wi-Fi Access Points Specifications
---

<h1>Wi-Fi Access Points Specifications</h1>
<p>Filter, search, and explore AP models. Add new models by editing the YAML data file.</p>

<!-- DataTable CSS -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">

<div id="ap-table-container">
<table id="ap-table" class="display" style="width:100%">
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
            <td>{{ col[1] }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </tbody>
</table>
</div>

<!-- jQuery and DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    // Use DataTables default (autoWidth: false) and set table-layout: fixed for alignment
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
        scrollX: true
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

<!-- DataTables Buttons extension for column visibility -->
<link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.4.1/css/buttons.dataTables.min.css">
<script src="https://cdn.datatables.net/buttons/2.4.1/js/dataTables.buttons.min.js"></script>
<script src="https://cdn.datatables.net/buttons/2.4.1/js/buttons.colVis.min.js"></script>

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
</style>
