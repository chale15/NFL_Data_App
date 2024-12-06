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


st.title('NFL Player Statistics App')

st.markdown('### Select a page from the menu to start exploring!')
st.text('')
st.markdown('*For more information about individual widgets, see below*')
st.text('')
st.text('')


#tab1, tab2, tab3 = st.tabs(['Quarterback Stats', 'Reciever Stats', 'Team Stats'])
tab1, tab2 = st.tabs(['Quarterback Stats', 'Reciever Stats'])

with tab1:
    col11, col12 = st.columns([1,1])
    with col11:
        st.text('')
        st.write('This widget allows the user to view Quarterback statistics. Options include league trends, individual season stat leaders, and individual player comparisons')
        #st.write('Hovering over the plot will display more detailed information, and stats such as the name\'s first usage, peak popularity, and highest rank are displayed below the plot')
    with col12:
        st.text('')
        st.image('img/qb.png')

with tab2:
    col21, col22 = st.columns([1,1])
    with col21:
        st.text('')
        st.write('This widget allows the user to view Reciever statistics. Options include league trends, individual season stat leaders, and individual player comparisons')
        #st.write('Hovering over the plot will display more detailed information, and the number of unique names given that year for males and females are displayed below the plot')
    with col22:
        st.text('')
        st.image('img/wr.png')


#with tab3:
#    col31, col32 = st.columns([1,1])
#   with col31:
#        st.text('')
#        st.write('This widget allows the user to view statistics for a selected team. Options include passing and recieving leaders, team statistics over time, and general trends')
#        #st.write('Hovering over the plot will display more detailed information, such as the name, year, and number of babies born with that name.')
#    with col32:
#        st.text('')
#        #st.image('img/name_comp.png')











