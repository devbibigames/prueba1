import requests
import streamlit as st


#DEVUELVO URL CON JSON 

### Dado un ENDPOINT[key] , esta función aplica .json() , y devuelve la clave del diccionario results, que tambien es otro

def devolver_data (URL , ENDPOINTS , key):
    data = requests.get(URL + ENDPOINTS[key])
    data = data.json()
    data = data["results"]
    return data

def devolver_enumerado_lista_dic(diccionario , key):
    for index , raza in enumerate(diccionario):
        print(f"{index + 1}) {raza[key]}")

# Recorrer lista de diccionarios, tomar un dato del diccionario y su url, devolviendo ese diccionario nuevo

def devolver_dic_de_lista_dic(lista_dic , sera_key , sera_value):
    diccionario = {}
    for item in lista_dic:
        key = item[sera_key]
        value = item[sera_value]
        diccionario[key] = value
    return diccionario



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