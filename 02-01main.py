import streamlit as st
import numpy as np
import pandas as pd
import PIL as pi

st.title("超入門")

st.write(":orange[画像]")
agree = st.checkbox("画像を:red[表示]")
if agree:
    img = pi.Image.open('test.jpg')
    st.image(img,caption='八丈島',use_column_width=True)


st.write("コードの埋め込み")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.write("NumericalPythonで3列2行の乱数生成")
data_np = np.random.rand(3, 2)
st.write(data_np)

st.write("乱数をナンパイの表dataframeに落とし込む")
df = pd.DataFrame(data_np,columns=['ナンパイ1','ナンパイ2'])
st.write(df)

st.write("チェックボックスで表示非表示")
if st.checkbox('表の表示'):
    df = pd.DataFrame(data_np,columns=['ナンパイ1','ナンパイ2'])
    st.write(df)


st.write(':blue[select box]のつかいかた')
option = st.selectbox(
            '1から10の数を選んで'
            ,list(range(1,11)))
'あなたの選んだ数字は',option,'です。'

st.write(':blue[ブランク]のつくりかた')
'text = st.text_input("質問内容")'
'"あなたの答え：",text'
text = st.text_input('あなたの好きな:rainbow[色]は何ですか？')
'好きな色は:',text

st.write(':blue[スライダー]のつくりかた')
'最小値、最大値、デフォルト'
condetion = st.slider('今の気分は',0,150,75)
'気分は', condetion,'%'