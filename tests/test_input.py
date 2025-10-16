import pandas as pd
from src.preprocessing import data_engineering
from src.scaling import data_scaling
from src.prediction import predict


# === TEST entrée : Vérifier que les étapes de preprocessing produisent un résultat exploitable ===
def test_preprocessing_pipeline_ok():
    """Teste le pipeline de preprocessing (data_engineering + data_scaling)."""

    # Exemple d'entrée cohérent avec EmployeeInput
    raw_data = pd.DataFrame([{
        "age": 34,
        "genre": "M",
        "revenu_mensuel": 4200.0,
        "statut_marital": "Marie",
        "departement": "Commercial",
        "poste": "Manager",
        "niveau_hierarchique_poste": 2,
        "nombre_experiences_precedentes": 3,
        "annee_experience_totale": 9,
        "annees_dans_l_entreprise": 4,
        "annees_dans_le_poste_actuel": 2,
        "satisfaction_employee_environnement": 4,
        "note_evaluation_precedente": 3,
        "satisfaction_employee_nature_travail": 3,
        "satisfaction_employee_equipe": 4,
        "satisfaction_employee_equilibre_pro_perso": 2,
        "note_evaluation_actuelle": 4,
        "heure_supplementaires": "Non",
        "augmentation_salaire_precedente_pourcent": 0.15,
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 2,
        "distance_domicile_travail": 29,
        "niveau_education": 3,
        "domaine_etude": "Entrepreunariat",
        "frequence_deplacement": "Occasionnel",
        "annees_depuis_la_derniere_promotion": 2,
        "annes_sous_responsable_actuel": 1
    }])

    # Étapes du pipeline
    engineered = data_engineering(raw_data)
    scaled = data_scaling(engineered)

    # Vérifications
    assert scaled.shape[0] == 1, "Une seule ligne doit être conservée"
    assert scaled.shape[1] > 5, "Le dataset final doit contenir plusieurs colonnes"
    assert not scaled.isnull().values.any(), "Le pipeline ne doit pas produire de valeurs manquantes"
    assert all(scaled.dtypes.apply(lambda t: t in ['float64', 'int64'])), "Toutes les variables doivent être numériques"
