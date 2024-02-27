import streamlit as st
import numpy as np
import pandas as pd

# stlimitを使ってtitle「Streamit超入門」をwebに表示する
st.title('Streamlit 超入門')
# 実行はターミナルでstreamlit run main.pyを打ち込んでenter
#titleのしたに本文（titleよりちいさい）を入れる。
st.write('DataFrame')

#pandasの「pd.」クラス「DataFrame()」で表(オブジェクト）を作る。
#()の中は{}で辞書型、[]でリスト型。
df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#上の表dfをstreamlitで表示させる。
#表示方法はwriteかdataframeかtable
#違いは表サイズ変更の可(dataframe)否(write)tableは変更の効かないデータベース
#st.write(df)
#st.dataframe(df,width=200,height=100)

#dataframeで表示する場合はdfオブジェクトの装飾style.も可能。
#styleはpandasの「pd.」クラス。
#1列2列それぞれの最大値maxの列axis=0をhighlite表示する
# st.dataframe(df.style.highlight_max(axis=0),width=200,height=100)

st.table(df.style.highlight_max(axis=0))

#実行はターミナルでstreamlit run ファイル名

"""
#   章
##  節
### 項

本文
改行は１行空けないとダメ。

コードの埋め込みは'''のあとにpython_'''

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""