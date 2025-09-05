#Hey!! Rishi here, here we are importing all the neccessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from statsbombpy import sb
from mplsoccer import Pitch
import streamlit as st
import warnings

#pandas for data manuplation, matplotlab to visualise the heatmap
#statsbomb and mplsoccer to fetch the players info

import requests_cache
requests_cache.disabled = True

warnings.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)
st.set_page_config(page_title="Player Heatmap Generator", layout="wide")
st.title("Player Heatmap Generator (StatsBomb Open Data)")

#here we will fetch all the competition available, note that we ar on the free plan of statsbomb
#therefore free stats might get added or removed,so instead of making a selector, we create 
#a drop down using combined label (competition_name + season_name)

competitions = sb.competitions()
competitions_df = competitions[['competition_name', 'season_name', 'competition_id', 'season_id']]
competitions_df['label'] = competitions_df['competition_name'] + ' - ' + competitions_df['season_name']
competition_options = {row['label']: (row['competition_id'], row['season_id']) for i,row in competitions_df.iterrows()}
selected_comp_label = st.selectbox("Select Competition + Season", list(competition_options.keys()))
st.write("Selected competition:", selected_comp_label)

def get_matches_and_teams(selected_comp_label):
    competition_id, season_id = competition_options[selected_comp_label]
    matches = sb.matches(competition_id=competition_id, season_id=season_id)
    matches['home_team_name'] = matches['home_team'].apply(lambda x: x if isinstance(x,str) else x['home_team_name'])
    matches['away_team_name'] = matches['away_team'].apply(lambda x: x if isinstance(x,str) else x['away_team_name'])
    teams = pd.unique(matches[['home_team_name','away_team_name']].values.ravel())
    return matches, teams

matches, teams = get_matches_and_teams(selected_comp_label)
selected_team = st.selectbox("Select Team", teams)
st.write("Selected team:", selected_team)

# # user selection menu , this extracts the actuall x and y of player data from the selected tour

team_matches = matches[(matches['home_team_name']==selected_team) | (matches['away_team_name']==selected_team)]
combined_events = []
for match_id in team_matches['match_id']:
    events = sb.events(match_id=match_id)
    events['match_id'] = match_id
    combined_events.append(events)
df_events = pd.concat(combined_events, ignore_index=True)
players = df_events[df_events['team']==selected_team]['player'].dropna().unique()
selected_player = st.selectbox("Select Player", players)
st.write("Selected player:", selected_player)

#Heatmap creation using matplot and a football pitch using mplsoccer
df_player = df_events[(df_events['player']==selected_player) & (df_events['team']==selected_team)].copy()
df_player[['x','y']] = df_player['location'].apply(pd.Series)
df_player = df_player.dropna(subset=['x','y'])
pitch = Pitch(pitch_type='statsbomb', pitch_color='white', line_color='grey', line_zorder=2)
fig, ax = pitch.draw(figsize=(10,7))
pitch.kdeplot(df_player.x, df_player.y, fill=True, n_levels=100, cmap='Reds', thresh=0, ax=ax)
st.pyplot(fig)
st.write(f"Heatmap generated for {selected_player}")
