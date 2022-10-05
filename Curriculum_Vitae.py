#!/usr/bin/env python
# coding: utf-8
# https://github.com/mehulgupta2016154/portfolio_builder
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import os

# <!------ Page Configs ------>
st.set_page_config(
        page_title='Arun Kishore\'s portfolio',
        layout="wide",
        page_icon='👨‍🔬',
        initial_sidebar_state="expanded")

# <!------ Side bar Items ------>
embed_component = {
    "linkedin":'<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="rpakishore" data-version="v1"></div>'
}
with st.sidebar:
        components.html(embed_component['linkedin'],height=310)
        st.caption('Wish to connect?')
        st.write('📧: rpakishore@gmail.com')
        pdfFileObj = open(os.path.join('assets','Resume-Arun_Kishore.pdf'), 'rb')
        st.download_button('Download Résumé',pdfFileObj,file_name='Resume-Arun_Kishore.pdf',mime='pdf')

# <!------ About Me Section ------>
st.subheader('About Me')
st.write("""
            > “Dream to reach infinity, Dare to go beyond” 
is one lucid line I experience resonating in my mind the most. An yearning appetite to better myself by inculcating new skills and acquiring new knowledge has been the recipe to my motivation. At the same time, the exhilaration in successfully conquering a challenge acts as the cornerstone to my passion.  

As a structural engineer, I have developed skills in the structural design of residential, office, industrial and other high-rise commercial structures inaddition to desiging and drafting structural plans and details in Revit Structure/AutoCAD. 

Experienced with interfacing with architects and contractors, I am able to provide support and innovative solutions to structural problems on the project.

In addition to my Master’s degree in Civil Engineering (Structural) from Georgia Institute of Technology, my familiarity with *BCBC*, *CSA*, *ACI*, *AISC*, *ASCE*, and *IBC* codes have enabled me to pass the latest Professional Engineer Licensure (**PE** & **P.Eng.**) Examination with ease.

With an entrepreneurial spirit and practical mindset, blended with my professional experience, I intend to pursue a challenging and yet collaborative career with a steep learning curve in the domain of structural engineering.
""")
st.markdown("""---""") 

# <!------ Career Timeline ------>
st.subheader('Career snapshot')
with st.spinner(text="Building line"):
    with open('timeline.json', "r", encoding="utf-8") as f:
        data = f.read()
        timeline(data, height=700)
st.markdown("""---""") 

# <!------ Featured Public Github Projects ------>
st.subheader("Featured Programming Projects")
left, middle, right = st.columns(3, gap="large")
middle.write("##### [Concrete Slab Design](https://github.com/rpakishore/Concrete_Slabs)")
middle.write("Python-streamlit app for the design of reinforced concrete slabs spanning over beams or walls.")
left.write("##### [Rebar Development length Calculator](https://github.com/rpakishore/Stru-Development-length)")
left.write("Python-streamlit app to calculate development lengths, per CSA A23.3-19. ")
right.write("##### [Concrete Test Results Summary Generator](https://github.com/rpakishore/Concrete_Test_Results)")
right.write("Generate summary of concrete test results from submitted result PDFs ")
st.markdown("""---""") 

# <!------ Research Papers ------>
st.subheader('Research Papers 📝')
st.markdown('<h5><u>'+'Development of sugarcane bagasse ash based Portland pozzolana cement and evaluation of compatibility with superplasticizers' + '</h5>' , unsafe_allow_html=True)
st.caption('Construction and Building Materials, Elsevier, 2014')
with st.expander('detailed description'):
        with st.spinner(text="Loading details..."):
                st.write("""
                #### Highlights:
                * Development of sugarcane bagasse ash based Portland pozzolana cement is reported.
                * Interaction of superplasticizers with bagasse ash based Portland pozzolana cement was studied.
                * Influence of irregular structure of silica particles on loss of fluidity is discussed.

                #### Abstract

                Sugarcane bagasse ash is a by-product from sugar industries and can be used as supplementary cementitious material in concrete.
                The development of new cementitious blends with processed sample of sugarcane bagasse ash is described in this paper.
                Utilization of various supplementary cementitious materials significantly influences fresh and hardened properties of concrete.
                Interaction of pozzolanic material with cement and chemical admixtures produces diverse effects in the fresh properties of blended cement concrete.
                This paper aims to ascertain the effect of different bagasse ash replacements of cement on the compatibility with superplasticizers in cement paste.
                Sugarcane bagasse ash based Portland pozzolana cements were produced with three different levels of replacement - 10%, 15%, and 20%. Marsh cone and mini-slump test were used to determine the effect of superplasticizer type and water binder ratio on the saturation dosage.
                From this study, it was observed that polycarboxylic ether based superplasticizer was more compatible with bagasse ash blended cement than sulphonated naphthalene based superplasticizer.
                
                ###### [Link to the Journal](https://www.sciencedirect.com/science/article/pii/S0950061814007284)

                """)

