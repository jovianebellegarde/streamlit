import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

# Breakfast menu
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Smoothie menu
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Read CSV file into a dataframe from S3 bucket
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display table on page
streamlit.dataframe(fruits_to_show)
