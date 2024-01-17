import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu("Help Desk", ["Home"], 
        icons=['house'], menu_icon="cast", default_index=0)
    
if selected == "Home":
    st.button("Abri Novo Chamado")
    st.button("Consultar Chamado")
