
import streamlit as st

# Set page config
st.set_page_config(
    page_title="SnackGPT",
    page_icon="🍿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cleaned and complete CSS block
st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');

    html, body, [data-testid="stAppViewContainer"], .center-wrapper {
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #ffd1dc 0%, #ffe0b2 100%);
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
        height: 100%;
        margin: 0;
        padding: 0;
        text-align: center;
    }

    .center-wrapper {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 10vh;
    }

    .stTextInput > div > input {
        background-color: #fffaf7;
        color: white;
        border-radius: 8px;
        border: 1px solid #f8c4c4;
    }

    .stTextInput > div > input:focus {
        border: 1px solid #ffb6b9 !important;
        outline: none !important;
        box-shadow: 0 0 0 0.15rem rgba(255, 182, 185, 0.5);
    }

    .stButton>button {
        background-color: #ffb6b9;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #fa929b;
    }

    .e1nzilvr5 { visibility: hidden; }
    </style>
''', unsafe_allow_html=True)

# Start center wrapper
st.markdown('<div class="center-wrapper">', unsafe_allow_html=True)

# Title
st.markdown("<h1 style=\"color:white; text-align:center;\">Snack to Calorie Agent</h1>", unsafe_allow_html=True)

# Description
st.markdown("<p style=\"color:white; text-align:center; font-size:18px;\">Enter a snack to find out how many calories it contains.</p>", unsafe_allow_html=True)

# Input field
snack = st.text_input("👀", placeholder="e.g., banana, Fairlife protein shake")

# Reasoning agent - local snack-to-calorie logic
snack_calories = {
    "fairlife protein shake": 150,
    "banana": 105,
    "3 chocolate chip cookies": 160,
    "handful of cashews": 157,
    "slice of pizza": 285
}

def get_calories(snack_query):
    snack_query = snack_query.strip().lower()
    return snack_calories.get(snack_query, None)

# Output logic
if snack:
    calories = get_calories(snack)
    if calories:
        st.success(f"That snack has approximately {calories} calories.")
    else:
        st.warning("Sorry, I'm actually pretty dumb. You can thank Sanzana for that.")

# End center wrapper
st.markdown('</div>', unsafe_allow_html=True)
