import re
import requests
import sys

link = 'https://www.python.org'
upcoming_events_pattern = r'<a href="/events/.+/\d+/">(.+)</a></li>'

python_org_html = requests.get(link)
upcoming_events = re.findall(upcoming_events_pattern, python_org_html.text)
stdout_file = sys.stdout
for event in upcoming_events:
    stdout_file.write(event + '\n')
