import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import sqlite3 as bd #https://discuss.streamlit.io/t/streamlit-and-sqlite-update-database-by-sharing-the-web-app/26156
import tkinter as tk
from tkinter import ttk
import os 

st.set_page_config(page_title="*Help Desk - Gerenciador de Ticket", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def sql_lite(label):
    try:
        conn = bd.connect(".\HelpDesk\banco.db", check_same_thread = False)
        c = conn.cursor()
        print("Connected to SQLite")
    except bd.Error as error:
        print("Conexão Falhou", error)
        
with st.sidebar:
    selected = option_menu("Help Desk", ["Home", "Novo Chamado", "Consultar Chamado"], 
        icons=['kanban', 'activity', "list"], menu_icon="cast", default_index=0)

st.divider()   

if selected == "Home":
    
    st.title("*Help Desk - Gerenciador de Ticket", )
    st.divider()    
    
    col1, col2, col3 = st.columns(3, gap="large")
   
    with col1:
      container = st.container(border=True)
      cols = st.columns(3)
      container.title("Novo")
      container.write(pd.DataFrame({
          'Novo': [1, 2, 3],
          'Analise': [3, 2, 1],
          'Concluído': [4, 5, 6]
      }))
    
    with col2:
      container = st.container(border=True)
      container.title("Analise")
      container.write(pd.DataFrame({
          'Novo': [1, 2, 3],
          'Analise': [3, 2, 1],
          'Concluído': [4, 5, 6]
      }))
        
    with col3:
      container = st.container(border=True)
      container.title("Concluído")
      container.write(pd.DataFrame({
          'Novo': [1, 2, 3],
          'Analise': [3, 2, 1],
          'Concluído': [4, 5, 6]
      }))

if selected == "Novo Chamado":

    st.title("*Help Desk - Gerenciador de Ticket")
    st.divider()     
    container = st.container(border=True)
    container.write("Título: ")
    Title = container.text_input('')
    
    container.write("Descreva o Problema: ")
    Desc = container.text_area('')
    
    uploaded_files = container.file_uploader("Imagem: ", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        container.write("filename:", uploaded_file.name, icons = "cloud-update")
        container.write(bytes_data)
        
    NORM_FONT= ("Verdana", 10)
    
    conn = bd.connect("banco.db", check_same_thread = False)
    Ent = ('''
                        update Ticket 
                        set Titlo = ?, Desc = ? , Setor = ?''', Title, Desc, os.uname())
    c = conn.cursor()
    c.execute(Ent, conn)
    conn.commit()
    
    def popupmsg():
        popup = tk.Tk()
        popup.wm_title(Title)
        label = ttk.Label(popup, text= dados, font=NORM_FONT)
        label.pack(side='top', fill='x', pady=20)
        B1 = ttk.Button(popup, text="Enviar", command= popup.destroy)
        B1.pack()
        popup.mainloop()
    
    container.button(label='Enviar', on_click=(popupmsg))


    container.button("Cancelar", type="primary")
    

   
    
    
            
if selected == "Consultar Chamado":
    
    st.title("*Help Desk - Gerenciador de Ticket")
    st.divider()    
    
    st.title("Consultar Ticket")
    st.radio("Consultar por", 
            ['IdTicket', 'Setor'])
    buscar = st.text_input('')
    

    
    st.button("Buscar")
    container = st.container(border=True)
    container.write("Olá1")
    container.write("Olá2")
    container.write("Olá3")
    container.write("Olá4")
    container.write("Olá5")
    container.write("Olá6")
    container.write("Olá7")
    container.write("Olá8")
    container.write("Olá9")
    container.write("Olá10")
    container.write("Olá11")
    container.write("Olá12")
    container.write("Olá13")
    container.write("Olá14")
    

   
st.divider()   

st.write("Autor: Helena Nascimento")
st.write("Ano: 2024")
    

