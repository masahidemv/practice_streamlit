import streamlit as st
import numpy as np
import pandas as pd

#NumercalPython(numpy)数値計算
#例えば下の乱数生成
#

st.title("超入門")

st.write("DataFrame")

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
# #np.のrandom.rando()関数。20行、3列のランダム表を作る。
# #columnsでリスト[]内にしていした名前を列に付ける。

# #表示方法
# # st.write(df)

# #折れ線グラフlinechart
# st.line_chart(df)

st.area_chart(df)

