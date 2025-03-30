
import streamlit as st

# Set page config
st.set_page_config(
    page_title="SnackGPT",
    page_icon="🍿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for pastel pink-peach gradient and Partiful-style font
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');

html, body {
    font-family: 'Space Grotesk', sans-serif;
    background: linear-gradient(#ffffff, #ffd1dc 15%, #ffe0b2 100%);
    color: #2c2c2c;
    height: 100%;
    margin: 0;
    padding: 0;
}

.center-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 10vh;
    text-align: center;
}

.stTextInput > div > input {
    background-color: #fffaf7;
    color: #2c2c2c;
    border-radius: 0px;
    border: 1px solid #000000;
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
</style>""", unsafe_allow_html=True)

# Start center wrapper
st.markdown('<div class="center-wrapper">', unsafe_allow_html=True)

# Title
st.title("SnackGPT")

# Description
st.markdown("What'd you have?")

# Input field
snack = st.text_input("Tell me everything", placeholder="e.g., a banana, a Fairlife protein shake")

# Reasoning agent - local snack-to-calorie logic
snack_calories = {
    "a fairlife protein shake": 150,
    "a banana": 105,
    "a slice of pizza": 285,
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
        st.warning("Idk, I'm still pretty dumb thanks to Sanzana's poor engineering skills.")

# End center wrapper
st.markdown('</div>', unsafe_allow_html=True)
