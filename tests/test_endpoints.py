# tests/test_endpoints.py
from fastapi.testclient import TestClient
import pytest
from app import app

client = TestClient(app)

# Test 1 — Endpoint /health

def test_health_endpoint():
    """Vérifie que le endpoint /health renvoie bien 200 et un message OK"""
    response = client.get("/health")
    assert response.status_code == 200, "Le endpoint /health doit répondre 200"
    data = response.json()
    assert "status" in data, "Le JSON doit contenir 'status'"
    assert data["status"].lower() == "ok"


# Test 2 — Endpoint /predict

def test_predict_endpoint_valid():
    """Vérifie qu’une prédiction valide renvoie bien 200 et un résultat"""
    example_input = {
        "age": 28,
        "genre": "M",
        "revenu_mensuel": 3000.0,
        "statut_marital": "Marie",
        "departement": "RessourcesHumaines",
        "poste": "CadreCommercial",
        "niveau_hierarchique_poste": 1,
        "nombre_experiences_precedentes": 2,
        "annee_experience_totale": 6,
        "annees_dans_l_entreprise": 3,
        "annees_dans_le_poste_actuel": 2,
        "satisfaction_employee_environnement": 3,
        "note_evaluation_precedente": 4,
        "satisfaction_employee_nature_travail": 3,
        "satisfaction_employee_equipe": 4,
        "satisfaction_employee_equilibre_pro_perso": 3,
        "note_evaluation_actuelle": 4,
        "heure_supplementaires": "Non",
        "augmentation_salaire_precedente_pourcent": 0.11,
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 2,
        "distance_domicile_travail": 17,
        "niveau_education": 3,
        "domaine_etude": "InfraCloud",
        "frequence_deplacement": "Occasionnel",
        "annees_depuis_la_derniere_promotion": 1,
        "annes_sous_responsable_actuel": 2
    }

    response = client.post("/predict", json=example_input)
    assert response.status_code == 200, "Le endpoint /predict doit répondre 200"
    result = response.json()
    assert "prediction" in result, "La réponse doit contenir la clé 'prediction'"
    assert result["prediction"] in [0, 1], "La prédiction doit être 0 ou 1"


def test_predict_endpoint_invalid():
    """Vérifie qu’une requête invalide est bien rejetée"""
    invalid_input = {"age": "trente"}  # Mauvais type
    response = client.post("/predict", json=invalid_input)
    assert response.status_code == 422, "Le endpoint /predict doit renvoyer 422 pour une entrée invalide"