import streamlit
import pandas as pd
import requests

streamlit.title('My Breakfast list')
streamlit.header('Having breakfast with brother')
streamlit.text('list of breakfast items')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

my_fruits= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect("list of fruits in drink:", list(my_fruits.Fruit))

streamlit.dataframe(my_fruits)
