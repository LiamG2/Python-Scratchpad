import streamlit as st
from streamlit_lottie import st_lottie


lottie_polyfox_1 = "https://raw.githubusercontent.com/LiamG2/Python-Scratchpad/main/kzrdAgrilI.json"

st.sidebar.header("Sidebar Title")

with st.sidebar: # method for adding widgets to sidebar
    st_lottie(lottie_polyfox_1, height = 100, key="polyfox")
    # note different 'key' name above, needed when using same animation multiple times

st.title("🎈 Much longer title of My new app")

st.write("................................................................................ testing 2 column layoutt")

# prep for [any-num] column layout
col1, col2 = st.columns(2)

# initiate 1st column
with col1:
    st.write("Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
    st_lottie(lottie_polyfox_1, height = 100, key="polyfox_1") 
    # note different 'key' name above, needed when using same animation multiple times
    
# initiate 2nd column
with col2:
    st.write("Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
    # st_lottie(lottie_polyfox_1, height = 100, key="polyfox_2")
    # note different 'key' name above, needed when using same animation multiple times
