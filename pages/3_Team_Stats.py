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

st.set_page_config(page_title="Team Stats")

@st.cache_data
def load_wr_data():
    data_file = 'https://github.com/chale15/NFL_Data/blob/f8b21ec34657411944467c0f4ddc058518e76d46/wr_full.csv'
    df = pd.read_csv(data_file)
    return df


def get_name():
    val = get_random_name(data)

data = load_wr_data()


st.markdown("# Team Stats")
st.sidebar.header("Team Stats")
st.markdown('*Pick your favorite team to explore trends!*')
st.write('')

#if 'input_name1' not in st.session_state:
    #st.session_state.input_name1 = ""

#if 'input_name2' not in st.session_state:
    #st.session_state.input_name2 = ""

#with st.sidebar:
    #input_name1 = st.text_input('Enter Name 1:', value=st.session_state.input_name1)
    #input_name2 = st.text_input('Enter Name 2:', value=st.session_state.input_name2)

#if len(input_name1) > 0:

    #chart_placeholder = st.empty()

#try:
    #fig = names_trend_line(data, [input_name1, input_name2])
    #with chart_placeholder.container():
        #st.plotly_chart(fig)

#except:
    #None
