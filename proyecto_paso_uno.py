import streamlit as st
import funciones_dnd
import funciones_generales
import dnd_prueba
from PIL import Image

###   CALCULA EL BONIFICADOR EN BASE AL PUNTAJE DE CARACTERISTICA  ###
def calcular_bono(base_point):
    bonus = int((base_point-10)/2)
    return bonus

###   IMPRIME EL VALOR DEL BONIFICADOR, AGREGANDOLE UN + SI ES POSITIVO  ###
def imprimir_bono(bonificador):
        if bonificador < 0:
            st.write(f"{bonificador}")
        else:
            st.write(f"+{bonificador}")



st.set_page_config(page_title="Creación de hoja de personaje") 
def main ():
    with st.container(border=True , horizontal_alignment="center"):
        basic_point_wisdom = st.slider("wisdom_sl" , min_value=5,max_value=30 , label_visibility="hidden")
        bonificador = calcular_bono(basic_point_wisdom)
        imprimir_bono(bonificador)
   
main ()

