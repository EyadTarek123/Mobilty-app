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


st.title("Smartphone Price Estimator")
st.sidebar.markdown("<h2 style='color: #2ecc71;'>Adjust Settings:</h2>", unsafe_allow_html=True)
brightness = st.sidebar.slider('Screen Brightness', 50, 100, 75)
contrast = st.sidebar.slider('Screen Contrast', 50, 150, 100)
theme = st.sidebar.selectbox('Theme Color', ['Light', 'Dark', 'Blue'])



lottie_url = "https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json"
lottie_animation = load_lottieurl(lottie_url)
st_lottie(lottie_animation, height=400, speed=1, loop=True)


st.markdown("""
### Welcome to the Smartphone Price Estimator
Use the sliders and input fields below to provide details about your smartphone. 
Our model will estimate the price range based on the features you provide.

### Input Features:
- **Battery Power**: Battery capacity in mAh.
- **Bluetooth**: Presence of Bluetooth connectivity (0 = No, 1 = Yes).
- **Clock Speed**: Processor speed in GHz.
- **Dual SIM**: Indicates whether the phone supports dual SIM (0 = No, 1 = Yes).
- **Front Camera**: Resolution of the front camera in MP.
- **4G Connectivity**: Presence of 4G connectivity (0 = No, 1 = Yes).
- **Internal Memory**: Internal storage capacity in GB.
- **Mobile Depth**: Thickness of the phone in cm.
- **Mobile Weight**: Weight of the phone in grams.
- **Number of Cores**: Number of processor cores.
- **Primary Camera**: Resolution of the primary camera in MP.
- **Pixel Height/Width**: Screen resolution in pixels.
- **RAM**: Memory capacity in MB.
- **Screen Height/Width**: Screen dimensions in inches.
- **Talk Time**: Battery talk time in hours.
- **3G Connectivity**: Presence of 3G connectivity (0 = No, 1 = Yes).
- **Touch Screen**: Indicates if the phone has a touch screen (0 = No, 1 = Yes).
- **WiFi**: Presence of WiFi connectivity (0 = No, 1 = Yes).
""")


battery = st.slider("Battery Power 🔋", 500, 1999)
blue = st.radio("Bluetooth ᛒ", [0, 1])
clock = st.number_input("Clock Speed (GHz)", 0.5, 3.0)
dual_sim = st.selectbox("Dual SIM", [0, 1])
fc = st.slider("Front Camera (MP)", 0, 19)
fourG = st.radio("4G Connectivity", [0, 1])
int_memory = st.number_input("Internal Memory (GB)", 2, 64)
mobile_depth = st.slider("Mobile Depth (cm)", 0.1, 1.0)
mobile_weight = st.number_input("Mobile Weight (g)", 80, 200)
n_core = st.number_input("Number of Cores", 1, 8)
pc = st.number_input("Primary Camera (MP)", 0, 20)
px_height = st.number_input("Pixel Height (px)", 0, 1907)
px_width = st.number_input("Pixel Width (px)", 501, 1998)
ram = st.number_input("RAM (MB)", 263, 3989)
sc_h = st.number_input("Screen Height (in)", 5, 19)
sc_w = st.number_input("Screen Width (in)", 0, 18)
talk_time = st.number_input("Talk Time (hour)", 2, 20)
threeG = st.radio("3G Connectivity", [0, 1])
touch = st.radio("Touch Screen", [0, 1])
wifi = st.radio("WiFi🛜", [0, 1])



if st.button('Calculate Price'):

    loaded_model = joblib.load('pages/best_svc_model.pkl')


    prediction = loaded_model.predict([[
        battery, blue, clock, dual_sim, fc, fourG, int_memory, mobile_depth,
        mobile_weight, n_core, pc, px_height, px_width, ram, sc_h, sc_w,
        talk_time, threeG, touch, wifi
    ]])


    prediction_value = prediction[0] if isinstance(prediction, np.ndarray) else prediction


    price_ranges = {
        0: "3000-7000",
        1: "8000-12000",
        2: "13000-17000",
        3: "18000-22000"
    }
    price_range = price_ranges.get(prediction_value, "Unknown")

    st.markdown(f"""
        <div class='price-box'>
            <p class='custom-text'>Estimated Price: 
            <span class='highlight'>{price_range}</span></p>
        </div>
        """, unsafe_allow_html=True)


    if prediction_value == 0:
        st.image(["low.jpg", "loww.jpg", "lowww.jpg", "lowwww.jpg"], width=300)
    elif prediction_value == 1:
        st.image(["med.jpg", "medd.jpg", "meddd.jpg", "medddd.jpg"], width=300)

    elif prediction_value == 2:
        st.image(["h.jpg", "hh.jpg", "hhh.jpg", "hhhh.jpg"], width=300)
    elif prediction_value == 3:
        st.image(["hi.jpg", "hihi.jpg", "hihihi.jpg", "hihihihi.jpg"], width=300)


    st.markdown("""
    ### Price Comparison
    Here is a general idea of what the estimated price range might buy you in the market:
    - **3000-7000**: Basic smartphones with essential features.
    - **8000-12000**: Mid-range smartphones with better cameras and performance.
    - **13000-17000**: High-end smartphones with advanced features and premium build.
    - **18000-22000**: Premium flagship smartphones with top-of-the-line specs and features.
    """)


st.markdown("""
    <style>
    .price-box {
        background-color: #f7f7f7;
        border: 1px solid #ddd;
        border-radius: 20px;
        padding: 30px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
    }

    .custom-text {
        color: #333;
        font-size: 1.5em;
        font-weight: bold;
    }

    .highlight {
        color: #e74c3c;
        font-size: 2em;
        font-weight: bold;
    }

    .stImage {
        max-width: 100%;
        height: auto;
        border-radius: 20px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
    }

    </style>
""", unsafe_allow_html=True)

