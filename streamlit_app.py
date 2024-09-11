import streamlit as st
from streamlit_lottie import st_lottie


# img_kitajom = Image.open("image_assets/KitaJombanner.png")
# with st.echo():
    # st_lottie("kzrdAgrilI.json", height = 250, key="polyfox")



st.title("🎈 My new app")

st_lottie("https://lottie.host/f8f6abbe-7797-48cb-9d72-e3f006de0987/kzrdAgrilI.json")

st.write(
    "Let's start building!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
