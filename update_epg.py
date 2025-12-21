import requests
import re

urls = [
    "https://epg.pw/api/epg.xml?channel_id=464857",
    "https://epg.pw/api/epg.xml?channel_id=465087",
    "https://epg.pw/api/epg.xml?channel_id=464902",
    "https://epg.pw/api/epg.xml?channel_id=464849",
    "https://epg.pw/api/epg.xml?channel_id=465150",
    "https://epg.pw/api/epg.xml?channel_id=470185",
    "https://epg.pw/api/epg.xml?channel_id=467679",
    "https://epg.pw/api/epg.xml?channel_id=464941",
    "https://epg.pw/api/epg.xml?channel_id=464937",
    "https://epg.pw/api/epg.xml?channel_id=469378",
    "https://epg.pw/api/epg.xml?channel_id=468311",
    "https://epg.pw/api/epg.xml?channel_id=465059",
    "https://epg.pw/api/epg.xml?channel_id=467015",
    "https://epg.pw/api/epg.xml?channel_id=465291",
    "https://epg.pw/api/epg.xml?channel_id=466524",
    "https://epg.pw/api/epg.xml?channel_id=465355",
    "https://epg.pw/api/epg.xml?channel_id=469143",
    "https://epg.pw/api/epg.xml?channel_id=465006",
    "https://epg.pw/api/epg.xml?channel_id=486317",
    "https://epg.pw/api/epg.xml?channel_id=464920",
    "https://epg.pw/api/epg.xml?channel_id=464754",
    "https://epg.pw/api/epg.xml?channel_id=465366",
    "https://epg.pw/api/epg.xml?channel_id=413152",
    "https://epg.pw/api/epg.xml?channel_id=464783",
    "https://epg.pw/api/epg.xml?channel_id=463924",
    "https://epg.pw/api/epg.xml?channel_id=463820",
    "https://epg.pw/api/epg.xml?channel_id=464048",
    "https://epg.pw/api/epg.xml?channel_id=464301",
    "https://epg.pw/api/epg.xml?channel_id=464249",
    "https://epg.pw/api/epg.xml?channel_id=464163",
    "https://epg.pw/api/epg.xml?channel_id=76740",
    "https://epg.pw/api/epg.xml?channel_id=422089",
    "https://epg.pw/api/epg.xml?channel_id=6379",
    "https://epg.pw/api/epg.xml?channel_id=5926",
    "https://epg.pw/api/epg.xml?channel_id=6003",
    "https://epg.pw/api/epg.xml?channel_id=7835",
    "https://epg.pw/api/epg.xml?channel_id=7221",
    "https://epg.pw/api/epg.xml?channel_id=7136",
    "https://epg.pw/api/epg.xml?channel_id=7135",
    "https://epg.pw/api/epg.xml?channel_id=408447",
    "https://epg.pw/api/epg.xml?channel_id=449590",
    "https://epg.pw/api/epg.xml?channel_id=449589",
    "https://epg.pw/api/epg.xml?channel_id=452290"
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