st.markdown('<h5><u>'+'Effects of Corrosion Inhibitors on the Critical Chloride Threshold of Thermo-Mechanically Treated (TMT) Steel' + '</h5>' , unsafe_allow_html=True)
st.caption('SCMT3, Japan, Aug, 2013')
with st.expander('detailed description'):
        with st.spinner(text="Loading details..."):
                st.write("""
                #### Abstract

                The critical chloride threshold (Clth) is defined as the concentration of chloride ions
                required at the surface of embedded reinforcement to initiate corrosion. This is an
                important parameter in determining the service life of reinforced concrete structures
                exposed to chloride environments. An increase in Clth indicates an increase in
                corrosion resistance and service life of structures. Now-a-days, corrosion inhibitors
                (say, calcium nitrite and bipolar inhibitors) are used to increase the corrosion
                resistance of reinforced concrete structures exposed to chloride environments.
                Nevertheless, the manufacturers recommend a wide range of dosage of corrosion
                inhibitors (e.g., 10 to 30 litres of calcium nitrite inhibitor per m3 of concrete).
                In addition, the quality control may be poor leading to a significance difference
                between the prescribed and actual concentrations of corrosion inhibitor used. Also,
                the effect of changes in the dosage of various types of corrosion inhibitors on Clth is
                not well understood. In addition, corrosion resistant steels (say, TMT steel) are also
                widely used with enhanced corrosion resistance in mind. However, very little
                information is available on the Clth of TMT steels used in India.

                This paper presents the Clth of TMT steel embedded in mortar with
                various dosages of two types of corrosion inhibitors. The experimental program used
                a recently developed accelerated chloride threshold test method in which the
                corrosion rates are measured by linear polarization resistance technique. In this test,
                the potential application and corrosion rate measurement are performed in a cyclic
                manner until the corrosion initiation occurs. After the initiation of corrosion, the test
                specimen is autopsied and the chloride concentration in the mortar adjacent to the
                steel surface is determined. This is recorded as Clth values of the embedded steel
                specimen. Using this method, the Clth of TMT steel embedded in mortar with five
                different dosages of the calcium nitrite [Ca(NO2)2] and bipolar corrosion inhibitors
                were determined. The various dosages tested are R-20%, R-10%, R%, R+10%, and
                R+20%, where R is the average dosage recommended by the manufacturer.
                """)
                conferencepaper = open(os.path.join('assets','SCMT-Kyoto20131.0.pdf'), 'rb')
                st.download_button('Download paper',conferencepaper,file_name='SCMT-Kyoto20131.0.pdf',mime='pdf')
st.markdown("""---""") 

# <!------ Footer ------>
hide_st_style = """
                <style>
                #MainMenu{visibility: hidden;}
                footer{visibility: hidden;}
                header{visibility: hidden;}
                </style>
                """

st.markdown(hide_st_style,unsafe_allow_html = True) 

footer="""<style>
a:link , a:visited{
color: blue;
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
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<hr>
<p style="font-family:Source Sans Pro;">Developed by <a href="https://linkedin.com/in/rpakishore" target="_blank">Arun Kishore</a><br> ⬅ See side bar for Résumé and contact information</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)