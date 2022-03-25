import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_echarts import st_echarts
import matplotlib as mpl
from cycler import cycler

st.set_option('deprecation.showPyplotGlobalUse', False)

uploaded_file = st.file_uploader("RAWDATA", type=['xlsx'])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df1 = df.drop(["Source name"], axis=1)
    df2 = df1.transpose()

    df_new = df2.iloc[0]
    df2 = df2.iloc[1:]
    df2.columns = df_new
    df3 = df2.drop(['Log time (UTC)', 'Log time (Local)'], axis=1)

metadata = df3

#st.set_page_config(layout="wide")
chart_visual = st.sidebar.selectbox('Select Analysis',
                                    ("Day's view", 'Power Curve'))
x=[0,1,1.5,2,2.5,2.9,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16,16.5,17,17.5,18,18.5,19,19.5,20,21,22,23]
y=[0,0,0,0,0.5,1,2.5,34,77,141,209,272,373,496,631,776,954,1137,1340,1509,1723,1853,1935,1978,2004,2017,2031,2033,2035,2037,2037,2037,2033,2036,2036,2036,2050,2050,2050,2050,2050,2050,2050,2050]
if chart_visual == 'Power Curve':
    fig = plt.figure(figsize=(15, 8))
    plt.plot(df3['Wind speed - AVE [m/s]'], df3['Active power - AVE [kW]'], 'o', label='Active Power')
    plt.plot(x,y,'-',label='theoretical_power_curve (kwh)',c='r')
    plt.xlabel('wind speed (m/s)', size=15)
    plt.ylabel('Power Production (kw)', size=15)
    plt.title('Wind Turbine Power day Production')
    plt.legend(fontsize=15)
    st.pyplot()

if chart_visual == "Day's view":
    fig = plt.figure(figsize=(15, 8))
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.linestyle'] = '--'
    plt.plot(df3['Wind speed - AVE [m/s]'], df3["Gearbox oil tank temp. - AVE [C]"], label='Relation')
    st.pyplot()



