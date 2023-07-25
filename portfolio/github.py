import streamlit as st
from streamlit_card import card
def main():
    st.subheader("Featured Programming Projects")
    card(
        title="Engineering Calculators",
        text="Empowering Engineers Globally: Explore Simplified Structural Calculators for Smarter Designs.",
        image="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/struct_work_screencap.png",
        url="https://struct.work",
    )
    left, middle, right = st.columns(3, gap="large")
    with left:
        # left.write("##### [Rebar Development length Calculator](https://github.com/rpakishore/Stru-Development-length)")
        # left.write("Python-streamlit app to calculate development lengths, per CSA A23.3-19. ")
        card(
            title="Rebar Development length Calculator",
            text="Python-streamlit app to calculate development lengths, per CSA A23.3-19.",
            image="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/dev_length_screencap.png",
            url="https://general.struct.work/Development_length",
        )

    with middle:
        # middle.write("##### [Concrete Slab Design](https://github.com/rpakishore/Concrete_Slabs)")
        # middle.write("Python-streamlit app for the design of reinforced concrete slabs spanning over beams or walls.")
        card(
            title="Seismic Design of Rectangular Liquid Containing Structures",
            text="Based on ACI-350.3-06",
            image="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/seismic_tank_screencap.png",
            url="https://loadings.struct.work/Rect_Tank-Seismic",
        )
    with right:
        # right.write("##### [Concrete Test Results Summary Generator](https://github.com/rpakishore/Concrete_Test_Results)")
        # right.write("Generate summary of concrete test results from submitted result PDFs ")
        card(
            title="Concrete Test Results Summary Generator",
            text="Generate summary of concrete test results from submitted result PDFs",
            image="https://raw.githubusercontent.com/rpakishore/CV-Arun_Kishore/main/assets/concrete_test_results.png",
            url="https://github.com/rpakishore/Concrete_Test_Results",
        )
    st.divider()