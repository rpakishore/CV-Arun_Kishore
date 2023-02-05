import streamlit as st
from PIL import Image
from pathlib import Path

def main():
    st.subheader('Certifications 📜')
    left,right = st.columns(2)

    with left:
        st.markdown('<h5><u>'+'Fall Protection Training' + '</h5>' , unsafe_allow_html=True)
        st.caption('ENVIROSAFETY, Sept. 2022')
        st.caption('Certification ID# FP5996931')
        with st.expander('Show Certificate'):
            img = Path(__file__).parent.parent / "assets" / "Arun_Kishore_FallProtection8Hours_26-Sep-2022.jpg"
            image = Image.open(img)
            st.image(image, caption='Fall Protection Training Certificate')

    with right:
        st.markdown('<h5><u>'+'Confined Space Entry' + '</h5>' , unsafe_allow_html=True)
        st.caption('ENVIROSAFETY, Oct. 2022')
        st.caption('Certification ID# CSE6022025')
        with st.expander('Show Certificate'):
            img = Path(__file__).parent.parent / "assets" / "Arun_Kishore_CSEConfinedSpaceEntryStandbyAttendantNonentryRescue8H_03-Oct-2022.jpg"
            image = Image.open(img)
            st.image(image, caption='Fall Protection Training Certificate')
    st.markdown("""---""") 