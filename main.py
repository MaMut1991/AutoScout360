# With this file, you can start the Streamlit app. Please open the console and type 'streamlit run main.py'.

# In addition, this file controls all the other files by calling functions.

# Import Libraries
import streamlit as st

# Title Streamlit 
st.header('AutoScout360 - With some clever insights to your new car!')

# Sidebar

# Find car
options_mileage = [0,1000]
options_brand = []
options_model = []
options_fuel = []
options_gear = []
options_hp = []
options_year = [2011,2021]

st.sidebar.markdown('# FIND your new car:')
input_mileage_find = st.sidebar.slider(label='Choose range for mileage:',min_value=options_mileage[0],max_value=options_mileage[1], value=options_mileage, step=10, key='find_car_mileage')
input_brand_find = st.sidebar.multiselect(label='Car Brand:',options=options_brand, key='find_car_brand')
input_model_find = st.sidebar.multiselect(label='Model:',options=options_model, key='find_car_model')
input_fuel_find = st.sidebar.multiselect(label='Fuel:',options=options_fuel,key='find_car_fuel')
input_gear_find = st.sidebar.multiselect(label='Gear:',options=options_gear,key='find_car_gear')
input_hp_find = st.sidebar.multiselect(label='Horsepower:',options=options_hp,key='find_car_hp')
input_year_find = st.sidebar.slider(label='Choose range for Year of Registration:',min_value=options_year[0],max_value=options_year[1],value=options_year,key='find_car_year')

col1,col2 = st.sidebar.columns(2)
button_find_car = col1.button('Find car')
button_find_car_reset = col2.button('Reset') 

# Sell car
st.sidebar.markdown('# SELL your old car:')
input_mileage_sell = st.sidebar.number_input(label='Enter Mileage:',placeholder='None',key='sell_car_mileage')
input_brand_sell = st.sidebar.multiselect(label='Car Brand:',options=options_brand,key='sell_car_brand')
input_model_sell = st.sidebar.multiselect(label='Model:',options=options_model,key='sell_car_model')
input_fuel_sell = st.sidebar.multiselect(label='Fuel:',options=options_fuel,key='sell_car_fuel')
input_gear_sell = st.sidebar.multiselect(label='Gear:',options=options_gear,key='sell_car_gear')
input_hp_sell = st.sidebar.number_input(label='Enter Horsepower:',key='sell_car_hp')
input_year_sell = st.sidebar.number_input(label='Enter Year of Registration',key='sell_car_year')

