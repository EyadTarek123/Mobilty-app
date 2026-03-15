import streamlit as st

st.set_page_config(page_title="Mobility App", page_icon="📱", layout="wide")

st.title("Mobility App 🌐")

# اختيار القسم
section = st.sidebar.selectbox(
    "Choose Section | اختر القسم",
    ["Mobile", "Laptop", "House"]
)

# -------- MOBILE --------
if section == "Mobile":

    st.header("📱 Mobile Features")

    camera = st.checkbox("Good Camera")
    battery = st.checkbox("Big Battery")
    gaming = st.checkbox("Gaming Performance")
    cheap = st.checkbox("Cheap Price")

    st.subheader("Your Selection")

    if camera:
        st.write("📷 You selected: Good Camera")

    if battery:
        st.write("🔋 You selected: Big Battery")

    if gaming:
        st.write("🎮 You selected: Gaming Performance")

    if cheap:
        st.write("💰 You selected: Cheap Price")


# -------- LAPTOP --------
elif section == "Laptop":

    st.header("💻 Laptop Features")

    ram = st.checkbox("16GB RAM")
    ssd = st.checkbox("SSD Storage")
    gpu = st.checkbox("Gaming GPU")
    light = st.checkbox("Light Weight")

    st.subheader("Your Selection")

    if ram:
        st.write("⚡ 16GB RAM")

    if ssd:
        st.write("💾 SSD Storage")

    if gpu:
        st.write("🎮 Gaming GPU")

    if light:
        st.write("🪶 Light Weight Laptop")


# -------- HOUSE --------
elif section == "House":

    st.header("🏠 House Features")

    smart = st.checkbox("Smart Home")
    security = st.checkbox("Security Cameras")
    solar = st.checkbox("Solar Energy")
    wifi = st.checkbox("Strong WiFi")

    st.subheader("Your Selection")

    if smart:
        st.write("🏠 Smart Home Enabled")

    if security:
        st.write("📹 Security Cameras")

    if solar:
        st.write("☀️ Solar Energy")

    if wifi:
        st.write("📡 Strong WiFi")
