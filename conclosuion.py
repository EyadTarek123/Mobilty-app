import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
st.set_page_config(page_title="Conclusion Page", layout="wide")

st.sidebar.markdown("<h2 style='color: #2ecc71;'>Adjust Settings:</h2>", unsafe_allow_html=True)
brightness = st.sidebar.slider('Screen Brightness', 50, 100, 75)
contrast = st.sidebar.slider('Screen Contrast', 50, 150, 100)
theme = st.sidebar.selectbox('Theme Color', ['Light', 'Dark', 'Blue'])

lottie_url_conclusion = "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json"  
lottie_conclusion = load_lottieurl(lottie_url_conclusion)

lottie_url_success = "https://assets2.lottiefiles.com/packages/lf20_iwmd6pyr.json"
lottie_success = load_lottieurl(lottie_url_success)

lottie_url_team = "https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json"  
lottie_team = load_lottieurl(lottie_url_team)


if lottie_conclusion:
    st_lottie(lottie_conclusion, height=300)
else:
    st.error("Failed to load conclusion animation.")


st.markdown("""
    <div class="conclusion-section">
        <h1 class="custom-title">Thank You for Being a Part of Mobility!</h1>
        <p class="conclusion-text">
            Mobility was created with a vision to transform how people shop for mobile devices. 
            We harness the power of AI to predict mobile prices and provide users with invaluable insights.
            Your journey with Mobility reflects your passion for technology, and we’re thrilled to have you along for the ride.
        </p>
        <p class="conclusion-highlight">This is not the end, but a new beginning!</p>
    </div>
""", unsafe_allow_html=True)


if lottie_success:
    st_lottie(lottie_success, height=300)
else:
    st.error("Failed to load success animation.")


st.markdown("""
    <div class="conclusion-section">
        <h2 class="custom-subtitle">The Future of Smart Shopping</h2>
        <p class="conclusion-text">
            Mobility isn't just a platform; it's a movement towards smarter, more efficient shopping. 
            We aim to provide users with accurate data and predictions, so they can make well-informed decisions when purchasing mobile devices.
        </p>
        <p class="conclusion-text">
            As we move forward, we continue to push boundaries and explore new ways to bring value to our users. 
            The future of Mobility is brighter than ever.
        </p>
        <p class="conclusion-highlight">Stay tuned for more amazing updates and innovations!</p>
    </div>
""", unsafe_allow_html=True)


if lottie_team:
    st_lottie(lottie_team, height=300)
else:
    st.error("Failed to load team animation.")


st.markdown('<h2 class="custom-subtitle">Meet the Team Behind Mobility</h2>', unsafe_allow_html=True)

team_col1, team_col2, team_col3, team_col4 = st.columns(4)
with team_col3:
    # st.image("eyadd.jpeg", width=150)
    st.markdown('<p class="team-name">Eyad</p>', unsafe_allow_html=True)
    st.markdown('<p class="team-role">Model Creator</p>', unsafe_allow_html=True)



st.markdown("""
    <div class="conclusion-section">
        <h2 class="custom-subtitle">Our Final Words</h2>
        <p class="conclusion-text">
            Mobility is committed to making your mobile shopping experience as seamless as possible. 
            With the help of advanced technologies and the dedication of our passionate team, we’ve brought a tool that’s easy to use and filled with valuable insights.
        </p>
        <p class="conclusion-text">
            We appreciate your trust in us and look forward to making more technological advancements in the future. 
            Thank you for being part of our journey, and we hope you continue to explore, learn, and grow with Mobility.
        </p>
        <p class="conclusion-highlight">Keep Exploring, Keep Innovating!</p>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
    .custom-title {
        color: #2C3E50;
        font-size: 3em;
        text-align: center;
        animation: glow 1s ease-in-out infinite alternate;
    }

    .custom-subtitle {
        color: #16A085;
        font-size: 2em;
        margin-bottom: 1em;
        text-align: center;
        animation: pulse 1s ease-in-out infinite alternate;
    }

    .conclusion-section {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        animation: fadeIn 2s ease-in-out;
    }

    .conclusion-text {
        color: #34495E;
        font-size: 1.25em;
        margin-bottom: 1em;
    }

    .conclusion-highlight {
        color: #E74C3C;
        font-size: 1.5em;
        font-weight: bold;
        text-align: center;
    }

    .team-name {
        font-size: 1.2em;
        font-weight: bold;
        text-align: center;
    }

    .team-role {
        font-size: 1em;
        color: #7F8C8D;
        text-align: center;
    }

    @keyframes glow {
        from {
            text-shadow: 0 0 10px #f39c12, 0 0 20px #e74c3c, 0 0 30px #e74c3c;
        }
        to {
            text-shadow: 0 0 20px #f39c12, 0 0 30px #e74c3c, 0 0 40px #e74c3c;
        }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

st.write("Thanks for using our app!")

