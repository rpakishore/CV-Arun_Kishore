import streamlit as st
from portfolio.html import FOOTER, HIDE_ST_STYLE

def main():
    st.markdown(FOOTER,unsafe_allow_html=True)