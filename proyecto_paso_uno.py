import streamlit as st
import funciones_dnd
import funciones_generales
import dnd_prueba
from PIL import Image


abilities_list_pares = [["Strenght" , "Dexterity"] , ["Constitution" , "Intelligence"] , ["Wisdom" , "Charisma"]]



st.set_page_config(page_title="Creación de hoja de personaje") 
st.title("Bienvenido a la creación de tu hoja de personaje")
abilities_list_pares = [["Strenght" , "Dexterity"] , ["Constitution" , "Intelligence"] , ["Wisdom" , "Charisma"]]
col1,col2,col3 = st.columns(3)
columns = [col1,col2,col3]
valores = {}
bonos = {}

def main ():
    
    for col,abilities in zip(columns,abilities_list_pares):
        with col:
            for abilitie in abilities:
                with st.container(border=True):
                    st.write(abilitie)
                    valor = st.slider(f"{abilitie}_sl" , min_value=0,max_value=30,step=1, label_visibility="hidden")
                    valores[abilitie] = valor
                    bono = funciones_dnd.calcular_bono(valor)
                    funciones_dnd.imprimir_bono(bono)
    st.write(valores)
main ()

