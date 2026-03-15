import streamlit as st
import joblib
import numpy as np
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
    body {
        background: linear-gradient(to right, #f5f7fa, #c3cfe2);
        font-family: 'Roboto', sans-serif;
    }
    h1 {
        font-size: 36px;
        color: #3498db;
        text-align: center;
    }
    .price-box {
        background-color: #f9f9f9;
        border: 1px solid #ccc;
        border-radius: 20px;
        padding: 40px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);
        transition: transform 0.6s ease, box-shadow 0.6s ease;
    }
    .price-box:hover {
        transform: scale(1.1);
        box-shadow: 0px 14px 28px rgba(0, 0, 0, 0.2);
    }
    .custom-text {
        color: #2c3e50;
        font-size: 1.8em;
        font-weight: 600;
    }
    .highlight {
        color: #e74c3c;
        font-size: 2.4em;
        font-weight: bold;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .stImage {
        max-width: 100%;
        height: auto;
        border-radius: 20px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
    }
    .stImage:hover {
        box-shadow: 0px 12px 24px rgba(0, 0, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1>💻 Laptop Price Estimator 💻</h1>", unsafe_allow_html=True)


lottie_url = "https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json"
lottie_animation = load_lottieurl(lottie_url)
if lottie_animation:
    st_lottie(lottie_animation, height=300, speed=1.2, loop=True)


st.sidebar.markdown("<h2 style='color: #2ecc71;'>Adjust Settings:</h2>", unsafe_allow_html=True)
brightness = st.sidebar.slider('Screen Brightness', 50, 100, 75)
contrast = st.sidebar.slider('Screen Contrast', 50, 150, 100)
theme = st.sidebar.selectbox('Theme Color', ['Light', 'Dark', 'Blue'])


st.markdown("<div style='padding: 10px; background-color: #f0f8ff; border-radius: 10px;'>### Enter Laptop Specifications:</div>", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    brands_list = ['Lenovo', 'HP', 'DELL', 'ASUS', 'acer', 'MSI', 'APPLE', 'RedmiBook',
                   'Avita', 'realme', 'Infinix', 'Vaio', 'Nokia', 'ALIENWARE', 'Smartron']
    brand = st.selectbox('Brand', brands_list)
    model = st.slider("Model", 0, 100)
    processor_gnrtn = st.selectbox('Processor Generation', ['1st', '2nd', '3rd', '4th'])
    ram_gb = st.number_input('RAM (GB)', min_value=4, max_value=64, step=4)
    ram_type = st.radio('RAM Type', ['DDR3', 'DDR4'])
    ssd = st.slider('SSD Storage (GB)', 0, 3072)
    hdd = st.slider('HDD Storage (GB)', 0, 2048)

with col2:
    os_bit = st.radio('Operating System Bit', [32, 64])
    graphic_card_gb = st.select_slider('Graphics Card (GB)', options=[0, 1, 2, 3, 4])
    warranty = st.selectbox('Warranty (Years)', [0, 1, 2, 3])
    touchscreen = st.checkbox('Touchscreen')
    msoffice = st.checkbox('Includes MS Office')
    discount = st.slider('Discount (%)', 0, 57)
    star_rating = st.select_slider('Star Rating', options=[0, 1, 2, 3, 4, 5])
    ratings = st.number_input('Total Ratings', min_value=0, max_value=20000, value=1000, step=100)
    reviews = st.number_input('Total Reviews', min_value=0, max_value=3000, value=500, step=50)


if st.button('Calculate Price'):

    brand_mapping = {'Lenovo': 0, 'Avita': 1, 'Hp': 2, 'Acer': 3, 'Asus': 4, 
         'Dell': 5, 'Redmibook': 6, 'Realme': 7, 'Infinix': 8, 
         'Microsoft': 9, 'Smartron': 10, 'Lg': 11, 'Nokia': 12, 
         'Msi': 13, 'Apple': 14, 'Vaio': 15, 'Mi': 16}


    brand_num = brand_mapping[brand]


    loaded_model = joblib.load('best_mod.pkl')

    user_input = np.array([[
        brand_num, model,
        int(processor_gnrtn[0]), ram_gb, 1 if ram_type == 'DDR4' else 0, ssd,
        hdd, os_bit, graphic_card_gb, warranty,
        int(touchscreen),
        int(msoffice), discount, star_rating, ratings, reviews
    ]])

    prediction = loaded_model.predict(user_input)
    prediction_value = prediction[0] if isinstance(prediction, np.ndarray) else prediction


    st.markdown(f"""
        <div class='price-box'>
            <p class='custom-text'>Estimated Price: 
            <span class='highlight'>{prediction_value:.2f}</span></p>
        </div>
    """, unsafe_allow_html=True)