import pandas as pd
import numpy as np
import requests

def read_file(path):
  data = ''
  with open(path) as f:
    data = f.read()
  
  return data


def process_dataframe(df, title):
  html = ''
  #html += f"<tr><td colspan='6'><strong>{title}</strong></td></tr>"
  for index, row in df.iterrows():
    html += "<tr>"
    html += "<td>" + str(row['second_name'])   + "</td>"
    html += "<td>" + str(row['team'])          + "</td>"
    html += "<td>" + str(row['element_type'])  + "</td>"
    html += "<td>" + str(row['now_cost'])      + "</td>"
    html += "<td>" + str(row['value'])         + "</td>"
    html += "<td>" + str(row['total_points'])  + "</td>"
    html += "</tr>"
  
  return html

def table_maker(dataframe, title):
  html = f"<h2>{title}</h2><br/>" 
  html += table_head()
  html += process_dataframe(dataframe, title)
  html += table_foot()
  return html


def table_head():
  return read_file('templates/thead.html')
  
def table_foot():
  return read_file('templates/tend.html')


url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json = r.json()

elements_df = pd.DataFrame(json['elements'])
elements_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])

slim_elements_df = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
slim_elements_df['element_type'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').plural_name_short)
slim_elements_df.rename(index={0: "id"})

goal_df = slim_elements_df.loc[slim_elements_df.element_type == 'GKP']
def_df = slim_elements_df.loc[slim_elements_df.element_type == 'DEF']
mid_df = slim_elements_df.loc[slim_elements_df.element_type == 'MID']
fwd_df = slim_elements_df.loc[slim_elements_df.element_type == 'FWD']

top_5_gk = goal_df.sort_values('value',ascending=False).head(10)
top_5_def = def_df.sort_values('value',ascending=False).head(10)
top_5_mid = mid_df.sort_values('value',ascending=False).head(10)
top_5_fwd = fwd_df.sort_values('value',ascending=False).head(10)

top_5_gk.to_csv('csv/gk.csv')
top_5_def.to_csv('csv/def.csv')
top_5_mid.to_csv('csv/mid.csv')
top_5_fwd.to_csv('csv/fwd.csv')

html = read_file('templates/page_start.html')

html += table_maker(top_5_gk, 'Goalkeepers')
html += table_maker(top_5_def, 'Defenders')
html += table_maker(top_5_mid, 'Midfielders')
html += table_maker(top_5_fwd, 'Forwards')

html += read_file('templates/page_end.html')

f = open("index.php", "w")
f.write(html)
f.close
