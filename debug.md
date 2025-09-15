---
layout: default
title: Debug Test
---

# Debug Test

## 🕒 Build Information
**Page Last Built:** {{ site.time | date: "%Y-%m-%d %H:%M:%S %Z" }}  
**Jekyll Version:** {{ jekyll.version }}  
**GitHub Pages Build:** {{ site.github.build_revision | truncate: 8, "" }}

---

## Test 1: Raw Data Access

Total items: {{ site.data.ap_models | size }}

## Test 2: Database Statistics

{% assign total_aps = site.data.ap_models | size %}
{% assign manufacturers = site.data.ap_models | map: "Manufacturer" | uniq | sort %}
{% assign generations = site.data.ap_models | map: "Generation" | uniq | sort %}

**Database Summary:**
- Total Access Points: {{ total_aps }}
- Manufacturers: {{ manufacturers | size }} ({{ manufacturers | join: ", " }})
- Wi-Fi Generations: {{ generations | size }} ({{ generations | join: ", " }})
- Data File: `_data/ap_models.yaml`

## Test 3: First Item
{% if site.data.ap_models[0] %}
First item manufacturer: {{ site.data.ap_models[0].Manufacturer }}
First item model: {{ site.data.ap_models[0].Model }}
{% else %}
No data found
{% endif %}

## Test 4: Loop Test (first 3)
{% for ap in site.data.ap_models limit:3 %}
- {{ ap.Manufacturer }} {{ ap.Model }}
{% endfor %}

## Test 5: Data Structure Debug
{% if site.data.ap_models[0] %}
{% assign first_ap = site.data.ap_models[0] %}
{% for item in first_ap %}
- {{ item[0] }}: {{ item[1] }}
{% endfor %}
{% endif %}