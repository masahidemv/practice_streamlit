import streamlit as st
import numpy as np
import pandas as pd

st.title("超入門")

st.write("DataFrame")

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.41581022902257, 139.63505642572176],
    columns=['lat','lon']
)
# #np.のrandom.rando()関数。20行、2列のランダム表を作る。
# #columnsでリスト[]内に指定した名前を列に付ける。
#mapに座標をプロットする場合の列名はlat,lon限定

# #表示方法
# # st.write(df)

# #折れ線グラフlinechart
# st.line_chart(df)

# st.dataframe(df,width=200,height=300)

st.map(df)