import requests
import funciones_dnd
import streamlit as st

#corroborar con la funcion isalpha() si el dato es texto
def pedir_dato_string(texto):
    dato = st.text_input(texto)
    while dato.isalpha() != True:
        st.error
        dato = st.text_input("Por favor, ingrese un texto válido: ")
    return dato

def pedir_dato_num_positivo(texto):
    dato = input(texto)
    while dato.isnumeric() != True or int(dato) < 1:
        dato = input("Por favor, ingrese un número válido")
    return dato

def devolver_lista_de_diccionario(diccionario):
    lista_return = []
    for item in diccionario:
        lista_return.append(item)
    return lista_return