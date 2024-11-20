import streamlit as st

from analysis import get_multiselect_options
from analysis import provide_data_find
from analysis import get_options_brand
from analysis import get_options_model
from analysis import get_options_propulsion

# Layout
st.set_page_config(layout="wide")

# Title Streamlit
st.header('AutoScout360 - With some clever insights to your new car!')

# Sidebar
st.sidebar.markdown('# FIND your new car:')

# Find car
# Get brands for multiselect 'car_brand'
options_brand = get_options_brand()

default_values_find = {
    'find_car_brand': [],
    'find_car_mileage': (0, 100000),
    'find_car_model': [],
    'find_car_fuel': [],
    'find_car_gear': [],
    'find_car_hp': (0, 500),
    'find_car_year': (2000, 2024)
}

# Initialize session state
for key, value in default_values_find.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Sidebar Widgets
input_brand_find = st.sidebar.multiselect(
    label='Car Brand:',
    options=options_brand,
    default=st.session_state['find_car_brand'],
    key='find_car_brand'
)
# Ask for options_model based on selected car brands
if input_brand_find:
    options_model = get_options_model(input_brand_find)
else:
    options_model = get_multiselect_options(None)

input_model_find = st.sidebar.multiselect(
    label='Model:',
    options=options_model,
    default=st.session_state['find_car_model'],
    key='find_car_model'
)
if (input_brand_find) and (input_model_find):
    options_fuel = get_options_propulsion(input_brand_find, input_model_find)
else:
    options_fuel= get_multiselect_options(None)

# Ask for options_fuel based on selected brands and models
input_fuel_find = st.sidebar.multiselect(
    label='Propulsion:',
    options=options_fuel,
    default=st.session_state['find_car_fuel'],
    key='find_car_fuel'
)

options_mileage,options_gear, options_hp, options_year = get_multiselect_options(input_brand_find)

input_gear_find = st.sidebar.multiselect(
    label='Gear:',
    options=options_gear,
    default=st.session_state['find_car_gear'],
    key='find_car_gear'
)
input_hp_find = st.sidebar.slider(
    label='Horsepower:',
    min_value=min(options_hp),
    max_value=max(options_hp),
    value=st.session_state['find_car_hp'],
    key='find_car_hp'
)
input_mileage_find = st.sidebar.slider(
    label='Mileage:',
    min_value=min(options_mileage),
    max_value=max(options_mileage),
    value=st.session_state['find_car_mileage'],
    key='find_car_mileage'
)
input_year_find = st.sidebar.slider(
    label='Year of Registration:',
    min_value=min(options_year),
    max_value=max(options_year),
    value=st.session_state['find_car_year'],
    key='find_car_year'
)

col1, col2 = st.sidebar.columns(2)
button_find_car = col1.button(label='Find car', key='find_car_button')
button_find_car_reset = col2.button(label='Reset', key='find_car_reset_button')

# Provide data
if button_find_car:
    provide_data_find(input_mileage_find, input_brand_find, input_model_find, input_fuel_find, input_gear_find, input_hp_find, input_year_find)

# Reset button logic
if button_find_car_reset:
    st.session_state.clear()
    st.experimental_rerun()

st.sidebar.markdown('---')  # Spatial separation

# Sell car

# Set default values
default_values_sell = {
    'sell_car_mileage': 0, # number_input
    'sell_car_brand': [],  # multiselect
    'sell_car_model': [],  # multiselect
    'sell_car_fuel': [],   # multiselect
    'sell_car_gear': [],   # multiselect
    'sell_car_hp': 0,      # number_input
    'sell_car_year': 0     # number_input
}

# Initialize session state for filters if not already set
for key, value in default_values_sell.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.sidebar.markdown('# SELL your old car:')

input_brand_sell = st.sidebar.multiselect(
    label='Car Brand:',
    options=options_brand,
    default = st.session_state['sell_car_brand'],
    key='sell_car_brand'
)
input_model_sell = st.sidebar.multiselect(
    label='Model:',
    options=options_model,
    default = st.session_state['sell_car_model'],
    key='sell_car_model'
)
input_fuel_sell = st.sidebar.multiselect(
    label='Propulsion:',
    options=options_fuel,
    default = st.session_state['sell_car_fuel'],
    key='sell_car_fuel'
)
input_gear_sell = st.sidebar.multiselect(
    label='Gear:',
    options=options_gear,
    default = st.session_state['sell_car_gear'],
    key='sell_car_gear'
)
input_hp_sell = st.sidebar.number_input(
    label='Enter Horsepower:',
    value=st.session_state['sell_car_hp'],
    key='sell_car_hp',
    step=1
)
input_mileage_sell = st.sidebar.number_input(
    label='Enter Mileage:',
    placeholder='None',
    value = st.session_state['sell_car_mileage'],
    key='sell_car_mileage',
    step=1
)
input_year_sell = st.sidebar.number_input(
    label='Enter Year of Registration',
    value=st.session_state['sell_car_year'],
    key='sell_car_year',
    step=1
)

col1, col2 = st.sidebar.columns(2)
button_sell_car = col1.button(label='Sell car', key='sell_car_button')
button_sell_car_reset = col2.button(label='Reset', key='sell_car_reset_button')

# Handle reset button for sell car section
if button_sell_car_reset:
    st.session_state.clear()
    st.experimental_rerun()
