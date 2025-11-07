import streamlit as st
from PIL import Image
import base64

# --- Funciones de Placeholder para la UI (El usuario se encargará de la lógica real) ---
# Estas funciones permiten que la interfaz se ejecute sin los módulos externos.
def calcular_bono(valor):
    """Calcula el modificador de habilidad simple."""
    return (valor - 10) // 2

def bono_a_texto(bono):
    """Formatea el bono como texto (+X o -X)."""
    return f"+{bono}" if bono >= 0 else str(bono)

# La función para simular la exportación a PDF
def exportar_a_pdf(datos):
    """Simula la exportación y genera un archivo de texto con los datos."""
    # Aquí iría la lógica de tu librería de generación de PDF
    st.session_state.pdf_content = f"--- Contenido de la Hoja de Personaje ---\n\n"
    for key, value in datos.items():
        st.session_state.pdf_content += f"{key}: {value}\n"
    st.session_state.pdf_export_ready = True
    st.success("¡Personaje listo para exportar! (Simulación de exportación completa)")

# --- Configuración de la Página y Título ---
st.set_page_config(page_title="Creación de Personaje D&D 5e", layout="wide", initial_sidebar_state="expanded")
st.title("🧙 Creador de Hojas de Personaje D&D 5e 🗡️")

# --- Inicialización de Session State para almacenar los datos del personaje ---
if 'character_data' not in st.session_state:
    st.session_state.character_data = {}
if 'pdf_export_ready' not in st.session_state:
    st.session_state.pdf_export_ready = False
if 'pdf_content' not in st.session_state:
    st.session_state.pdf_content = ""

# --- Definiciones de Listas ---
ABILITIES_LIST = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma"]
SKILLS_LIST = [
    ("Acrobacias", "Destreza"), ("Juego", "Carisma"), ("Atletismo", "Fuerza"),
    ("Engaño", "Carisma"), ("Historia", "Inteligencia"), ("Perspicacia", "Sabiduría"),
    ("Intimidación", "Carisma"), ("Investigación", "Inteligencia"), ("Medicina", "Sabiduría"),
    ("Naturaleza", "Inteligencia"), ("Percepción", "Sabiduría"), ("Interpretación", "Carisma"),
    ("Persuasión", "Carisma"), ("Religión", "Inteligencia"), ("Juego de Manos", "Destreza"),
    ("Sigilo", "Destreza"), ("Supervivencia", "Sabiduría"), ("Trato con Animales", "Sabiduría")
]
ALIGNMENTS = ["Legal Bueno", "Neutral Bueno", "Caótico Bueno", "Legal Neutral", "Neutral", "Caótico Neutral", "Legal Malvado", "Neutral Malvado", "Caótico Malvado"]
CLASSES = ["Bárbaro", "Bardo", "Clérigo", "Druida", "Guerrero", "Monje", "Paladín", "Explorador", "Pícaro", "Hechicero", "Brujo", "Mago"]
RACES = ["Humano", "Elfo", "Enano", "Mediano", "Tiefling", "Dragonborn", "Gnomo", "Semielfo", "Semiorco"]

# --- Sidebar para Puntuaciones de Habilidad (Pilar Central) ---
with st.sidebar:
    st.header("Puntuaciones de Habilidad")
    st.markdown("Ajusta las habilidades de tu personaje (0-30)")
    
    col_str, col_dex = st.columns(2)
    col_con, col_int = st.columns(2)
    col_wis, col_cha = st.columns(2)
    
    abilities_cols = {
        "Fuerza": col_str, "Destreza": col_dex,
        "Constitución": col_con, "Inteligencia": col_int,
        "Sabiduría": col_wis, "Carisma": col_cha,
    }

    # Inicializar y mostrar sliders
    for ability in ABILITIES_LIST:
        with abilities_cols[ability]:
            valor = st.slider(f"{ability}", 1, 30, 10, key=f"sl_{ability}", help=f"Puntuación base de {ability}")
            bono = calcular_bono(valor)
            
            # Mostrar la tarjeta de habilidad
            st.markdown(
                f"""
                <div style="background-color: #1f2937; border-radius: 8px; padding: 10px; margin-bottom: 10px; text-align: center; color: white;">
                    <p style="font-size: 1.25rem; font-weight: bold; margin: 0;">{bono_a_texto(bono)}</p>
                    <p style="font-size: 0.75rem; color: #9ca3af; margin: 0;">{ability.upper()}</p>
                </div>
                """, unsafe_allow_html=True
            )
            # Guardar en el estado para uso posterior
            st.session_state.character_data[ability] = valor
            st.session_state.character_data[f"Bono_{ability}"] = bono

