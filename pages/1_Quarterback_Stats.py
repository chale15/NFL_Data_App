import numpy as np
import pandas as pd
import zipfile
import plotly.express as px
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from my_plots import *
import streamlit as st

st.set_page_config(page_title="Quarterback Stats")

@st.cache_data
def load_qb_data():
    data = pd.read_csv('qb_data.csv', index_col=0)
    data = data[data['YDS'] > 10]
    data = data[data['ATT'] > 3]
    data['CMPP'] = data['CMP']/data['ATT']
    data = data.fillna(0)
    return data

data = load_qb_data()

stats = {'Passing Yards':'YDS', 'Passing Attempts':'ATT', 'Yards per Attempt':'YPA','Completion Percentage':'CMPP', 'Passing Touchdowns':'TDs','Interceptions':'INTs', 'Quarterback Rating':'QBR', 'Sacks':'SCK','Rushing Attempts':'ATT(R)','Rushing Yards':'YDS(R)', 'Yards per Carry':'YPC', 'Rushing Touchdowns':'TDs(R)'}

st.markdown("# Quarterback Stats")
st.markdown('*Explore league trends, stat leaders, and player comparisons for NFL quarterbacks!*')
st.write('')

tab1, tab2, tab3 = st.tabs(['League Trends', 'Stat Leaders', 'Player Comparisons'])
with tab1:
    chart_placeholder = st.empty()

    
    with st.sidebar:
        st.subheader('League Trends', divider = 'blue')
        stat = st.selectbox('Choose a stat', 
                        ('Passing Yards', 'Passing Attempts', 'Yards per Attempt','Completion Percentage', 'Passing Touchdowns','Interceptions', 'Quarterback Rating', 'Sacks','Rushing Attempts','Rushing Yards', 'Yards per Carry', 'Rushing Touchdowns'),
                        index= None, placeholder = 'Choose an Option')

    if stat:
        stat2 = stats[stat]   
        fig = plot_qb_features_over_time(data, [stat2])

    with chart_placeholder.container():
        if stat:
            st.markdown(f"<h3 style='text-align: center;'>{stat} over Time</h3>", unsafe_allow_html=True)
            st.pyplot(fig)
        else: 
            st.write('')


with tab2:
    with st.sidebar:
        st.subheader('Stat Leaders', divider = 'blue')
        stat3 = st.selectbox('Choose a stat:', 
                            ('Passing Yards', 'Passing Attempts', 'Yards per Attempt','Completion Percentage', 'Passing Touchdowns','Interceptions', 'Quarterback Rating', 'Sacks','Rushing Attempts','Rushing Yards', 'Yards per Carry', 'Rushing Touchdowns'),
                            placeholder = 'Choose an Option', index=None)
    
        year = st.pills('Select Season(s):',['2020','2021','2022','2023','2024'], selection_mode='multi', key = 'slkdfj')

        n_names = st.number_input('Number of Players to Display', value = 10)

    chart_placeholder2 = st.empty()
    if stat3:
        stat4 = stats[stat3]
        if year:
            fig2 = plot_qb_leaders(data, stat3, year, n_names)
            with chart_placeholder2.container():
                st.plotly_chart(fig2)

    


with tab3:
    with st.sidebar:
        st.subheader('Player Comparisons', divider = 'blue')

        player_names = data['QB'].unique()

        player1 = st.selectbox('First Player to Compare:', player_names, placeholder = 'Choose a Player', index=None)
        player2 = st.selectbox('Second Player to Compare:', player_names, placeholder = 'Choose a Player', index=None)

        stat5 = st.selectbox('Stat to Compare:', 
                            ('Passing Yards', 'Passing Attempts', 'Yards per Attempt','Completion Percentage', 'Passing Touchdowns','Interceptions', 'Quarterback Rating', 'Sacks','Rushing Attempts','Rushing Yards', 'Yards per Carry', 'Rushing Touchdowns'),
                            placeholder = 'Choose an Option', index=None)
    
        year2 = st.pills('Select Season(s):',['2020','2021','2022','2023','2024'], selection_mode='multi')

    chart_placeholder3 = st.empty()

    if stat5:
        stat6 = stats[stat5]
        if year2:
            if player1: 
                if player2:
                    fig3 = plot_qb_comp(data, stat5,year2, [player1,player2])
                    with chart_placeholder3.container():
                        st.plotly_chart(fig3)


