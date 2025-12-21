import requests

# The two sources you want to combine
urls = [
    "https://epg.pw/api/epg.xml?channel_id=464857",
    "https://epg.pw/api/epg.xml?channel_id=465087"
]

combined_content = '<?xml version="1.0" encoding="UTF-8"?>\n<tv>'

for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Remove the XML header and <tv> tags from individual files
            content = response.text
            content = content.split('<tv')[1].split('>', 1)[1]
            content = content.rsplit('</tv>', 1)[0]
            combined_content += content
    except Exception as e:
        print(f"Error downloading {url}: {e}")

combined_content += '</tv>'

with open("combined_epg.xml", "w", encoding="utf-8") as f:
    f.write(combined_content)
