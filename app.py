import streamlit as st

st.set_page_config("Creando tu hoja de personaje")
st.title("🧙 Creador de Hojas de Personaje D&D 5e 🗡️")

with st.sidebar:
    st.header("Puntuaciones de Habilidad")
    st.markdown("Ajusta las habilidades de tu personaje (0-30)")
    
    col_str , col_dex = st.columns(2)
    