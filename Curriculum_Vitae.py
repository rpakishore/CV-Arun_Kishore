#!/usr/bin/env python
# coding: utf-8
# https://github.com/mehulgupta2016154/portfolio_builder
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import os

st.set_page_config(page_title='Arun Kishore\'s portfolio' ,layout="wide",page_icon='👨‍🔬')

embed_component = {
    "linkedin":'<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="rpakishore" data-version="v1"></div>'
}

with st.sidebar:
        components.html(embed_component['linkedin'],height=310)

with st.expander("About Me"):
    st.write("""
            > “Dream to reach infinity, Dare to go beyond”\n is one lucid line I experience resonating in my mind the most. A yearning appetite to better myself by inculcating new skills and acquiring new knowledge has been the recipe to my motivation. At the same time, the exhilaration in successfully conquering a challenge acts as the cornerstone to my passion. 

    As a structural engineer, I have developed skills in the structural design of residential, office, industrial and other high-rise commercial structures inaddition to desiging and drafting structural plans and details in Revit Structure/AutoCAD.

    Experienced with interfacing with architects and contractors, I am able to provide support and innovative solutions to structural problems on the project.

    In addition to my Master’s degree in Civil Engineering (Structural) from Georgia Institute of Technology, my familiarity with BCBC, CSA, ACI, AISC, ASCE, and IBC codes have enabled me to pass the latest Professional Engineer Licensure (PE & P.Eng.) Examination with ease.

    With an entrepreneurial spirit and practical mindset, blended with my professional experience, I intend to pursue a challenging and yet collaborative career with a steep learning curve in the domain of structural engineering.“Dream to reach infinity, Dare to go beyond” is one lucid line I experience resonating in my mind the most. A yearning appetite to better myself by inculcating new skills and acquiring new knowledge has been the recipe to my motivation. At the same time, the exhilaration in successfully conquering a challenge acts as the cornerstone to my passion. 

    As a structural engineer, I have developed skills in the structural design of residential, office, industrial and other high-rise commercial structures inaddition to desiging and drafting structural plans and details in Revit Structure/AutoCAD.

    Experienced with interfacing with architects and contractors, I am able to provide support and innovative solutions to structural problems on the project.

    In addition to my Master's degree in Civil Engineering (Structural) from Georgia Institute of Technology, my familiarity with BCBC, CSA, ACI, AISC, ASCE, and IBC codes have enabled me to pass the latest Professional Engineer Licensure (PE & P.Eng.) Examination with ease.

    With an entrepreneurial spirit and practical mindset, blended with my professional experience, I intend to pursue a challenging and yet collaborative career with a steep learning curve in the domain of structural engineering.
            """)

st.subheader('Career snapshot')
with st.spinner(text="Building line"):
    with open('timeline.json', "r", encoding="utf-8") as f:
        data = f.read()
        timeline(data, height=800)
        
st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: rpakishore@gmail.com')
pdfFileObj = open(os.path.join('assets','Resume-Arun_Kishore.pdf'), 'rb')
st.sidebar.download_button('Download Resume',pdfFileObj,file_name='Resume-Arun_Kishore.pdf',mime='pdf')

icon_size = 20
st.header("")
st.subheader("Featured Programming Projects")
left, middle, right = st.columns(3, gap="large")
middle.write("##### [Concrete Slab Design](https://github.com/rpakishore/Concrete_Slabs)")
middle.write("Python-streamlit app for the design of reinforced concrete slabs spanning over beams or walls.")
left.write("##### [Rebar Development length Calculator](https://github.com/rpakishore/Stru-Development-length)")
left.write("Python-streamlit app to calculate development lengths, per CSA A23.3-19. ")
right.write("##### [Concrete Test Results Summary Generator](https://github.com/rpakishore/Concrete_Test_Results)")



right.write("Generate summary of concrete test results from submitted result PDFs ")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                <style>
                #MainMenu{visibility: hidden;}
                footer{visibility: hidden;}
                header{visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style,unsafe_allow_html = True)  