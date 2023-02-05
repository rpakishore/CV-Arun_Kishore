import streamlit as st

FOOTER="""
<style>
  a:link , a:visited{
    color: #fe2b4b;
    background-color: transparent;
    text-decoration: underline;
  }
  a:hover,  a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
  }
  .footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: black;
    color: #f0f2f6;
    text-align: center;
  }
</style>
<div class="footer">
  <p style="font-family:'PT Serif';">Developed by 
    <a href="https://linkedin.com/in/rpakishore" target="_blank">Arun Kishore
    </a>
    <br> ⬅ See side bar for Résumé and contact information
  </p>
</div>
"""
SIDEBAR_FOOTER = """
<div class="footer">
  <p style="font-family:'PT Serif';">
    </br>
    </br>
  </p>
</div>
"""

def main():
    st.markdown(FOOTER,unsafe_allow_html=True)
    #st.sidebar.markdown(SIDEBAR_FOOTER,unsafe_allow_html=True)