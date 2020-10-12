import pandas as pd
import numpy as np
import requests
from datetime import datetime
import json

def create_li_item(title, active, sort_item):
  tab_id = title.lower() + sort_item.lower()
  html = f'''
<li class="nav-item">
    <a href="#{tab_id}" class="nav-link {active}" data-toggle="tab">{title}</a>
</li>
'''
  return html

def create_tab_content(title, content, active, sort_item):
  tab_id = title.lower() + sort_item.lower()
  html = f'''
<div class="tab-pane fade show {active}" id="{tab_id}">
    <p>
      {content}
    </p>
</div>
'''
  return html

def read_file(path):
  data = ''
  with open(path) as f:
    data = f.read()
  
  return data

def write_file(path, content):
  f = open(path, "w")
  f.write(content)
  f.close


def process_dataframe(df, title):
  html = ''
  for index, row in df.iterrows():
    html += "<tr>"
    html += "<td>" + str(row['first_name']) + " " + str(row['second_name'])   + "</td>"
    html += "<td>" + str(row['team'])          + "</td>"
    #html += "<td>" + str(row['element_type'])  + "</td>"
    html += "<td>" + str(row['now_cost']/10)      + "</td>"
    html += "<td>" + str(row['value'])         + "</td>"
    html += "<td>" + str(row['total_points'])  + "</td>"
    html += "<td>" + str(row['points_per_game'])  + "</td>"
    html += "<td>" + str(row['minutes'])  + "</td>"
    html += "<td>" + str(row['selected_by_percent'])  + "%</td>"

    html += "</tr>"
  
  return html

def date_str():
  return datetime.now().strftime('%A %d %B %Y %H:%M:%S')

def date_line():
  html = "<small>Page generated: " + date_str() + "</small>"
  html += '<hr/>'
  return html

def table_maker(dataframe, title, sort_item):
  table_name = sort_item.lower() + "_table"
  html = f"<h4>{title}</h4><br/>" 
  html += table_head(table_name)
  html += process_dataframe(dataframe, title)
  html += table_foot()
  return html

def table_head(table_name):
  table = read_file('templates/thead.html')
  table = table.replace('table_name_place_holder', table_name)
  return table
  
def table_foot():
  return read_file('templates/tend.html')

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
response_json = r.json()
json_text = json.dumps(response_json)

write_file("raw-data/stats.json", json_text)

elements_df = pd.DataFrame(response_json['elements'])
elements_types_df = pd.DataFrame(response_json['element_types'])
teams_df = pd.DataFrame(response_json['teams'])

elements_df['team'] = elements_df.team.map(teams_df.set_index('id').name)
elements_df['value'] = elements_df.value_season.astype(float)
elements_df['position'] = elements_df.element_type.map(elements_types_df.set_index('id').plural_name_short)

positions = {
  'GKP': 'Goalkeeper', 
  'DEF': 'Defender', 
  'MID': 'Midfielder', 
  'FWD': 'Forward'
}

html = read_file('templates/page_start.html')
html += date_line()

#upper tabs
upper_tabs_template = read_file('templates/upper_tabs.html')
sort_items = ['value', 'total_points', 'points_per_game']

for sort_item in sort_items:

  replacement_tag = f"by_{sort_item}_content_place_holder"

  #lower tabs
  tabs_html = "<ul class='nav nav-tabs'>"

  for pos_short, pos_long in positions.items():
    active = "active" if (pos_short == 'GKP') else ""
    tabs_html += create_li_item(pos_long, active, sort_item)

  tabs_html += "</ul>"
  tabs_html += "<div class='tab-content'>"

  for pos_short, pos_long in positions.items():
    slim_dataframe = elements_df.loc[elements_df.position == pos_short]
    top5 = slim_dataframe.sort_values(sort_item, ascending=False).head(10)

    content = table_maker(top5, pos_long, sort_item)
    active = "active" if (pos_short == 'GKP') else ""
    tabs_html += create_tab_content(pos_long, content, active, sort_item)

  tabs_html += "</div>"
  upper_tabs_template = upper_tabs_template.replace(replacement_tag, tabs_html)

html += upper_tabs_template
html += read_file('templates/page_end.html')

write_file("index.php", html)