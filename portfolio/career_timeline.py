import streamlit as st
from streamlit_timeline import timeline
from pathlib import Path

def main():
    st.subheader('Career snapshot')
    with st.spinner(text="Building line"):
        timeline_path = Path(__file__).parent / "timeline.json"
        with open(timeline_path, "r", encoding="utf-8") as f:
            data = f.read()
            timeline(data, height=900)
    st.markdown("""---""") 