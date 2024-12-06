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

df = load_wr_data()

def random_year():
    year_input = get_random_year(data)

#year_val = 2000

st.markdown("# Reciever Stats")
st.sidebar.header("Reciever Stats")
st.markdown('*Explore league trends, stat leaders, and player comparisons for NFL recievers!*')
st.write('')
#with st.sidebar:
    #slider_placeholder = st.empty()

    #if st.button("Random Year"):
        #year_val = get_random_year(data)

    #n_names = st.number_input('Number of Names to Display (per sex)', value = 5)


#chart_placeholder = st.empty()


#with slider_placeholder.container():
    #year_input = st.slider('Year', min_value = 1880, max_value = 2023, value=year_val)


#fig2 = top_names_plot(data, year=year_input, n=n_names)


#with chart_placeholder.container():
    #st.plotly_chart(fig2)

#unique_male = len(data[(data['year']==year_input) & (data['sex']=='M')]['name'].unique())
#unique_female = len(data[(data['year']==year_input) & (data['sex']=='F')]['name'].unique())

#st.write(f"Number of Unique Male Names: {unique_male}")
#st.write(f"Number of Unique Female Names: {unique_female}")
