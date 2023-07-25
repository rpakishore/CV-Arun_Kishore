import streamlit as st
from pathlib import Path
from PIL import Image

BLURB = """
> “Dream to reach infinity, Dare to go beyond” 
is one lucid line I experience resonating in my mind the most. An yearning appetite to better myself by inculcating new skills and acquiring new knowledge has been the recipe to my motivation. At the same time, the exhilaration in successfully conquering a challenge acts as the cornerstone to my passion.  

As a structural engineer, I have developed skills in the structural design of residential, office, industrial and other high-rise commercial structures inaddition to desiging and drafting structural plans and details in Revit Structure/AutoCAD. 

Experienced with interfacing with architects and contractors, I am able to provide support and innovative solutions to structural problems on the project.

In addition to my Master’s degree in Civil Engineering (Structural) from Georgia Institute of Technology, my familiarity with *BCBC*, *CSA*, *ACI*, *AISC*, *ASCE*, and *IBC* codes have enabled me to pass the latest Professional Engineer Licensure (**PE** & **P.Eng.**) Examination with ease.

With an entrepreneurial spirit and practical mindset, blended with my professional experience, I intend to pursue a challenging and yet collaborative career with a steep learning curve in the domain of structural engineering.
"""

image_path = Path(__file__).parent.parent / "assets" / "headshot.png"
def main():
    st.subheader('About Me')
    left, right = st.columns([2,1])
    left.write(BLURB) 
    with right:
        st.image(Image.open(image_path))
        st.markdown("""
                    <h3 style='text-align: center;'>
                        <a href='https://linkedin.com/in/rpakishore' style='color: #31333f;'>
                            Arun Kishore
                        </a></br>
                    </h3>
                    <p style='text-align: center;'>
                        <a href="mailto:portfolio@rpakishore.co.in" style='color: #fe2b4b;'>
                            📧: portfolio@rpakishore.co.in
                        </a></br>
                        <a href="https://www.linkedin.com/in/rpakishore/">
                            Linkedin
                        </a>
                         | 
                        <a href="https://github.com/rpakishore">
                            Github
                        </a>
                    </p>
                    """, unsafe_allow_html=True)
    st.markdown("""---""") 