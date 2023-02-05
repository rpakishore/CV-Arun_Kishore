import streamlit as st
from pathlib import Path


def main():
    st.subheader('Research Papers 📝')
    st.markdown('<h5>'+'Development of sugarcane bagasse ash based Portland pozzolana cement and evaluation of compatibility with superplasticizers' + '</h5>' , unsafe_allow_html=True)
    st.caption('Construction and Building Materials, Elsevier, 2014')
    with st.expander('Detailed Description'):
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

    st.markdown('<h5>'+'Effects of Corrosion Inhibitors on the Critical Chloride Threshold of Thermo-Mechanically Treated (TMT) Steel' + '</h5>' , unsafe_allow_html=True)
    st.caption('SCMT3, Japan, Aug, 2013')
    with st.expander('Detailed Description'):
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
                    paperlink = Path(__file__).parent.parent / "assets" / "SCMT-Kyoto20131.0.pdf"
                    conferencepaper = open(paperlink, 'rb')
                    st.download_button('Download paper',conferencepaper,file_name='SCMT-Kyoto20131.0.pdf',mime='pdf')
    st.markdown("""---""") 