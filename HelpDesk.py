import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu("Help Desk", ["Home"], 
        icons=['house'], menu_icon="cast", default_index=0)
    
st.divider()    

st.title("*Help Desk - Gerenciador de Ticket")

st.divider()    

col1, col2, col3 = st.columns(3)

with col1:
    Inicio = st.button("Inicio")
    
with col2:   
    Novo = st.button("Abrir Novo Chamado")

with col3:   
    Consulta = st.button("Consultar Chamado")
    
st.divider()   

if Inicio:
    st.write("Olá3")

if Novo:
    st.write("Resuma o Problema")
    text_in = st.text_input('')
    
    st.write("Descreva o Problema")
    st.text_area('')
    
    uploaded_files = st.file_uploader("Upload da Imagem", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
    
    col4, col5 = st.columns(2)
    with col4:
        st.button("Enviar")
    with col5:  
        st.button("Cancelar")

if Consulta:
    st.write("Olá2")

