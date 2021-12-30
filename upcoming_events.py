import re
import requests

link = 'https://www.python.org'
upcoming_events_pattern = r'<a href="/events/.+/\d+/">(.+)</a></li>'

python_org_html = requests.get(link)
upcoming_events = re.findall(upcoming_events_pattern, python_org_html.text)
print(upcoming_events)