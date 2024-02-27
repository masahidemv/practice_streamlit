import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#NumercalPython(numpy)モジュールは数値計算
#Pandasモジュールはnumpyで計算された数字を表にまとめたりする
#PILモジュールはPython Image Libraryで画像処理のため
#from PIL import ImageはImage関数だけ取り込む
#import PIL as piでもいい


st.title("超入門")

st.write("画像")

img = Image.open('test.jpg')
st.image(img,caption='八丈島',use_column_width=True)

code = '''import PIL as pi
img = pi.Image.open('test.jpg')'''
st.code(code, language='python')



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
