import streamlit as st


st.markdown(
    """
    <style>
        section.stMain .block-container {
        padding-top: 1rem;
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("The Marksman Training Problem")


st.image("./assets/pitch/training-ratio.jpg", width=600)
st.image("./assets/pitch/training-accident.jpg", width=600)
