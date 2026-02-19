import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="CV Safiyah NGOM", layout="wide")

# --- Style CSS personnalisé pour correspondre à l'image ---
st.markdown("""
    <style>
    /* Fond de la zone principale (à droite) */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff; 
    }
    /* Style de la barre latérale (Partie colorée à gauche) */
    [data-testid="stSidebar"] {
        background-color: #dccab9; /* Couleur beige/sable du modèle */
    }
    /* Ajustement des titres pour plus de sobriété */
    h1, h2, h3 {
        color: #2c2c2c;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DONNÉES DU CV ---
cv = {
    "Nom": "Safiyah NGOM",
    "Titre": "Étudiante en Géomatique",
    "Email": "safiyahngom@gmail.com",
    "Adresse": "Grand Standing, Thiès",
    "Langues": {
        "Français": "Courant",
        "Anglais": "Niveau intermédiaire"
    },
    "Formation": [
        {"Année": "2024 - 2025", "Diplôme": "Licence 1 en Géomatique", "Lieu": "CEDT, LE G15, Dakar"},
        {"Année": "2023", "Diplôme": "Baccalauréat L2", "Lieu": "Annexe Malick Sy, Thiès"}
    ],
    "Compétences": [
        "Maîtrise des logiciels de SIG : ArcGIS, QGIS",
        "Gestion de bases de données : PostgreSQL/PostGIS, MySQL, MariaDB",
        "Travail en équipe et en autonomie",
        "Capacité d’analyse et de synthèse",
        "Sens de l’organisation et rigueur professionnelle"
    ],
    "Projets": [
        "Carte de la répartition de la population de Thiès",
        "Numérisation des Parcelles Assainies",
        "Base de données spatiale pour le recensement des infrastructures de Diass"
    ],
    "Interets": [
        "Cartographie interactive",
        "Tendances démographiques et sociales"
    ]
}

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    # --- SECTION PHOTO ---
    # Remplacez 'votre_photo.jpg' par le nom réel de votre fichier image
    try:
        image = Image.open('votre_photo.jpg') 
        st.image(image, use_container_width=True)
    except:
        st.warning("📸 Emplacement Photo")

    st.markdown("### COORDONNÉES")
    st.write(f"✉️ {cv['Email']}")
    st.write(f"📍 {cv['Adresse']}")

    st.markdown("---")
    st.markdown("### LANGUES")
    for langue, niveau in cv["Langues"].items():
        st.write(f"*{langue}* : {niveau}")

    st.markdown("---")
    st.markdown("### FORMATION")
    for f in cv["Formation"]:
        st.markdown(f"*{f['Diplôme']}*")
        st.caption(f"{f['Lieu']} | {f['Année']}")

    st.markdown("---")
    st.markdown("### CENTRES D'INTÉRÊT")
    for i in cv["Interets"]:
        st.write(f"• {i}")

# --- ZONE PRINCIPALE (À DROITE) ---
st.title(cv["Nom"])
st.subheader(cv["Titre"])

st.markdown("---")

st.markdown("### 🛠 COMPÉTENCES")
for comp in cv["Compétences"]:
    st.markdown(f"- {comp}")

st.markdown("### 📊 PROJETS ACADÉMIQUES")
for projet in cv["Projets"]:
    st.markdown(f"- {projet}")
