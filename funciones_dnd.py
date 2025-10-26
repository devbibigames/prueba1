import requests


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
