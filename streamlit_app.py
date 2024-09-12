import streamlit as st
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# lottie_streamlit = load_lottiefile("/kzrdAgrilI.json")
lottie_polyfox = "https://raw.githubusercontent.com/LiamG2/Python-Scratchpad/main/kzrdAgrilI.json"

st.title("🎈 My new app")

st_lottie(lottie_polyfox, height = 250, key="polyfox")

st.write(
    "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
