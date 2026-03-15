import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title="Mobility",
    page_icon="📱",
    layout="wide",
)

st.title("Welcome to Mobility App 💻 | مرحبا بك في تطبيق Mobility")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animation
lottie_url = "https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json"
lottie_animation = load_lottieurl(lottie_url)

col1, col2, col3 = st.columns([1,1,2])

with col1:
    st.image("Capture.PNG", width=200)

with col2:
    st.image("dembo.jpeg", width=200)

with col3:
    st_lottie(lottie_animation, height=300)

st.markdown("## 🚀 Discover the Future of Mobile Tech")

st.write(
    "Mobility helps you predict phone prices using AI models and compare devices easily."
)

st.markdown("## 💡 Features")

st.markdown("""
- 📱 Device Comparison  
- 📊 AI Price Prediction  
- 🔔 Price Alerts  
""")

st.markdown("## 💻 Laptop")
st.write("This section analyzes laptop specifications and performance.")

st.markdown("## 🏠 House")
st.write("Mobility technology can also help smart home systems.")

st.markdown("## 📊 Conclusion")
st.write("Mobility uses AI to help users make better technology decisions.")
