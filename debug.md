---
layout: default
title: Debug Test
---

# Debug Test

## Test 1: Raw Data Access
Total items: {{ site.data.ap_models | size }}

## Test 2: First Item
{% if site.data.ap_models[0] %}
First item manufacturer: {{ site.data.ap_models[0].Manufacturer }}
First item model: {{ site.data.ap_models[0].Model }}
{% else %}
No data found
{% endif %}

## Test 3: Loop Test (first 3)
{% for ap in site.data.ap_models limit:3 %}
- {{ ap.Manufacturer }} {{ ap.Model }}
{% endfor %}

## Test 4: Data Structure Debug
{% if site.data.ap_models[0] %}
{% assign first_ap = site.data.ap_models[0] %}
{% for item in first_ap %}
- {{ item[0] }}: {{ item[1] }}
{% endfor %}
{% endif %}