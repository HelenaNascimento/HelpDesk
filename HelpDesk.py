import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import sqlite3 as bd
import platform
import tkinter as tk
from tkinter import ttk

st.set_page_config(page_title="*Help Desk - Gerenciador de Ticket", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

# Move the SQLite connection code inside the function and return the connection
def sql_lite():
    try:
        conn = bd.connect(".\HelpDesk\banco.db", check_same_thread=False)
        c = conn.cursor()
        print("Connected to SQLite")
        return conn
    except bd.Error as error:
        print("Conexão Falhou", error)
        return None

# Function to create the Ticket table if it doesn't exist
def create_ticket_table():
    conn = sql_lite()
    with conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS Ticket (
                Titlo TEXT,
                Desc TEXT,
                Setor TEXT
            )
        ''')

# Call the function to create the table
create_ticket_table()

with st.sidebar:
    selected = option_menu("Help Desk", ["Home", "Novo Chamado", "Consultar Chamado"],
                           icons=['kanban', 'activity', "list"], menu_icon="cast", default_index=0)

st.divider()

if selected == "Home":
    st.title("*Help Desk - Gerenciador de Ticket")
    st.divider()

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        container = st.container(border=True)
        container.title("Novo")
        # Fetch data from the database and display it in the container
        conn = sql_lite()
        with conn:
            c = conn.cursor()
            c.execute("SELECT * FROM Ticket WHERE Setor = 'Novo'")
            data = c.fetchall()
            container.write(pd.DataFrame(data, columns=["Titlo", "Desc", "Setor"]))

    with col2:
        container = st.container(border=True)
        container.title("Analise")
        # Fetch data from the database and display it in the container
        conn = sql_lite()
        with conn:
            c = conn.cursor()
            c.execute("SELECT * FROM Ticket WHERE Setor = 'Analise'")
            data = c.fetchall()
            container.write(pd.DataFrame(data, columns=["Titlo", "Desc", "Setor"]))

    with col3:
        container = st.container(border=True)
        container.title("Concluído")
        # Fetch data from the database and display it in the container
        conn = sql_lite()
        with conn:
            c = conn.cursor()
            c.execute("SELECT * FROM Ticket WHERE Setor = 'Concluído'")
            data = c.fetchall()
            container.write(pd.DataFrame(data, columns=["Titlo", "Desc", "Setor"]))

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
        container.write("filename:", uploaded_file.name, icons="cloud-update")
        container.write(bytes_data)

    # Use the sql_lite function to get the connection
    conn = sql_lite()

    with conn:
        c = conn.cursor()
        # Replace os.uname() with platform.system()
        Ent = '''
            INSERT INTO Ticket (Titlo, Desc, Setor)
            VALUES (?, ?, ?)
        '''
        c.execute(Ent, (Title, Desc, "Novo"))  # Assuming the default setor is "Novo"
        conn.commit()

    def popupmsg():
        popup = tk.Tk()
        popup.wm_title(Title)
        label = ttk.Label(popup, text="Dados: Replace with the actual data", font=("Verdana", 10))
        label.pack(side='top', fill='x', pady=20)
        B1 = ttk.Button(popup, text="Enviar", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    # Use st.session_state to maintain state across button clicks
    if "cancel_button_clicked" not in st.session_state:
        st.session_state.cancel_button_clicked = False

    if st.session_state.cancel_button_clicked:
        # Clear the input fields if the "Cancelar" button is clicked
        Title = ""
        Desc = ""
        st.session_state.cancel_button_clicked = False

    container.button(label='Enviar', on_click=(popupmsg))
    st.session_state.cancel_button_clicked = container.button("Cancelar", type="primary")

if selected == "Consultar Chamado":
    st.title("*Help Desk - Gerenciador de Ticket")
    st.divider()

    st.title("Consultar Ticket")
    consulta_por = st.radio("Consultar por", ['IdTicket', 'Setor'])
    buscar = st.text_input(f'Buscar por {consulta_por}:')

    if st.button("Buscar Ticket"):
        container = st.container(border=True)
        conn = sql_lite()
        with conn:
            c = conn.cursor()
            c.execute(f"SELECT * FROM Ticket WHERE {consulta_por}=?", (buscar,))
            data = c.fetchall()
            container.write(pd.DataFrame(data, columns=["Titlo", "Desc", "Setor"]))


st.divider()

st.write("Autor: Helena Nascimento")
st.write("Ano: 2024")
