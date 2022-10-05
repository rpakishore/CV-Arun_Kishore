#!/usr/bin/env python
# coding: utf-8
# https://github.com/mehulgupta2016154/portfolio_builder
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline

st.set_page_config(page_title='Arun Kishore\'s portfolio' ,layout="wide",page_icon='👨‍🔬')

embed_component = {
    "linkedin":'<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="rpakishore" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ca.linkedin.com/in/rpakishore?trk=profile-badge">Arun Kishore</a></div>'
}

with st.sidebar:
        components.html(embed_component['linkedin'],height=310)

st.subheader('Summary')

st.write("""
         Structural E.I.T with 6+ years of professional experience looking out ...
         """)

st.subheader('Career snapshot')
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

# st.components.v1.html("""
# <h3 style="font-family:courier;">Created by</h3>
# <p style="font-family:courier;">
# Arun Kishore<br>
# Structural EIT,<br>
# Associated Engineering,<br>
# <a href="mailto:rpakishore@gmail.com">Mail</a> • <a href="https://www.linkedin.com/in/rpakishore/">LinkedIn</a><br>
# version: 1.1
# </p>
# """)