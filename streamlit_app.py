import streamlit as st
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# lottie_streamlit = load_lottiefile("/kzrdAgrilI.json")
lottie_polyfox = "https://raw.githubusercontent.com/LiamG2/Python-Scratchpad/main/kzrdAgrilI.json"

st.title("🎈 Much longer title of My new app")

st.write("................................................................................ testing 2 column layout")

# prep for [any-num] column layout
col1, col2 = st.columns(2)

# initiate 1st column
with col1:
    st.write(
        "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )
    
# initiate 2nd column
with col2:
    st.write(
        "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )

# with col2:
    # st_lottie(lottie_polyfox, height = 250, key="polyfox")