# --- Lógica de la Interfaz Principal (Tabs) ---

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📜 Info Básica", 
    "🛡️ Combate", 
    "🎯 Habilidades", 
    "🎒 Rasgos y Equipo", 
    "📥 Exportar"
])

# =================================================================
# TAB 1: Información Básica y Características Generales
# =================================================================
with tab1:
    st.header("Información Esencial del Personaje")
    
    # Fila de Nombre y Clase/Nivel
    col_name, col_clase_lvl = st.columns([2, 1])
    with col_name:
        st.session_state.character_data["Nombre"] = st.text_input("Nombre del Personaje", "Borin Peñadura")
    with col_clase_lvl:
        col_clase, col_lvl = st.columns(2)
        with col_clase:
            st.session_state.character_data["Clase"] = st.selectbox("Clase", CLASSES, index=4)
        with col_lvl:
            st.session_state.character_data["Nivel"] = st.number_input("Nivel", 1, 20, 1)

    # Fila de Raza, Fondo y Alineamiento
    col_raza, col_fondo, col_alineamiento = st.columns(3)
    with col_raza:
        st.session_state.character_data["Raza"] = st.selectbox("Raza", RACES, index=2)
    with col_fondo:
        st.session_state.character_data["Fondo"] = st.text_input("Fondo (Ej: Soldado, Sabio)", "Ermitaño")
    with col_alineamiento:
        st.session_state.character_data["Alineamiento"] = st.selectbox("Alineamiento", ALIGNMENTS, index=0)

    st.subheader("Otras Características")
    
    col_otros1, col_otros2 = st.columns(2)
    with col_otros1:
        st.session_state.character_data["Puntos_Exp"] = st.number_input("Puntos de Experiencia (PX)", 0, 1000000, 0)
        st.session_state.character_data["Idiomas"] = st.text_area("Idiomas y Otros (Separa con comas)", "Común, Enano")
    with col_otros2:
        try:
            image = Image.open("dnd_logo_placeholder.png") # Simula cargar una imagen de personaje
            st.image(image, caption="Retrato del Personaje", use_column_width=True)
        except:
             # Placeholder simple si la imagen no existe
             st.markdown('<div style="height: 200px; background-color: #4a5568; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white;"> Placeholder de Retrato</div>', unsafe_allow_html=True)
        

