# ---------------- HOUSE SECTION ----------------

section = "Mobile"

if section == "Laptop":
    # هنا تحط كود اللابتوب
    print("Laptop section")
elif section == "Mobile":
    # هنا تحط كود الموبايل
    print("Mobile section")
elif section == "House":
    # هنا تحط كود البيت
    print("House section")
    st.header("🏠 Apartments in Egypt")

    # اختار المدينة
    city = st.selectbox(
        "Choose city",
        ["Cairo", "Giza", "Alexandria", "Nasr City","Elswiis","ELMaadi","AL Mokattam","EL Harm","EL Hadba","Hadyek Helwan"]
    )

    # اختار نوع الغرفة
    room = st.selectbox(
        "Choose the room",
        ["Bedroom","Kitchen","Living Room","Terrace"," Balcony"]
    )

    # اختيارات إضافية
    wifi = st.checkbox("WiFi Available")
    smart = st.checkbox("Smart Home")
    rooms_count = st.slider("Number of Rooms", 1, 5, 2)
    bathrooms_count = st.slider("Number of Bathrooms", 1, 3, 1)

    st.subheader("Available Apartments")

    # قائمة الشقق
    houses = [
        {"name":"Apartment 1","city":"Cairo","room":"Bedroom","wifi":True,"smart":True,"rooms":3,"bathrooms":2,"price":80000},
        {"name":"Apartment 2","city":"Giza","room":"Living Room","wifi":True,"smart":False,"rooms":2,"bathrooms":1,"price":60000},
        {"name":"Apartment 3","city":"Alexandria","room":"Kitchen","wifi":False,"smart":False,"rooms":1,"bathrooms":1,"price":50000},
        {"name":"Apartment 4","city":"Nasr City","room":"Bedroom","wifi":True,"smart":True,"rooms":4,"bathrooms":2,"price":90000},
        {"name":"Apartment 5","city":"Cairo","room":"Kitchen","wifi":True,"smart":False,"rooms":2,"bathrooms":1,"price":75000},
    ]

    for house in houses:
        if house["city"] == city and house["room"] == room:
            if wifi and not house["wifi"]:
                continue
            if smart and not house["smart"]:
                continue
            if house["rooms"] < rooms_count:
                continue
            if house["bathrooms"] < bathrooms_count:
                continue

            st.write(f"🏠 {house['name']} - {house['rooms']} rooms, {house['bathrooms']} bathrooms - Price: ${house['price']}")
