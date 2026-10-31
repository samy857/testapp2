import streamlit as st
import random

# Configuration de la page
st.set_page_config(
    page_title="Jeu du Nombre Mystère",
    page_icon="🎩",
    layout="centered"
)

# Style CSS pour un arrière-plan ultra décoratif et moderne
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f172a 1e-2, #1e293b 100%);
        color: #f8fafc;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        color: white;
        padding: 0.75rem;
        border: none;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #4f46e5 0%, #9333ea 100%);
        color: white;
    }
    .mystery-banner {
        text-align: center;
        background: rgba(30, 41, 59, 0.8);
        border: 2px solid rgba(148, 163, 184, 0.2);
        padding: 30px;
        border-radius: 24px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        margin-bottom: 25px;
    }
    .character {
        font-size: 70px;
        margin-bottom: 10px;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-12px); }
    }
    </style>
""", unsafe_allow_html=True)

# En-tête avec le personnage mystère et décorations lumineuses
st.markdown("""
    <div class="mystery-banner">
        <div class="character">🎩🧐❓</div>
        <h1 style="color: #f8fafc; margin: 0; font-size: 2.2rem;">Jeu du Nombre Mystère</h1>
        <p style="color: #94a3b8; font-size: 16px; margin-top: 8px;">Défie ton esprit logique et trouve le nombre secret ! 🌟🧩🎲</p>
    </div>
""", unsafe_allow_html=True)

# Sélection de la difficulté
niveau = st.selectbox("🎚️ Choisis ton niveau de difficulté :", ["Facile (1 à 50)", "Moyen (1 à 100)", "Difficile (1 à 500)"])

# Définition des bornes selon le niveau
if "Facile" in niveau:
    max_val = 50
elif "Moyen" in niveau:
    max_val = 100
else:
    max_val = 500

# Initialisation ou réinitialisation du jeu si on change de niveau
if "niveau_actuel" not in st.session_state or st.session_state.niveau_actuel != niveau:
    st.session_state.niveau_actuel = niveau
    st.session_state.nombre_secret = random.randint(1, max_val)
    st.session_state.tentatives = 0

# Zone de saisie pour l'utilisateur
choix = st.number_input(f"🔍 Entre ton nombre (entre 1 et {max_val}) :", min_value=1, max_value=max_val, step=1)

if st.button("✨ Valider ma proposition ✨"):
    st.session_state.tentatives += 1
    
    if choix < st.session_state.nombre_secret:
        st.warning(f"📈 C'est **plus grand** que {choix} ! Monte un peu plus haut ⬆️")
    elif choix > st.session_state.nombre_secret:
        st.warning(f"📉 C'est **plus petit** que {choix} ! Descends un peu plus bas ⬇️")
    else:
        st.success(f"🎉 Félicitations ! Tu as trouvé le nombre mystère **{st.session_state.nombre_secret}** en **{st.session_state.tentatives} tentatives** 🏆 !")
        if st.button("🔄 Relancer une partie"):
            st.session_state.nombre_secret = random.randint(1, max_val)
            st.session_state.tentatives = 0
            st.rerun()

# Affichage du compteur de tentatives
if st.session_state.tentatives > 0:
    st.info(f"🎯 Nombre de tentatives actuelles : **{st.session_state.tentatives}**")