# =================================================================
# TAB 2: Combate y Defensa
# =================================================================
with tab2:
    st.header("Estadísticas de Combate")

    # Calculadora de Bono de Competencia (PB)
    pb = (st.session_state.character_data.get("Nivel", 1) - 1) // 4 + 2
    st.session_state.character_data["Bono_Competencia"] = pb
    st.info(f"**Bono de Competencia (PB):** **+{pb}**")

    col_ac, col_in, col_vel = st.columns(3)
    with col_ac:
        ac = st.number_input("Clase de Armadura (CA)", 1, 30, 10 + st.session_state.character_data.get("Bono_Destreza", 0))
        st.session_state.character_data["CA"] = ac
    with col_in:
        ini = st.session_state.character_data.get("Bono_Destreza", 0)
        st.session_state.character_data["Iniciativa"] = ini
        st.metric("Iniciativa", bono_a_texto(ini))
    with col_vel:
        st.session_state.character_data["Velocidad"] = st.number_input("Velocidad (ft)", 5, 100, 30)
    
    st.subheader("Puntos de Golpe (HP)")
    col_hp_max, col_hp_curr, col_hp_temp, col_dados = st.columns(4)
    
    with col_hp_max:
        st.session_state.character_data["Max_HP"] = st.number_input("HP Máximos", 1, 500, 10)
    with col_hp_curr:
        st.session_state.character_data["Current_HP"] = st.number_input("HP Actuales", 0, st.session_state.character_data.get("Max_HP", 10), st.session_state.character_data.get("Max_HP", 10))
    with col_hp_temp:
        st.session_state.character_data["Temp_HP"] = st.number_input("HP Temporales", 0, 500, 0)
    with col_dados:
        st.session_state.character_data["Dados_Golpe"] = st.text_input("Dados de Golpe", "1d8")

    st.subheader("Tiradas de Salvación y Ataques")

    col_salv, col_ataques = st.columns([1, 2])
    
    with col_salv:
        st.markdown("**Tiradas de Salvación**")
        for ability in ABILITIES_LIST:
            # Checkbox para seleccionar competencia en la tirada de salvación
            is_proficient = st.checkbox(f"Comp. en {ability}", key=f"prof_save_{ability}")
            base_bono = st.session_state.character_data.get(f"Bono_{ability}", 0)
            final_bono = base_bono + (pb if is_proficient else 0)
            
            st.session_state.character_data[f"Salv_{ability}"] = final_bono
            st.metric(f"Sal. {ability}", bono_a_texto(final_bono))

    with col_ataques:
        st.markdown("**Ataques y Lanzamiento de Conjuros**")
        # Usamos un expander para una lista de ataques con más detalle
        with st.expander("Ataques/Conjuros", expanded=True):
            for i in range(1, 4):
                st.markdown(f"**Ataque {i}**")
                col_n, col_b, col_d = st.columns(3)
                with col_n:
                    st.text_input(f"Nombre (Ataque {i})", f"Espada Larga {i}", key=f"att_name_{i}")
                with col_b:
                    st.text_input(f"Bono (Ataque {i})", "+4", key=f"att_bonus_{i}")
                with col_d:
                    st.text_input(f"Daño (Ataque {i})", "1d8 + 2", key=f"att_damage_{i}")
            
        st.session_state.character_data["Descripcion_Ataques"] = st.text_area("Notas sobre Conjuros/Ataques", "CD de conjuros: 12. Bono de ataque de conjuro: +4.")

# =================================================================
# TAB 3: Habilidades y Percepción
# =================================================================
with tab3:
    st.header("Habilidades (Skills) y Competencia")
    
    col_main, col_passive = st.columns([2, 1])

    with col_main:
        st.markdown("---")
        # Mostrar las 18 habilidades en una cuadrícula
        for i, (skill_name, ability) in enumerate(SKILLS_LIST):
            # Usar 3 columnas para el diseño
            if i % 3 == 0:
                col_a, col_b, col_c = st.columns(3)
            
            # Alternar la columna para cada habilidad
            current_col = [col_a, col_b, col_c][i % 3]

            with current_col:
                with st.container(border=True):
                    # Checkbox para competencia
                    is_proficient = st.checkbox(f"**{skill_name}** ({ability[:3]})", key=f"prof_skill_{skill_name}")
                    
                    # Cálculo del bono
                    base_bono = st.session_state.character_data.get(f"Bono_{ability}", 0)
                    final_bono = base_bono + (pb if is_proficient else 0)
                    
                    st.session_state.character_data[f"Skill_{skill_name}"] = final_bono
                    
                    st.markdown(f"**Bono:** `{bono_a_texto(final_bono)}`")

    with col_passive:
        st.subheader("Percepción Pasiva")
        # Calcular Percepción Pasiva (10 + Bono de Percepción)
        
        # Buscar el bono de Percepción (Skill_Percepción) en el estado. Si no existe, usar el bono de Sabiduría.
        perception_skill_bono = st.session_state.character_data.get("Skill_Percepción", 
                                                10 + st.session_state.character_data.get("Bono_Sabiduría", 0))
        
        passive_perception = 10 + perception_skill_bono
        st.session_state.character_data["Pasiva_Percepcion"] = passive_perception
        
        st.metric("Puntuación", passive_perception, delta="10 + Bono de Percepción")
        st.markdown("---")

        st.subheader("Otros Sentidos Pasivos")
        st.session_state.character_data["Pasiva_Investigacion"] = st.number_input("Investigación Pasiva", 1, 30, 10)
        st.session_state.character_data["Pasiva_Perspicacia"] = st.number_input("Perspicacia Pasiva", 1, 30, 10)

