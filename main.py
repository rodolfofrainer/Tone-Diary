import streamlit as st
import glob
import plotly.express as px

import backend

diary = sorted(glob.glob('diary_entries/*.txt'))

entries = []

for i in diary:
    with open(i, 'r') as file:
        entry = file.read()
        entries.append(entry)


general_sentiment = backend.analyze_entries(entries)

positivity = [i['pos'] for i in general_sentiment]
negativity = [i['neg'] for i in general_sentiment]

entries_date = [i[14:-4] for i in diary]

st.title('Tone Diary')

st.subheader('Positivity')
figure = px.line(x=entries_date, y=positivity)
st.plotly_chart(figure)

st.subheader('Negativity')
figure = px.line(x=entries_date, y=negativity)
st.plotly_chart(figure)
