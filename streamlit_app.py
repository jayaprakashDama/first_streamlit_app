import streamlit
import pandas as pd

streamlit.title('My Breakfast list')
streamlit.header('Having breakfast with brother')
streamlit.text('list of breakfast items')

my_fruits= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
myfruits = myfruits.set_index('Fruit')
streamlit.dataframe(my_fruits)
streamlit.multiselect("list of fruits in drink:", list(my_fruits.index))
