import streamlit as st
import manage
import pandas as p

def tofloat(str):
    if(str == 'tbd'):
        return 0
    return float(str)

st.title('Games released in a specific year')

option1 = st.selectbox(
   "Year of Observation",
   manage.yearEx,
   index=1,
   placeholder="Select an year...",
)
#world = world[(world.name!= 'Russia') & (world.name!= 'Iceland')]

showing = manage.months_per_year[(manage.months_per_year['release_date'] == option1)]
showing = showing.groupby(['monthes'])['name'].count()
st.bar_chart(showing)

st.title('Mean of rating of a specific year')
double_rating = manage.months_per_year['user_review'].apply(tofloat)
chart_rating11 = manage.months_per_year
chart_rating11['user_review'] = double_rating
chart_rating1 = chart_rating11.drop(chart_rating11[chart_rating11['user_review'] == 0].index)

chart_rating = chart_rating1.groupby(['release_date'])['user_review'].mean()
st.bar_chart(chart_rating)