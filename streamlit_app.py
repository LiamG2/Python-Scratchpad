import streamlit as st
from streamlit_lottie import st_lottie


lottie_polyfox_1 = "https://raw.githubusercontent.com/LiamG2/Python-Scratchpad/main/kzrdAgrilI.json"

st.sidebar.title("Sidebar Title")
st.sidebar.header("Sidebar Header")

with st.sidebar: # method for adding widgets to sidebar
    st_lottie(lottie_polyfox_1, height = 100, key="polyfox_1")
    # note different 'key' name above, needed when using same animation multiple times


st.title("🎈 Much longer title of My new app")
st.radio("", [0], help='Select a number out of 3 choices')

# Tooltips also support markdown
radio_markdown = '''
Select a number, you have **3** choices!
'''.strip()

st.header('Tooltips with Markdown')
st.radio("Pick a number", [1, 2, 3], help=radio_markdown)




st.write("................................................................................ testing 2 column layoutt")

# prep for [any-num] column layout
col1, col2 = st.columns(2)

# initiate 1st column
with col1:
    st.write("Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
    st_lottie(lottie_polyfox_1, height = 100, key="polyfox_2") 
    # note different 'key' name above, needed when using same animation multiple times
    
# initiate 2nd column
with col2:
    st.write("Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
    st_lottie(lottie_polyfox_1, height = 100, key="polyfox_3")
    # note different 'key' name above, needed when using same animation multiple times
