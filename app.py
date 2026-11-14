import streamlit as st
import pandas as pd
from streamlit.elements.lib.color_util import Color

st.title('Первое приложение на Streamlit')
st.header('Это заголовок')
st.subheader('это подзаголовок')

st.write('Привет это я пишу какой-то текст')

# st.caption(
#     'Пояснительная подпись'
#     help='Подсказка'
# )

st.markdown('# markdown 1')
st.markdown('## markdown 2')
st.markdown('### markdown 3')

st.markdown("<span style='color:red'> Red text</span>", unsafe_allow_html=True)


#_________________ТАБЛИЧНЫЕ ДАННЫЕ_______________
#словарь
custom_dict = {
    'course' : [1, 2, 3, 4, 5],
    'marks' : [8, 9, 10, 6, 8]
}

st.write(custom_dict)
# Датафрейм
custom_df = pd.DataFrame(custom_dict)
st.write(custom_df)

st.header('Это загруженный датасет')
#csv в дата фрейм
df = pd.read_csv('data/Pop Mart IP sales in various countries in 2025.csv')
st.write(df)