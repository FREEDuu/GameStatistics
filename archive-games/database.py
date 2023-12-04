import streamlit as s
import manage

s.title('VideoGame Data')
s.write('Starting big dataframe !')
s.write(manage.dataframe)
s.write('Some curios dumps and grupping by')
c1 ,c2, c3 = s.columns(3)
with c2:
    s.write(manage.count_platform)
with c1:
    s.write(manage.rating_games)
with c3:
    s.write(manage.year_games)

    