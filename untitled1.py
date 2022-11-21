# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:36:51 2022

@author: m45subaru
"""
import streamlit as st
import pandas as pd
import numpy as np

st.title('初めてのstreamlit')
st.write('これから作品をつくっていきます')
text = st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は,',text,'です')
condition = st.slider('あなたの今の調子は?',0, 100, 50)
option = st.selectbox('好きな数字を教えてください',list(['1番','2番','3番','4番']))
df = pd.DataFrame([[36.6431,138.1886]],columns = ['lat','lon',])
st.map(df)
df = pd.DataFrame([[36.676037,138.213074]],columns = ['lat','lon',])
st.map(df)
