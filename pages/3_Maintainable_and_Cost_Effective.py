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
st.title("Maintainable and Cost Effective")

st.image("./assets/pitch/streamlit-vs-nextjs.png")
