from typing import Text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

#ページのタイトル作成
st.title('streamlit超入門')

#プログレスバー（ダウンロードの表示みたいなやつ）
st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'完了！！'


# #文章書くときはwrite
# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40],
# })

# #並び替えとかができるデータフレームを作成する
# st.dataframe(df.style.highlight_max(axis=0))

# #ただ表を出したいとき
# #st.table(df.style.highlight_max(axis=0))

# #文字列の書き方(マークダウン表記ができる)
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


# df2 = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a','b','c']
# )
# #折れ線グラフの作成
# st.write('折れ線グラフ')
# st.line_chart(df2)
# #折れ線の下を塗ったグラフ
# st.write('折れ線の中を塗る')
# st.area_chart(df2)
# #棒グラフ
# st.write('棒グラフ')
# st.bar_chart(df2)

# #新宿近辺の緯度と経度の位置にプロットする
# df3 = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['latitude', 'longitude']
# )
# st.map(df3)

# st.write("Display Image")

# #チェック僕巣にチェックが入ったら画像が表示される
# if st.checkbox('Show Image'):
#     img = Image.open('logo.jpg')
#     st.image(img, caption='logo', use_column_width=True)

# #use_column_width=Trueはwebアプリの幅に合わせて表示

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 100))
# )

# 'あなたが好きな数字は', option, 'です'


# # st.write('テキスト入力を読み取り、反映させる')
# # text = st.sidebar.text_input('あなたの趣味を教えてください')
# # 'あなたの趣味は', text, 'です'

# # #スライダー, 最後の50は最初に選択されている場所
# # #sidebarはアプリの横の部分に入力バーが出てくる
# # cond = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# # 'コンディション:', cond,'です'

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('よくある問い合わせ')
expander2 = st.expander('問い合わせ2')
expander2.write('データの記入について')
expander3 = st.expander('問い合わせ3')
expander3.write('計算について')
expander4 = st.expander('問い合わせ4')
expander4.write('文字の大きさについて')



# st.write('テキスト入力を読み取り、反映させる')
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', text, 'です'

# #スライダー, 最後の50は最初に選択されている場所
# #sidebarはアプリの横の部分に入力バーが出てくる
# cond = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', cond,'です'