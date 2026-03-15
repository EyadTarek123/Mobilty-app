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
      background: linear-gradient(to right, #e0eafc, #cfdef3);
      font-family: 'Roboto', sans-serif;
  }
  h1 {
      font-size: 36px;
      color: #2c3e50;
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
      color: #34495e;
      font-size: 1.8em;
      font-weight: 600;
  }
  .highlight {
      color: #e67e22;
      font-size: 2.4em;
      font-weight: bold;
      animation: pulse 1.5s infinite;
  }
  @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.1); }
      100% { transform: scale(1); }
  }
  </style>
""", unsafe_allow_html=True)


st.markdown("<h1>House Price Estimator</h1>", unsafe_allow_html=True)


lottie_url = "https://assets4.lottiefiles.com/packages/lf20_5e7wgehs.json"
lottie_animation = load_lottieurl(lottie_url)
if lottie_animation:
    st_lottie(lottie_animation, height=300, speed=1.0, loop=True)


st.sidebar.markdown("<h2 style='color: #1abc9c;'>Customize Inputs:</h2>", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns(4)

with col1:
    area = st.slider("Area (in sq ft)", 500, 9400, step=100)
    num_rooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5, 6, 7, 8])
    resale = st.radio("Is it a Resale Property?", ['Yes', 'No'])
    swimming_pool = st.radio("Swimming Pool Available?", ['Yes', 'No'])
    gym = st.radio("Gymnasium Available?", ['Yes', 'No'])

with col2:
    security = st.number_input('Security Score (0-9)', 0, 9)
    landscaped_garden = st.slider('Landscaped Garden Score', 0, 9)
    club_house = st.slider('Club House Score', 0, 9)
    sports_facility = st.slider('Sports Facility Score', 0, 9)
    jogging_track = st.slider('Jogging Track Score', 0, 9)

with col3:
    school_nearby = st.slider('School Nearby Score', 0, 9)
    hospital_nearby = st.slider('Hospital Nearby Score', 0, 9)
    car_parking = st.slider('Car Parking Spaces', 0, 5)
    staff_quarter = st.radio('Staff Quarter Available?', ['Yes', 'No'])
    cafeteria = st.radio('Cafeteria Available?', ['Yes', 'No'])

with col4:
    atm_nearby = st.radio('ATM Nearby?', ['Yes', 'No'])
    lift_available = st.radio('Lift Available?', ['Yes', 'No'])
    gas_station = st.radio('Gas Station Nearby?', ['Yes', 'No'])
    wifi = st.radio('Wi-Fi Available?', ['Yes', 'No'])
    ac_available = st.radio('AC Available?', ['Yes', 'No'])


st.markdown("<h3>Enter Additional Amenities:</h3>", unsafe_allow_html=True)


if st.button('Calculate Price'):

    loaded_model = joblib.load('best_mod.pkl')


    user_input = np.array([
        area, num_rooms, 1 if resale == 'Yes' else 0, security,
        1 if swimming_pool == 'Yes' else 0, 1 if gym == 'Yes' else 0,
        landscaped_garden, club_house, sports_facility, jogging_track,
        school_nearby, hospital_nearby, car_parking, 
        1 if staff_quarter == 'Yes' else 0, 1 if cafeteria == 'Yes' else 0,
        1 if atm_nearby == 'Yes' else 0, 1 if lift_available == 'Yes' else 0,
        1 if gas_station == 'Yes' else 0, 1 if wifi == 'Yes' else 0,
        1 if ac_available == 'Yes' else 0
    ]).reshape(1, -1)

    prediction = loaded_model.predict(user_input)


    st.markdown(f"""
      <div class='price-box'>
          <p class='custom-text'>Estimated Price: 
          <span class='highlight'>${prediction[0]:,.2f}</span></p>
      </div>
    """, unsafe_allow_html=True)