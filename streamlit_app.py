import streamlit as st
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# lottie_streamlit = load_lottiefile("/kzrdAgrilI.json")
lottie_polyfox = "https://raw.githubusercontent.com/LiamG2/Python-Scratchpad/main/kzrdAgrilI.json"

st.title("🎈 My new app")

col1, col2 = st.columns(2)

with col1:
    st.write(
        "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )

with col2:
    st.write(
        "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )

# with col2:
    # st_lottie(lottie_polyfox, height = 250, key="polyfox")
