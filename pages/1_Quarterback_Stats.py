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
    qb_file = 'https://github.com/chale15/NFL_Data/blob/f8b21ec34657411944467c0f4ddc058518e76d46/qb_data.csv'
    df = pd.read_csv(qb_file)
    return df

def get_name():
    val = get_random_name(data)

data = load_qb_data()


st.markdown("# Quarterback Stats")
st.sidebar.header("Quarterback Stats")
st.markdown('*Explore league trends, stat leaders, and player comparisons for NFL quarterbacks!*')
st.write('')

#if 'input_name' not in st.session_state:
    #st.session_state.input_name = ""

#with st.sidebar:
    #input_name = st.text_input('Enter a name:', value=st.session_state.input_name)
        
    #if st.button("Random Name"):
        #random_name = get_random_name(data)
        #st.session_state.input_name = random_name
        #st.rerun()



#chart_placeholder = st.empty()

#try:
    #stats = name_trend_stats(data, input_name)
    #if len(stats)==0:
        #st.write(f"No Occurrances of the Name {input_name} Found")
    #else:
        #st.write(f"First Recorded Occurrance of Name: {stats[0]}")
        #st.write(f"Peak Popularity: {stats[2]}  ({stats[1]})")

    #fig = name_trend_line(data, input_name)
    #with chart_placeholder.container():
        #st.plotly_chart(fig)

#except:
    #None
