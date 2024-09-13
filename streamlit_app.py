import streamlit as st
from streamlit_lottie import st_lottie

'''
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
'''

lottie_polyfox_1 = "https://raw.githubusercontent.com/LiamG2/Python-Scratchpad/main/kzrdAgrilI.json"
# lottie_polyfox_2 = "https://raw.githubusercontent.com/LiamG2/Python-Scratchpad/main/kzrdAgrilI.json"

st.sidebar.header("Sidebar Title")

st.title("🎈 Much longer title of My new app")

st.write("................................................................................ testing 2 column layoutt")

# prep for [any-num] column layout
col1, col2 = st.columns(2)

# initiate 1st column
with col1:
    st.write("Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
    st_lottie(lottie_polyfox_1, height = 100, key="polyfox_1")
    
# initiate 2nd column
with col2:
    st.write("Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
    st_lottie(lottie_polyfox_1, height = 100, key="polyfox_2")

# with col2:
    # st_lottie(lottie_polyfox, height = 250, key="polyfox")
