import requests
import re

urls = [
    "https://epg.pw/api/epg.xml?channel_id=464857",
    "https://epg.pw/api/epg.xml?channel_id=465087"
]

# Nagłówek i otwarcie tagu tv
combined = '<?xml version="1.0" encoding="UTF-8"?>\n<tv>'

for url in urls:
    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            # Wyciągamy tylko to, co jest MIĘDZY <tv...> a </tv>
            data = r.text
            content = re.search(r'<tv[^>]*>(.*)</tv>', data, re.DOTALL)
            if content:
                combined += content.group(1)
    except Exception as e:
        print(f"Błąd przy {url}: {e}")

# Zamknięcie tagu tv
combined += "</tv>"

with open("combined_epg.xml", "w", encoding="utf-8") as f:
    f.write(combined)
