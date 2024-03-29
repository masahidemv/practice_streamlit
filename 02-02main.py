import streamlit as st
import numpy as np
import pandas as pd
import PIL as pi

st.title("超入門")

st.write(":orange[レイアウト]")
'sidebarの使い方'
'st.sidebar.ﾒｿｯﾄﾞ'

st.sidebar.write(":orange[wigets]")

option = st.sidebar.selectbox(
            '1から10の数を選んで'
            ,list(range(1,11)))

text = st.sidebar.text_input('あなたの好きな:rainbow[色]は何ですか？')

condetion = st.sidebar.slider('今の気分は',0,150,75)

'あなたの選んだ数字は',option,'です。'
'好きな色は:',text
'気分は', condetion,'%'

'2カラム（列）レイアウト'
'左列から1，2の名前'
col1,col2 = st.columns(2)
button = col1.button('col2に文字表示')
if button:
    col2.write('col2')

'expander'
sample_ex = st.expander('詳しい説明')
sample_ex.write('st.expanderに名前を付けて、関数を作る。関数を作ったらそれに.writeをつけて、表示したい内容を書く')