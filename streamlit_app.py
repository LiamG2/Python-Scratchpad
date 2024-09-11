import streamlit as st
from streamlit_lottie import st_lottie


# img_kitajom = Image.open("image_assets/KitaJombanner.png")
# with st.echo():
    # st_lottie("kzrdAgrilI.json", height = 250, key="polyfox")

lottie_streamlit = load_lottiefile("kzrdAgrilI.json")

st.title("🎈 My new app")

st_lottie(lottie_streamlit)

st.write(
    "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
