import streamlit as st

def main():
    st.subheader("Featured Programming Projects")
    left, middle, right = st.columns(3, gap="large")
    middle.write("##### [Concrete Slab Design](https://github.com/rpakishore/Concrete_Slabs)")
    middle.write("Python-streamlit app for the design of reinforced concrete slabs spanning over beams or walls.")
    left.write("##### [Rebar Development length Calculator](https://github.com/rpakishore/Stru-Development-length)")
    left.write("Python-streamlit app to calculate development lengths, per CSA A23.3-19. ")
    right.write("##### [Concrete Test Results Summary Generator](https://github.com/rpakishore/Concrete_Test_Results)")
    right.write("Generate summary of concrete test results from submitted result PDFs ")
    st.markdown("""---""") 