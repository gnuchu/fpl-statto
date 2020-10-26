import requests
from datetime import datetime, timedelta
import json

def icaldt(dt):
  return dt.strftime('%Y%m%dT%H%M%S')

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
response_json = r.json()
json_text = json.dumps(response_json)

vinfo = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
"""
counter = 1

for event in response_json['events']:
  uid = f"uid{counter}@gnuchu.com"
  counter += 1

  date = datetime.strptime(event['deadline_time'], "%Y-%m-%dT%H:%M:%SZ")
  end_date = date + timedelta(hours=2)

  vinfo += "BEGIN:VEVENT\n"
  vinfo += f"UID: {uid}\n"
  vinfo += "DTSTAMP:" + icaldt(date) + "\n"
  vinfo += "DTSTART:" + icaldt(date) + "\n"
  vinfo += "DTEND:" + icaldt(end_date) + "\n"

  description = f"Gameweek {event['id']} deadline\n"
  vinfo += f"SUMMARY: {description}"
  vinfo += "END:VEVENT\n"

vinfo += "END:VCALENDAR"

with open('./deadlines.ics', "w") as f:
  f.write(vinfo)