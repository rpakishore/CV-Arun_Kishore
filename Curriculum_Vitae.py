#!/usr/bin/env python
# coding: utf-8
# https://github.com/mehulgupta2016154/portfolio_builder
import streamlit as st

from portfolio import (
        about_me, career_timeline, github, 
        research, certifications, footer, sidebar, html )


# <!------ Page Configs ------>
st.set_page_config(page_title='Arun Kishore\'s portfolio',layout="wide",page_icon='👨‍🔬',initial_sidebar_state="expanded")

##Custom Fonts
st.markdown(html.CUSTOM_FONT,unsafe_allow_html=True)
## General Style
st.markdown(html.HIDE_ST_STYLE,unsafe_allow_html = True) 
st.markdown(html.PADDING_CSS,unsafe_allow_html = True) 

# <!------ Side bar Items ------>
sidebar.main()

# <!------ Title ------->
st.markdown("""
            <h1 style='text-align: center;'>
                Arun's Portfolio
            </h1>
            """,unsafe_allow_html = True) 

# <!------ About Me Section ------>
about_me.main()

# <!------ Career Timeline ------>
career_timeline.main()

# <!------ Featured Public Github Projects ------>
github.main()

# <!------ Research Papers ------>
research.main()

# <!------ Certifications ------>
certifications.main()

# <!------ Footer ------>
footer.main()
