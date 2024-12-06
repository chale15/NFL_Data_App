import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd
import random


def plot_qb_features_over_time(df, features):
    df['Year'] = df['Year'].astype(int)

    df_grouped_med = df.groupby('Year')[features].median()
    df_grouped_max = df.groupby('Year')[features].max()
    df_grouped_mean = df.groupby('Year')[features].mean() 

    plt.figure(figsize=(10, 6))
    
    plt.plot(df_grouped_med.index, df_grouped_med[features], label=features)
    plt.plot(df_grouped_mean.index, df_grouped_mean[features], label=features)
    plt.plot(df_grouped_max.index, df_grouped_max[features], label=features)
    
    plt.title("")
    plt.xlabel("Season")
    plt.ylabel("Value")
    plt.legend(['Median','Mean','Max'])
    plt.grid(True)

    plt.xlim(df_grouped_med.index.min(), df_grouped_med.index.max())
    plt.xticks(df_grouped_med.index.unique())
    
    return plt

def plot_qb_leaders(df, feature, seasons, top_n=10, width=800, height=600):

    stats = {'Passing Yards':'YDS', 'Passing Attempts':'ATT', 'Yards per Attempt':'YPA','Completion Percentage':'CMPP', 'Passing Touchdowns':'TDs','Interceptions':'INTs', 'Quarterback Rating':'QBR', 'Sacks':'SCK','Rushing Attempts':'ATT(R)','Rushing Yards':'YDS(R)', 'Yards per Carry':'YPC', 'Rushing Touchdowns':'TDs(R)'}
    stats2 = dict(zip(stats.values(), stats.keys()))
    sum_list = ['GP','ATT(R)', 'YDS(R)', 'TDs(R)', 'YDS', 'ATT','TDs', 'INTs', 'SCK']
    feature = stats[feature]

    df_filtered = df[df['Year'].isin(seasons)]

    if feature in sum_list:
        df_grouped = df_filtered.groupby('QB')[feature].sum().reset_index()
    else:
        df_grouped = df_filtered.groupby('QB')[feature].mean().reset_index()

    df_top_n = df_grouped.sort_values(by=feature, ascending=False).head(top_n)

    fig = px.bar(df_top_n, 
                 x='QB', 
                 y=feature, 
                 title=f"Top {top_n} Quarterbacks by {stats2[feature]} ({', '.join(map(str, seasons))})", 
                 labels={feature: feature, 'QB': 'Player Name'}, 
                 )
    
    fig.update_layout(width=width, height=height)
    return fig

def plot_qb_comp(df, feature, years, qbs, width=800, height=600):

    stats = {'Passing Yards':'YDS', 'Passing Attempts':'ATT', 'Yards per Attempt':'YPA','Completion Percentage':'CMPP', 'Passing Touchdowns':'TDs','Interceptions':'INTs', 'Quarterback Rating':'QBR', 'Sacks':'SCK','Rushing Attempts':'ATT(R)','Rushing Yards':'YDS(R)', 'Yards per Carry':'YPC', 'Rushing Touchdowns':'TDs(R)'}
    stats2 = dict(zip(stats.values(), stats.keys()))
    sum_list = ['GP','ATT(R)', 'YDS(R)', 'TDs(R)', 'YDS', 'ATT','TDs', 'INTs', 'SCK']
    feature = stats[feature]

    df_filtered = df[(df['Year'].isin(years)) & (df['QB'].isin(qbs))]

    if feature in sum_list:
        df_grouped = df_filtered.groupby(['Year', 'QB'])[feature].sum().reset_index()
    else:
        df_grouped = df_filtered.groupby(['Year', 'QB'])[feature].mean().reset_index()

    fig = px.bar(df_grouped, 
                 x='Year', 
                 y=feature, 
                 color='QB', 
                 barmode='group', 
                 title=f"Comparison of {stats2[feature]} for {qbs[0]} and {qbs[1]}",
                 labels={feature: feature, 'QB': 'Player Name', 'Year': 'Season'},
                 color_discrete_map={qbs[0]: 'blue', qbs[1]: 'lightblue'})

    fig.update_layout(width=width, height=height)

    return fig

def plot_wr_features_over_time(df, features):
    df['Year'] = df['Year'].astype(int)

    df_grouped_med = df.groupby('Year')[features].median()
    df_grouped_max = df.groupby('Year')[features].max()
    df_grouped_mean = df.groupby('Year')[features].mean() 

    plt.figure(figsize=(10, 6))
    
    plt.plot(df_grouped_med.index, df_grouped_med[features], label=features)
    plt.plot(df_grouped_mean.index, df_grouped_mean[features], label=features)
    plt.plot(df_grouped_max.index, df_grouped_max[features], label=features)
    
    plt.title("")
    plt.xlabel("Season")
    plt.ylabel("Value")
    plt.legend(['Median','Mean','Max'])
    plt.grid(True)

    plt.xlim(df_grouped_med.index.min(), df_grouped_med.index.max())
    plt.xticks(df_grouped_med.index.unique())
    
    return plt

def plot_wr_leaders(df, feature, seasons, top_n=10, width=800, height=600):

    stats = {'Receptions':'Receptions', 'Recieving Yards':'REC_YDS', 'Recieving Touchdowns':'REC_TDS', 'Recieving Yards After Catch':'REC_YAC', 'Targets':'Targets'}
    stats2 = dict(zip(stats.values(), stats.keys()))
    feature = stats[feature]

    df_filtered = df[df['Year'].isin(seasons)]

    df_grouped = df_filtered.groupby('Reciever')[feature].sum().reset_index()
    
    df_top_n = df_grouped.sort_values(by=feature, ascending=False).head(top_n)

    fig = px.bar(df_top_n, 
                 x='Reciever', 
                 y=feature, 
                 title=f"Top {top_n} Recievers by {stats2[feature]} ({', '.join(map(str, seasons))})", 
                 labels={feature: feature, 'Reciever': 'Player Name'}, 
                 )
    
    fig.update_layout(width=width, height=height)
    return fig

def plot_wr_comp(df, feature, years, wrs, width=800, height=600):

    stats = {'Receptions':'Receptions', 'Recieving Yards':'REC_YDS', 'Recieving Touchdowns':'REC_TDS', 'Recieving Yards After Catch':'REC_YAC', 'Targets':'Targets'}
    stats2 = dict(zip(stats.values(), stats.keys()))
    feature = stats[feature]

    df_filtered = df[(df['Year'].isin(years)) & (df['Reciever'].isin(wrs))]

    df_grouped = df_filtered.groupby(['Year', 'Reciever'])[feature].sum().reset_index()

    fig = px.bar(df_grouped, 
                 x='Year', 
                 y=feature, 
                 color='Reciever', 
                 barmode='group', 
                 title=f"Comparison of {stats2[feature]} for {wrs[0]} and {wrs[1]}",
                 labels={feature: feature, 'Reciever': 'Player Name', 'Year': 'Season'},
                 color_discrete_map={wrs[0]: 'blue', wrs[1]: 'lightblue'})

    fig.update_layout(width=width, height=height)

    return fig



    