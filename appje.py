import streamlit as st
import random

# Configuration de la page
st.set_page_config(
    page_title="Jeu du Nombre Mystère",
    page_icon="🎩",
    layout="centered"
)

# Style CSS pour un design coloré, moderne et plein de déco autour du jeu
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        background: linear-gradient(90deg, #4F46E5 0%, #9333EA 100%);
        color: white;
        padding: 0.75rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #4338CA 0%, #7E22CE 100%);
        color: white;
    }
    .mystery-box {
        text-align: center;
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .character {
        font-size: 80px;
        margin-bottom: 10px;
        animation: bounce 2s infinite;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    </style>
""", unsafe_allow_html=True)

# En-tête avec le personnage mystère complet (Chapeau, Moustaches, Jambes) et décorations de jeu
st.markdown("""
    <div class="mystery-box">
        <div class="character">🎩🧐❓</div>
        <h1 style="color: #1E293B; margin: 0;">Jeu du Nombre Mystère</h1>
        <p style="color: #64748B; font-size: 16px; margin-top: 5px;">Devine le nombre secret entre 1 et 100 ! 🎲🧩</p>
    </div>
""", unsafe_allow_html=True)

# Initialisation de l'état du jeu
if "nombre_secret" not in st.session_state:
    st.session_state.nombre_secret = random.randint(1, 100)
    st.session_state.tentatives = 0

# Zone de saisie pour l'utilisateur
choix = st.number_input("🔍 Entre ton nombre mystère :", min_value=1, max_value=100, step=1)

if st.button("✨ Valider ma proposition ✨"):
    st.session_state.tentatives += 1
    
    if choix < st.session_state.nombre_secret:
        st.warning(f"📈 C'est **plus grand** que {choix} ! Monte un peu ⬆️")
    elif choix > st.session_state.nombre_secret:
        st.warning(f"📉 C'est **plus petit** que {choix} ! Descends un peu ⬇️")
    else:
        st.success(f"🎉 Félicitations ! Tu as trouvé le nombre mystère **{st.session_state.nombre_secret}** en **{st.session_state.tentatives} tentatives** 🏆 !")
        if st.button("🔄 Rejouer une partie"):
            st.session_state.nombre_secret = random.randint(1, 100)
            st.session_state.tentatives = 0
            st.rerun()

# Affichage du compteur de tentatives avec un style sympa
if st.session_state.tentatives > 0:
    st.info(f"🎯 Nombre de tentatives actuelles : **{st.session_state.tentatives}**")