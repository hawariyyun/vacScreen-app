import streamlit as st
from skrining import load_skrining
from faq import load_faqs

st.sidebar.header('paDetect COVID-19 Vaccination Screening App')
skrinOrfaq = st.sidebar.selectbox("SKRINING/FAQS", ('SKRINING', 'FAQS'))

if skrinOrfaq == 'SKRINING':
    load_skrining()
else:
    load_faqs()