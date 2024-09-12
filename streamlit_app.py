import streamlit as st
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# lottie_streamlit = load_lottiefile("/kzrdAgrilI.json")
lottie_polyfox = "https://lottie.host/f8f6abbe-7797-48cb-9d72-e3f006de0987/kzrdAgrilI.json"

st.title("🎈 My new app")

st_lottie(lottie_polyfox, height = 250, key="polyfox")

st.write(
    "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
