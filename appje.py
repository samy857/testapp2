import streamlit as st
import random

# Configuration de la page
st.set_page_config(
    page_title="Jeu du Nombre Mystère",
    page_icon="🎯",
    layout="centered"
)

# Style CSS épuré et moderne
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        background-color: #2563EB;
        color: white;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Titre et description
st.title("🎯 Jeu du Nombre Mystère")
st.write("Trouve le nombre secret compris entre **1 et 100**. Bon jeu !")

# Initialisation du jeu
if "nombre_secret" not in st.session_state:
    st.session_state.nombre_secret = random.randint(1, 100)
    st.session_state.tentatives = 0

# Zone de saisie
choix = st.number_input("Entre ton nombre :", min_value=1, max_value=100, step=1)

if st.button("Valider ma proposition"):
    st.session_state.tentatives += 1
    
    if choix < st.session_state.nombre_secret:
        st.warning(f"📈 C'est **plus grand** que {choix} !")
    elif choix > st.session_state.nombre_secret:
        st.warning(f"📉 C'est **plus petit** que {choix} !")
    else:
        st.success(f"🎉 Bravo ! Tu as trouvé le nombre mystère **{st.session_state.nombre_secret}** en **{st.session_state.tentatives} tentatives** !")
        if st.button("Rejouer une partie"):
            st.session_state.nombre_secret = random.randint(1, 100)
            st.session_state.tentatives = 0
            st.rerun()

# Affichage du compteur de tentatives
if st.session_state.tentatives > 0:
    st.info(f"Nombre de tentatives : {st.session_state.tentatives}")