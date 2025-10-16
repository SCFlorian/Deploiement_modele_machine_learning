---
title: Deploiement Modele Machine Learning
emoji: 📊
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

# Déploiement d’un modèle de machine learning

## Description
Ce projet reprend le modèle développé dans *« Classifiez automatiquement des informations »* et le déploie sous la forme d’une **API FastAPI** accessible en ligne via **Hugging Face Spaces**.  

L’objectif :  
- rendre le modèle prédictif accessible via une interface utilisateur (Gradio)  
- automatiser les tests et le déploiement grâce à **GitHub Actions (CI/CD)**  
- journaliser les prédictions dans une base de données (PostgreSQL ou SQLite selon l’environnement)

---

## Organisation Gitflow

Le cycle de vie du projet suit strictement le workflow **Gitflow** :  

1. **Feature branches** : développement d’une nouvelle fonctionnalité.  
   - `feature/feature-engineering` : traitement des données brutes pour générer des données nettoyées.  

2. **Develop** : intègre les fonctionnalités terminées.  

3. **Release** : stabilisation avant passage en production. Un **tag de version** est créé (ex : `v1.0.0`).  

4. **Main** : branche de production, déployée automatiquement sur Hugging Face Spaces.  

**Exemple de cycle :**  
- Création de `feature/feature-engineering` → merge dans `develop`
- Merge de `develop` → `release/v1.0.0` avec création du tag
- Merge de `release/v1.0.0` → `main`
- Même logique ensuite pour `feature/feature-prediction`

---

## Installation

### 1. Cloner le dépôt
```bash
git clone git@github.com:SCFlorian/Deploiement_modele_ML.git
cd Deployez_modele_ml
```

### 2. Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate    # Mac / Linux
.venv\Scripts\activate       # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```
---

## Organisation du projet
```
deployez_modele_ml/
 ├── .github/workflows/      # Configuration du pipeline CI/CD
 ├── assets/                 # Captures d’écran & schémas (tests, UML, etc.)
 ├── data/                   # Échantillon du jeu de données de test
 ├── database/               # Création et gestion des bases (PostgreSQL / SQLite)
 ├── models/                 # Modèle sauvegardé (model.pkl)
 ├── src/                    # Modules de preprocessing, scaling, prédiction
 ├── tests/                  # Tests unitaires et fonctionnels (Pytest)
 ├── .gitignore
 ├── app.py                  # Application principale FastAPI + interface Gradio
 ├── Dockerfile
 ├── README_CI_CD.md
 ├── README.md
 └── requirements.txt
```

---

## Fonctionnalités principales
- Interface web Gradio intégrée
- API FastAPI documentée automatiquement via Swagger/OpenAPI (/docs)
- Journalisation complète des entrées, prédictions et réponses
- Préprocessing et scaling automatisés avant la prédiction
- Base de données hybride : PostgreSQL (local) / SQLite (Hugging Face)
- Pipeline CI/CD automatisé via GitHub Actions :
   - exécution des tests Pytest
   - génération du rapport de couverture
   - déploiement automatique sur Hugging Face si tout est valide

---

## Base de données
Deux modes selon l’environnement :
- **Local avec PostreSQl** : connexion via DATABASE_URL dans .env
- **Hugging Face ave SQLite** temporaire : stockée dans /tmp/hf_temp.db car Hugging Face ne permet pas PostgreSQL

Tables créées par SQLAlchemy :
- employee_inputs : données brutes
- features : données prêtes pour la prédiction
- prediction_results : résultats du modèle
- requests : journalisation des requêtes API
- api_responses : réponses envoyées à l’utilisateur

Diagramme UML de la base :

<img width="788" height="644" alt="diagramme-UML" src="https://github.com/user-attachments/assets/a0fdf6ca-6ada-4c14-aefd-7de30ce31ace" />


---

## Tests unitaires & fonctionnels
Les tests sont réalisés avec **Pytest** et **Pytest-Cov**, couvrant :
- les endpoints /health et /predict
- le pipeline de preprocessing
- le modèle complet sur le jeu de test

Résultats des tests :
- Pytest :

<img width="564" height="111" alt="pytest" src="https://github.com/user-attachments/assets/277c495e-7376-4562-b845-50b591c57ef6" />

- Pytest-Cov :

<img width="514" height="160" alt="pytest-cov" src="https://github.com/user-attachments/assets/536fcccd-6b9e-4f51-825f-c599718c95e8" />

---

## Authentification & Sécurisation
- Authentification par token
- Gestion des secrets via .env

---

## Gestion des environnements
- Développement : branches feature/*
- Test : exécution automatique des tests unitaires via GitHub Actions à chaque push
- Release : stabilisation et tagging (ex. v1.0.0, v1.1.0)
- Production : branche main, déployée automatiquement sur Hugging Face Spaces
- Fusion vers main uniquement via Pull Request validée
