import streamlit as st
from pycaret.classification import load_model, predict_model
import pandas as pd

# Définir le style de la page Streamlit
st.set_page_config(
    page_title="Déploiement de modèle avec Streamlit",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Insérer un titre avec une mise en forme personnalisée
st.title("Déploiement de modèle avec Streamlit")
st.markdown(
    """
    <div style='text-align: center; padding-top: 10px;'>
    <h2 style='color: #0073e6;'>Prédiction de diabète</h2>
    <p style='color: #666;'>Utilisez ce formulaire pour prédire le risque de diabète.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Mise en cache du chargement du modèle de prédiction (fichier pkl)
@st.cache_resource 
def chargement_modele():
    return load_model("modele_ulrich_streamlit")

##chargement effectif 
modele = chargement_modele()

# Organisation en deux colonnes (1/4 , 3/4) de l'espace d'affichage
col1, col2 = st.columns([1, 3])

# Text_input aligné sur la première colonne
Pregnancies = col1.text_input("Pregnancies: ", "6", max_chars=3)
Glucose = col1.text_input("Glucose: ", "148", max_chars=3)
BloodPressure = col1.text_input("BloodPressure: ", "72", max_chars=3)
SkinThickness = col1.text_input("SkinThickness: ", "35", max_chars=3)
Insulin = col1.text_input("Insulin: ", "0", max_chars=3)
BMI = col1.text_input("BMI: ", "33.6", max_chars=4)
DiabetesPedigreeFunction = col1.text_input("DiabetesPedigreeFunction: ", "0.627", max_chars=5)
Age = col1.text_input("Age: ", "50", max_chars=3)

# Fonction pour la transtypage avec contrôle
def try_parse(str_value):
    try:
        value = float(str_value)
    except Exception:
        value = float('NaN')
    return value

# Conversion en dictionnaire des données saisies par l'utilisateur
la_data = {'Pregnancies': try_parse(Pregnancies), 'Glucose': try_parse(Glucose),
           'BloodPressure': try_parse(BloodPressure), 'SkinThickness': try_parse(SkinThickness),
           'Insulin': try_parse(Insulin), 'BMI': try_parse(BMI),
           'DiabetesPedigreeFunction': try_parse(DiabetesPedigreeFunction), 'Age': try_parse(Age)}

# Calcul de la classe d'appartenance 
try:
    # Prédiction
    la_prediction = predict_model(modele, data=pd.DataFrame([la_data]))
except Exception:
    la_prediction = "inconnu"


##Calcul de la classe d'appartenance 
# appel de la fonction de prédiction basée sur le modèle chargé
try:
    #Prédiction
    la_prediction = predict_model(modele, data=pd.DataFrame([la_data]))  # Modification ici pour importer pandas sous l'alias pd

    #Bouton pour faire la prédiction
    if st.button("Calculer"):
        if 'prediction_label' in la_prediction.columns and 'prediction_score' in la_prediction.columns:
            # Affichage de la classe prédite et du score
            st.markdown(
                """
                <div style='text-align: center; padding-top: 10px;'>
                <h3 style='color: #0073e6;'>Résultats de la prédiction</h3>
                <p style='color: #666;'>Classe d'appartenance : {}</p>
                <p style='color: #666;'>Score de prédiction : {}</p>
                </div>
                """.format(la_prediction['prediction_label'].iloc[0], la_prediction['prediction_score'].iloc[0]),
                unsafe_allow_html=True,
            )
        else:
            st.error("Les colonnes 'prediction_label' et 'prediction_score' sont introuvables dans les résultats de la prédiction.")
except Exception as e:
    st.error(f"Une erreur s'est produite lors de la prédiction : {e}")
