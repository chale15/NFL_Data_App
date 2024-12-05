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

st.set_page_config(page_title="Home")

@st.cache_data
def load_name_data():
    names_file = 'https://www.ssa.gov/oact/babynames/names.zip'
    response = requests.get(names_file)
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        dfs = []
        files = [file for file in z.namelist() if file.endswith('.txt')]
        for file in files:
            with z.open(file) as f:
                df = pd.read_csv(f, header=None)
                df.columns = ['name','sex','count']
                df['year'] = int(file[3:7])
                dfs.append(df)
        data = pd.concat(dfs, ignore_index=True)
    data['pct'] = data['count'] / data.groupby(['year', 'sex'])['count'].transform('sum')
    return data

@st.cache_data
def ohw(df):
    nunique_year = df.groupby(['name', 'sex'])['year'].nunique()
    one_hit_wonders = nunique_year[nunique_year == 1].index
    one_hit_wonder_data = df.set_index(['name', 'sex']).loc[one_hit_wonders].reset_index()
    return one_hit_wonder_data

data = load_name_data()
ohw_data = ohw(data)


st.title('NFL Player Statistics App')

st.markdown('### Select a page from the menu to start exploring!')
st.text('')
st.markdown('*For more information about individual widgets, see below*')
st.text('')
st.text('')


tab1, tab2, tab3 = st.tabs(['Quarterback Stats', 'Reciever Stats', 'Team Stats'])
with tab1:
    col11, col12 = st.columns([1,1])
    with col11:
        st.text('')
        st.write('This widget allows the user to view Quarterback statistics. Options include league trends, individual season stat leaders, and individual player comparisons')
        #st.write('Hovering over the plot will display more detailed information, and stats such as the name\'s first usage, peak popularity, and highest rank are displayed below the plot')
    with col12:
        st.text('')
        st.image('img/names_over_time.png')

with tab2:
    col21, col22 = st.columns([1,1])
    with col21:
        st.text('')
        st.write('This widget allows the user to view Reciever statistics. Options include league trends, individual season stat leaders, and individual player comparisons')
        #st.write('Hovering over the plot will display more detailed information, and the number of unique names given that year for males and females are displayed below the plot')
    with col22:
        st.text('')
        st.image('img/top_by_year.png')


with tab3:
    col31, col32 = st.columns([1,1])
    with col31:
        st.text('')
        st.write('This widget allows the user to view statistics for a selected team. Options include passing and recieving leaders, team statistics over time, and general trends')
        #st.write('Hovering over the plot will display more detailed information, such as the name, year, and number of babies born with that name.')
    with col32:
        st.text('')
        st.image('img/name_comp.png')











