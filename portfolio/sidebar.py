import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from portfolio.html import LINKEDIN

def table_of_contents():
    st.markdown("""
<p style="font-family: 'PT Serif'">
    <h4>Table of Contents</h4>
    <a href="#about-me">About Me</a></br>    
    <a href="#career-snapshot">Career snapshot</a></br>
    <a href="#featured-programming-projects">Featured Programming Projects</a></br>
    <a href="#research-papers">Research Papers</a></br>
    <a href="#certifications">Certifications</a>
</p>
""", unsafe_allow_html=True)

def email():
    st.markdown("""
<p style='font-size: 14px;color: #31333f';>Wish to connect?</br>
    <a href="mailto:portfolio@rpakishore.co.in">📧: portfolio@rpakishore.co.in</a>
</p>
""", unsafe_allow_html=True)
    
def linkedin():
    linkedin_embed = '<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="rpakishore" data-version="v1"></div>'
    components.html(linkedin_embed,height=300)

def resume():
    resume = Path(__file__).parent.parent / "assets" / "Resume-Arun_Kishore.pdf"
    pdfFileObj = open(resume, 'rb')
    st.download_button('Download Résumé',pdfFileObj,file_name='Resume-Arun_Kishore.pdf',mime='pdf')

def main():


    with st.sidebar:
        table_of_contents()
        email()
        resume()
        linkedin()
        
        
        
        