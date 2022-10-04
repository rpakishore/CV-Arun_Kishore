import streamlit as st
import os
from streamlit_timeline import timeline
st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: rpakishore@gmail.com')
pdfFileObj = open(os.path.join('assets','Resume-Arun_Kishore.pdf'), 'rb')
st.sidebar.download_button('Download Resume',pdfFileObj,file_name='Resume-Arun_Kishore.pdf',mime='pdf')

with open(os.path.join('assets','timeline-test.json'), "r", encoding="utf-8") as f: 
       data = f.read()        
timeline(data, height=800)
