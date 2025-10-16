import pandas as pd
from src.preprocessing import data_engineering
from src.scaling import data_scaling
from src.prediction import predict

# === TEST 2 : Vérifier que le modèle produit une prédiction cohérente ===
def test_model_prediction_output_ok():
    """Teste que la fonction predict renvoie bien une valeur cohérente."""
    df = pd.DataFrame([{
        "age": 45,
        "genre": "F",
        "revenu_mensuel": 5300.0,
        "statut_marital": "Divorce",
        "departement": "Consulting",
        "poste": "DirecteurTechnique",
        "niveau_hierarchique_poste": 3,
        "nombre_experiences_precedentes": 6,
        "annee_experience_totale": 15,
        "annees_dans_l_entreprise": 8,
        "annees_dans_le_poste_actuel": 4,
        "satisfaction_employee_environnement": 3,
        "note_evaluation_precedente": 3,
        "satisfaction_employee_nature_travail": 1,
        "satisfaction_employee_equipe": 2,
        "satisfaction_employee_equilibre_pro_perso": 1,
        "note_evaluation_actuelle": 4,
        "heure_supplementaires": "Oui",
        "augmentation_salaire_precedente_pourcent": 4,
        "nombre_participation_pee": 2,
        "nb_formations_suivies": 3,
        "distance_domicile_travail": 15,
        "niveau_education": 4,
        "domaine_etude": "Entrepreunariat",
        "frequence_deplacement": "Frequent",
        "annees_depuis_la_derniere_promotion": 3,
        "annes_sous_responsable_actuel": 2
    }])

    processed = data_engineering(df)
    scaled = data_scaling(processed)
    result = predict(scaled)

    assert "prediction" in result, "Le résultat doit contenir une clé 'prediction'"
    assert "probability" in result, "Le résultat doit contenir une clé 'probability'"
    assert result["prediction"] in [0, 1], "La prédiction doit être binaire (0 ou 1)"
    assert 0 <= result["probability"] <= 1, "La probabilité doit être comprise entre 0 et 1"