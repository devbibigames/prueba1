import requests
import funciones_dnd
import funciones_generales

URL = "https://www.dnd5eapi.co"

datos = requests.get(URL + "/api/2014/").json()

ENDPOINTS = datos


###     RECOLECTANDO DATA DE RAZAS       ###

races_data = funciones_dnd.devolver_data(URL , ENDPOINTS , "races")
races_data =  funciones_dnd.devolver_dic_de_lista_dic(races_data , "name" , "url")
list_races = funciones_generales.devolver_lista_de_diccionario(races_data)


###     RECOLECTANDO DATA DE CLASES       ###

classes_data = funciones_dnd.devolver_data(URL , ENDPOINTS , "classes")
classes_data = funciones_dnd.devolver_dic_de_lista_dic(classes_data , "name" , "url")
list_classes = funciones_generales.devolver_lista_de_diccionario(classes_data)

###     RECOLECTANDO DATA DE CLASES       ###

abilities_data = funciones_dnd.devolver_data(URL , ENDPOINTS , "ability-scores")
abilities_data = funciones_dnd.devolver_dic_de_lista_dic(abilities_data , "name", "url")
list_abilities = funciones_generales.devolver_lista_de_diccionario(abilities_data)
