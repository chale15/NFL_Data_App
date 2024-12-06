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

st.set_page_config(page_title="Reciever Stats")

@st.cache_data
def load_wr_data():
    data = pd.read_csv('wr_full.csv', index_col=0)
    data = data.dropna()
    return data

data = load_wr_data()

stats = {'Receptions':'Receptions', 'Recieving Yards':'REC_YDS', 'Recieving Touchdowns':'REC_TDS', 'Recieving Yards After Catch':'REC_YAC', 'Targets':'Targets'}


st.markdown("# Reciever Stats")
st.markdown('*Explore league trends, stat leaders, and player comparisons for NFL recievers!*')
st.write('')

tab1, tab2, tab3 = st.tabs(['League Trends', 'Stat Leaders', 'Player Comparisons'])
with tab1:
    chart_placeholder4 = st.empty()

    
    with st.sidebar:
        st.subheader('League Trends', divider = 'blue')
        stat = st.selectbox('Choose a stat', 
                        ('Receptions', 'Recieving Yards', 'Recieving Touchdowns','Recieving Yards After Catch', 'Targets'),
                        index= None, placeholder = 'Choose an Option', key = 'sldkfj')

    if stat:
        stat12 = stats[stat]   
        fig = plot_wr_features_over_time(data, [stat12])

    with chart_placeholder4.container():
        if stat:
            st.markdown(f"<h3 style='text-align: center;'>{stat} over Time</h3>", unsafe_allow_html=True)
            st.pyplot(fig)
        else: 
            st.write('')


with tab2:
    chart_placeholder5 = st.empty()

    with st.sidebar:
        st.subheader('Stat Leaders', divider = 'blue')
        stat13 = st.selectbox('Choose a stat', 
                            ('Receptions', 'Recieving Yards', 'Recieving Touchdowns','Recieving Yards After Catch', 'Targets'),
                            index= None, placeholder = 'Choose an Option', key = 'sdafjkk')
    
        year10 = st.pills('Select Season(s):',['2021','2022','2023','2024'], selection_mode='multi', key = 'slkdfj')

        n_names10 = st.number_input('Number of Players to Display', value = 10, key = 'lsdkfjslkdjf')

    
    if stat13:
        stat14 = stats[stat13]
        if year10:
            fig2 = plot_wr_leaders(data, feature= stat13, seasons=year10, top_n=n_names10)
            with chart_placeholder5.container():
                st.plotly_chart(fig2, use_container_width = True)

    


with tab3:
    chart_placeholder6 = st.empty()

    with st.sidebar:
        st.subheader('Player Comparisons', divider = 'blue')

        player_names = data['Reciever'].unique()

        player3 = st.selectbox('First Player to Compare:', player_names, placeholder = 'Choose a Player', index=None)
        player4 = st.selectbox('Second Player to Compare:', player_names, placeholder = 'Choose a Player', index=None)

        stat5 = st.selectbox('Choose a stat', 
                            ('Receptions', 'Recieving Yards', 'Recieving Touchdowns','Recieving Yards After Catch', 'Targets'),
                            index= None, placeholder = 'Choose an Option', key = 'wiefodjslfj')
    
        year2 = st.pills('Select Season(s):',['2021','2022','2023','2024'], selection_mode='multi', key = 'slioepfsjd')
        for year in year2:
            year = int(year)


    if stat5:
        stat6 = stats[stat5]
        if year2:
            if player3: 
                if player4:
                    fig3 = plot_wr_comp(data, stat5,year2, [player3,player4])
                    with chart_placeholder6.container():
                        st.plotly_chart(plot_wr_comp(data, stat5,year2, [player3,player4]))



