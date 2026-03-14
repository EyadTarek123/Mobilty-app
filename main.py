import streamlit as st
from streamlit_lottie import st_lottie
import requests 
import streamlit as st
import stripe
from streamlit_lottie import st_lottie  

stripe.api_key = "sk_test_XXXXXXX"  
st.title("Welcome to Mobility App 💻 | مرحبا بك في تطبيق Mobility App")
if "paid" not in st.session_state:
    st.session_state.paid = False


if not st.session_state.paid:
    st.write("Before using the app, please pay $5 | قبل ما تستخدم التطبيق، ادفع 5$")
    
    if st.button("Pay Now | ادفع الآن"):

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": "Access to Mobility App | الوصول لتطبيق Mobility App"
                    },
                    "unit_amount": 500,  
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="https://your-streamlit-app-link/?success=true",
            cancel_url="https://your-streamlit-app-link/?canceled=true",
        )
        st.write(f"[Click here to pay | اضغط هنا للدفع]({session.url})")
else:
    st.write("✅ Thanks for paying! Now you can use the app | شكراً لدفعك، الآن يمكنك استخدام التطبيق")
    
    st.write("Here starts your app content | هنا يبدأ محتوى التطبيق")
    
st.set_page_config(
    page_title="Mobility",
    page_icon="📱",
    layout="wide",
)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.markdown("<h1 class='title'>🌐 Welcome to Mobility!</h1>", unsafe_allow_html=True)


st.sidebar.markdown("<h2 style='color:#2ecc71;'>🎨 Choose Theme</h2>", unsafe_allow_html=True)
theme_col1, theme_col2, theme_col3 = st.sidebar.columns(3)

if theme_col1.button("Light"):
    theme = "Light"
elif theme_col2.button("Dark"):
    theme = "Dark"
elif theme_col3.button("Blue"):
    theme = "Blue"
else:
    theme = "Light"  


if theme == "Light":
    bg_color = "#ECF0F1"
    text_color = "#2C3E50"
    accent_color = "#1F8A70"
elif theme == "Dark":
    bg_color = "#1E1E1E"
    text_color = "#ECF0F1"
    accent_color = "#E74C3C"
else:  
    bg_color = "#D6EAF8"
    text_color = "#154360"
    accent_color = "#2E86C1"


st.markdown(f"""
    <style>
    body {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .title {{
        text-align: center;
        color: {accent_color};
        font-size: 3em;
        animation: glow 1s ease-in-out infinite alternate;
    }}
    .section {{
        background-color: {bg_color};
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 30px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }}
    .highlight {{
        color: {accent_color};
        font-weight: bold;
    }}
    @keyframes glow {{
        from {{ text-shadow: 0 0 10px {accent_color}; }}
        to {{ text-shadow: 0 0 20px {accent_color}; }}
    }}
    </style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 1, 2])
with col1:
#     st.image("dembo.jpeg", width=200)
# with col2:
#     st.image("mahatech.jpeg", width=200)

    lottie_url = "https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json"
    lottie_animation = load_lottieurl(lottie_url)
    st_lottie(lottie_animation, height=300)


st.markdown(f"""
<div class="section">
    <h2>🚀 Discover the Future of Mobile Tech</h2>
    <p>
        <span class="highlight">Mobility</span> helps you predict phone prices using powerful AI models.
        Compare devices, analyze trends, and make smarter decisions.
    </p>
</div>

<div class="section">
    <h2>💡 Key Features</h2>
    <ul style="text-align:left; font-size:1.2em; line-height:1.6;">
        <li>📱 <strong>Device Comparison:</strong> Compare specs side by side.</li>
        <li>📊 <strong>AI Price Predictions:</strong> Get accurate estimates instantly.</li>
        <li>🔔 <strong>Price Alerts:</strong> Know when prices drop.</li>
    </ul>
</div>

<div class="section">
    <h2>✨ Start Now!</h2>
    <p>
        Experience the power of <span class="highlight">Mobility</span> today and see how AI changes the mobile world.
    </p>
</div>
""", unsafe_allow_html=True)

