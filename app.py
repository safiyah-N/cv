import streamlit as st

# --- Style CSS pour le fond ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f5f5dc; /* beige clair */
}
.sidebar .sidebar-content {
    background-color: #d2b48c; /* marron clair */
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Données du CV
cv = {
    "Nom": "Safiyah NGOM",
    "Titre": "Étudiante en Géomatique",
    "Résumé": (
        "Étudiante en première année en géomatique au centre de formation CEDT, le G15, "
        "je souhaite intégrer l’Agence Nationale de la Statistique et de la Démographie (ANSD) pour un stage académique. "
        "Ce stage me permettra de renforcer mes compétences en SIG, en traitement de données statistiques et en cartographie numérique, "
        "tout en contribuant aux missions de collecte et d’analyse de données territoriales et socio-économiques."
    ),
    "Compétences": [
        "Maîtrise des bases des logiciels de SIG : ArcGIS, QGIS",
        "Conception et gestion de bases de données sous PostgreSQL/PostGIS, MySQL et MariaDB",
        "Travail en équipe et en autonomie",
        "Capacité d’analyse et de synthèse",
        "Sens de l’organisation et rigueur professionnelle"
    ],
    "Projets Académiques": [
        "Carte de la répartition de la population de Thiès (Travail pratique de SIG)",
        "Numérisation des Parcelles Assainies",
        "Projet de base de données spatiale sous PostgreSQL visant à recenser et gérer les infrastructures de la commune de Diass"
    ],
    "Formation": [
        {"Année": "2024-2025", "Diplôme": "Licence 1 en Géomatique", "Établissement": "CEDT, LE G15, Dakar"},
        {"Année": "2023", "Diplôme": "Baccalauréat L2", "Établissement": "Annexe Malick Sy, Thiès"}
    ],
    "Centres d'intérêt": [
        "Cartographie interactive",
        "Curiosité pour les tendances démographiques et leurs conséquences sociales"
    ],
    "Langues": {
        "Français": "Courant",
        "Anglais": "Niveau intermédiaire"
    },
    "Coordonnées": {
        "Email": "safiyahngom@gmail.com",
        "Adresse": "Grand Standing, Thiès"
    }
}

# --- Mise en page en colonnes ---
col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.title(f"{cv['Nom']} - {cv['Titre']}")

    st.subheader("Résumé")
    st.write(cv['Résumé'])

    st.subheader("Compétences")
    for comp in cv["Compétences"]:
        st.markdown(f"- {comp}")

    st.subheader("Projets Académiques")
    for projet in cv["Projets Académiques"]:
        st.markdown(f"- {projet}")

    st.subheader("Formation")
    for formation in cv["Formation"]:
        st.markdown(f"- {formation['Année']} : {formation['Diplôme']} ({formation['Établissement']})")

with col2:
    st.subheader("Coordonnées")
    for cle, valeur in cv["Coordonnées"].items():
        st.markdown(f"- {cle} : {valeur}")

    st.subheader("Langues")
    for langue, niveau in cv["Langues"].items():
        st.markdown(f"- {langue} : {niveau}")

    st.subheader("Centres d'intérêt")
    for centre in cv["Centres d'intérêt"]:
        st.markdown(f"- {centre}")
