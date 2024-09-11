import streamlit as st
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_streamlit = load_lottiefile("/kzrdAgrilI.json")

st.title("🎈 My new app")

st_lottie(lottie_streamlit)

st.write(
    "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
