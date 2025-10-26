import streamlit as st
import funciones_dnd
import funciones_generales
import dnd_prueba
from PIL import Image


st.set_page_config(page_title="Creación de hoja de personaje" , initial_sidebar_state="collapsed") 
def main ():
    
    st.title("Creando hoja de personaje")
    
    player_name = st.text_input("Nombre del jugador")
    character_name = st.text_input("Nombre del personaje")
    character_last_name = st.text_input("Apellido del personaje")
    character_race = st.selectbox("Elija una raza:" , dnd_prueba.list_races)
    character_race = st.multiselect("Elija una clase:", dnd_prueba.list_classes)
    st.sidebar.title("NAVEGACIÓN")
    
main ()