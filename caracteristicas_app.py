import requests
import dnd_prueba
import funciones_dnd
import funciones_generales
import streamlit as st

atributos = [["Strenght" , "Dexterity"] , ["Constitution" , "Intelligence"] , ["Wisdom" , "Charisma"]]
columnas = ["col1" , "col2" , "col3"]
contador = 0
for col , atributo in zip(columnas , atributos):
    col = [col , atributo]
    print(col)