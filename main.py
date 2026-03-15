import streamlit as st

st.set_page_config(page_title="Mobility App", layout="wide")

st.title("Mobility App 🔎")

# اختيار القسم
section = st.sidebar.selectbox(
    "Choose Section",
    ["Mobile", "Laptop", "House"]
)

# اختيار الميزانية
salary = st.sidebar.slider("Choose your budget ($)", 100, 3000, 500)

# ---------------- MOBILE ----------------
if section == "Mobile":

    st.header("📱 Mobile Features")

    camera = st.checkbox("Good Camera")
    battery = st.checkbox("Big Battery")
    gaming = st.checkbox("Gaming")
    fast_charge = st.checkbox("Fast Charging")
    amoled = st.checkbox("AMOLED Screen")

    st.subheader("Recommended Mobiles")

    if salary <= 300:
        st.write("• Xiaomi Redmi Note 12")
        st.write("• Samsung Galaxy A14")

    elif salary <= 700:
        st.write("• Samsung Galaxy S21 FE")
        st.write("• iPhone 12")

    else:
        st.write("• iPhone 14")
        st.write("• Samsung Galaxy S23")

# ---------------- LAPTOP ----------------
elif section == "Laptop":

    st.header("💻 Laptop Features")

    ram = st.checkbox("16GB RAM")
    ssd = st.checkbox("SSD")
    gpu = st.checkbox("Gaming GPU")
    light = st.checkbox("Lightweight")
    battery = st.checkbox("Long Battery")

    st.subheader("Recommended Laptops")

    if salary <= 700:
        st.write("• HP Pavilion")
        st.write("• Lenovo IdeaPad 3")

    elif salary <= 1500:
        st.write("• Dell XPS 13")
        st.write("• MacBook Air M1")

    else:
        st.write("• MacBook Pro M2")
        st.write("• ASUS ROG Zephyrus")

# ---------------- HOUSE ----------------
elif section == "House":

    st.header("🏠 House Features")

    smart = st.checkbox("Smart Home")
    security = st.checkbox("Security Cameras")
    solar = st.checkbox("Solar Energy")
    wifi = st.checkbox("Strong WiFi")
    automation = st.checkbox("Home Automation")

    st.subheader("Recommended Solutions")

    if salary <= 500:
        st.write("• Smart Lights System")
        st.write("• Basic Security Camera")

    elif salary <= 1500:
        st.write("• Smart Home Starter Kit")
        st.write("• Google Nest System")

    else:
        st.write("• Full Smart Home Setup")
        st.write("• Solar + Automation System")
