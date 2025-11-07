import streamlit as st

st.set_page_config("Creando tu hoja de personaje")
st.title("🧙 Creador de Hojas de Personaje D&D 5e 🗡️")

with st.sidebar:
    st.header("Puntuaciones de Habilidad")
    st.markdown("Ajusta las habilidades de tu personaje (0-30)")
    
    col_str , col_dex = st.columns(2)
    col_con , col_int = st.columns(2)
    col_wis , col_cha = st.columns(2)

columnas_habilidades = {"Fuerza" : col_str, "Destreza": col_dex , "Constitución" : col_con , "Inteligencia" : col_int ,
                        "Sabiduría" : col_wis , "Carisma" : col_cha}

for habilidad in columnas_habilidades:
    with columnas_habilidades[habilidad]:
        valor = st.slider(f"{habilidad}" , 1 , 30 , 10 , key= f"sl{habilidad}" , help=f"Puntuación base de: {habilidad}")
        #CALCULAR BONO