# =================================================================
# TAB 4: Rasgos y Equipo
# =================================================================
with tab4:
    st.header("Rasgos, Trasfondo y Equipo")
    
    col_traits, col_features = st.columns(2)

    with col_traits:
        st.subheader("Rasgos de Personalidad")
        st.session_state.character_data["Personalidad"] = st.text_area("Personalidad (Aspiraciones, manías)", "Soy desconfiado y siempre busco la verdad detrás de las apariencias.", height=150)
        st.session_state.character_data["Ideales"] = st.text_area("Ideales", "La verdad debe prevalecer.", height=100)
        st.session_state.character_data["Vínculos"] = st.text_area("Vínculos", "Mi familia fue asesinada por un culto maligno.", height=100)
        st.session_state.character_data["Defectos"] = st.text_area("Defectos", "Soy demasiado testarudo y me cuesta admitir un error.", height=100)

    with col_features:
        st.subheader("Rasgos y Características (Clase/Raza)")
        st.session_state.character_data["Rasgos_Especiales"] = st.text_area("Rasgos de Clase y Raza", 
            "**Visión en la Oscuridad:** Puedes ver en la penumbra. **Determinación enana:** Ventaja en tiradas de salvación contra veneno.", 
            height=300)

    st.subheader("Equipo e Inventario")
    st.session_state.character_data["Equipo"] = st.text_area("Lista de Equipo (separado por líneas)", 
        "Mochila, Raciones (10 días), Cuerda (50ft), 50 PO (Piezas de Oro).", 
        height=150)
    
    col_moneda = st.columns(5)
    with col_moneda[0]:
        st.session_state.character_data["PC"] = st.number_input("PC (Cobre)", 0, 1000, 0)
    with col_moneda[1]:
        st.session_state.character_data["PP"] = st.number_input("PP (Plata)", 0, 1000, 0)
    with col_moneda[2]:
        st.session_state.character_data["PE"] = st.number_input("PE (Electro)", 0, 1000, 0)
    with col_moneda[3]:
        st.session_state.character_data["PO"] = st.number_input("PO (Oro)", 0, 1000, 50)
    with col_moneda[4]:
        st.session_state.character_data["PPla"] = st.number_input("PPla (Platino)", 0, 1000, 0)


# =================================================================
# TAB 5: Finalización y Exportación
# =================================================================
with tab5:
    st.header("Paso Final: Revisión y Exportación")
    st.info("Revisa todos los datos antes de exportar. Pulsa 'Generar Hoja' para consumir la API y 'Exportar PDF' para descargar el resultado.")

    # Simulación de llamada a API/Lógica de programa
    if st.button("Generar Hoja de Personaje (Llama a tu Lógica)", type="primary"):
        # Aquí iría tu función `funciones_dnd.generar_personaje(st.session_state.character_data)`
        # Por ahora, simplemente actualizamos el estado:
        st.session_state.character_data["Estado_Final"] = "Datos Procesados OK"
        st.success("¡Datos listos! Se ha completado la simulación de la llamada a la API.")
        
    st.markdown("---")

    # Botón de exportación a PDF (Simulado)
    if st.button("Exportar Personaje como PDF (Archivo)", disabled=(st.session_state.character_data.get("Estado_Final") != "Datos Procesados OK")):
        exportar_a_pdf(st.session_state.character_data)

    # Bloque de descarga simulada
    if st.session_state.pdf_export_ready:
        st.subheader("Descarga de Hoja de Personaje")
        st.download_button(
            label="Descargar Hoja de Personaje.txt", # En el futuro, este será .pdf
            data=st.session_state.pdf_content,
            file_name=f"{st.session_state.character_data.get('Nombre', 'Personaje')}_DnD5e.txt",
            mime="text/plain"
        )
        st.code(st.session_state.pdf_content, language="text")
        st.warning("Nota: Por ahora se exporta un archivo .txt con todos los datos. Cuando implementes la librería de PDF, cambia `mime` a `application/pdf` y genera los bytes del PDF.")
    
    st.markdown("---")
    st.subheader("Vista Previa de Datos Recopilados")
    st.json(st.session_state.character_data)