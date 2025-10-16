import pandas as pd
import pytest
from src.preprocessing import data_engineering
from src.scaling import data_scaling
from src.prediction import predict

@pytest.mark.slow
def test_model_on_full_dataset():
    """
    Teste le modèle sur le jeu de test complet du projet précédent.
    Objectif : s'assurer que la prédiction s'exécute sans erreur
    et que les résultats sont cohérents.
    """
    # Chargement du jeu de test
    test_data_path = "data/test_sample.csv"
    data = pd.read_csv(test_data_path)
    assert len(data) > 0, "Le fichier de test est vide"

    # Préparation des données
    try:
        processed = data_engineering(data)
        scaled = data_scaling(processed)
    except Exception as e:
        pytest.fail(f"Erreur lors du preprocessing ou du scaling : {e}")

    # Prédiction avec ton modèle
    try:
        results = predict(scaled)
    except Exception as e:
        pytest.fail(f"Erreur lors de la prédiction : {e}")

    # Vérifications logiques
    assert "prediction" in results, "La sortie du modèle doit contenir 'prediction'"
    preds = results["prediction"]

    # Cas où une seule prédiction (int)
    if isinstance(preds, (int, float)):
        assert preds in [0, 1], f"La prédiction doit être 0 ou 1, pas {preds}"
    else:
        # Cas où plusieurs prédictions (list/array)
        assert all(p in [0, 1] for p in preds), "Les prédictions doivent être 0 ou 1"
        assert len(set(preds)) > 1, "Toutes les prédictions sont identiques, possible surapprentissage"

        # Vérifie la cohérence du taux de départs prédits
        assert 0.05 < preds.mean() < 0.9, f"Taux de départs prédits incohérent : {preds.mean():.2f}"

    print(f"Prédiction(s) OK sur {len(data)} employés.")