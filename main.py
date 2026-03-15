import streamlit as st

st.set_page_config(page_title="Mobility App", layout="wide")

st.title("Mobility App 🔎")

section = st.sidebar.selectbox(
    "Choose Section",
    ["Mobile", "Laptop", "House"]
)

budget = st.sidebar.number_input("Enter your budget ($)", min_value=0)

# ---------------- MOBILE DATA ----------------

mobiles = [
{"name":"iPhone 15","price":1100,"camera":True,"battery":True,"gaming":True},
{"name":"iPhone 14","price":900,"camera":True,"battery":True,"gaming":True},
{"name":"Samsung S23","price":850,"camera":True,"battery":True,"gaming":True},
{"name":"Samsung A54","price":400,"camera":True,"battery":True,"gaming":False},
{"name":"Xiaomi Redmi Note 12","price":250,"camera":True,"battery":True,"gaming":False},
{"name":"Xiaomi Poco X5","price":320,"camera":True,"battery":True,"gaming":True},
{"name":"Realme GT","price":500,"camera":True,"battery":True,"gaming":True},
{"name":"Oppo Reno 8","price":550,"camera":True,"battery":True,"gaming":False},
{"name":"Google Pixel 7","price":700,"camera":True,"battery":True,"gaming":True},
{"name":"OnePlus 11","price":750,"camera":True,"battery":True,"gaming":True},
]

# ---------------- HOUSE DATA ----------------

houses = [
{"name":"Apartment in Cairo","price":80000,"room":"Bedroom","wifi":True,"smart":True},
{"name":"Apartment in Giza","price":60000,"room":"Living Room","wifi":True,"smart":False},
{"name":"Apartment in Alexandria","price":50000,"room":"Kitchen","wifi":False,"smart":False},
{"name":"Apartment in Nasr City","price":90000,"room":"Bedroom","wifi":True,"smart":True},
]

# ---------------- MOBILE SECTION ----------------

if section == "Mobile":

    st.header("📱 Mobile Features")

    camera = st.checkbox("High Camera")
    battery = st.checkbox("Big Battery")
    gaming = st.checkbox("Gaming Performance")

    st.subheader("Recommended Mobiles")

    for phone in mobiles:

        if phone["price"] <= budget:

            if camera and not phone["camera"]:
                continue
            if battery and not phone["battery"]:
                continue
            if gaming and not phone["gaming"]:
                continue

            st.write(f"📱 {phone['name']} - ${phone['price']}")

# ---------------- LAPTOP SECTION ----------------

elif section == "Laptop":

    st.header("💻 Laptop Features")

    ram = st.checkbox("16GB RAM")
    ssd = st.checkbox("SSD")
    gpu = st.checkbox("Gaming GPU")

    laptops = [
    {"name":"MacBook Air M1","price":1000},
    {"name":"Dell XPS 13","price":1200},
    {"name":"HP Pavilion","price":700},
    {"name":"ASUS ROG","price":1800},
    ]

    st.subheader("Recommended Laptops")

    for laptop in laptops:
        if laptop["price"] <= budget:
            st.write(f"💻 {laptop['name']} - ${laptop['price']}")

# ---------------- HOUSE SECTION ----------------

elif section == "House":

    st.header("🏠 Choose Room in the Apartment")

    room = st.selectbox(
        "Choose the place in the apartment",
        ["Bedroom","Kitchen","Living Room"]
    )

    wifi = st.checkbox("WiFi Available")
    smart = st.checkbox("Smart Home")

    st.subheader("Available Apartments")

    for house in houses:

        if house["room"] == room:

            if wifi and not house["wifi"]:
                continue
            if smart and not house["smart"]:
                continue

            st.write(f"🏠 {house['name']} - Price: ${house['price']}")
