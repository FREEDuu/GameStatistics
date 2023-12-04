import streamlit as s
import manage

s.title('CHARTS PAGE')
s.subheader('chart of game accessible in a platform')
s.bar_chart(manage.count_platform)
s.subheader('chart of games with a specific rate')
s.bar_chart(manage.rating_games)
s.subheader('chart of games released on a specific year')
s.bar_chart(manage.year_games)