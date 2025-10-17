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

Le projet suit le workflow **Gitflow** avec **Pull Requests** :
- **feature/** → développement d’une nouvelle fonctionnalité  
- **develop** → intégration et validation des fonctionnalités terminées  
- **Pull Request** → ouverture d’une PR depuis `develop` vers `main`  
  - Exécution automatique de la CI/CD (tests Pytest + couverture)  
  - Merge uniquement si les tests passent  
- **release/vX.X.X** → stabilisation avant mise en production et création du tag de version  
- **main** → branche de production, déployée automatiquement sur **Hugging Face Spaces**

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

### 4. Lancer l'application en local
```bash
python app.py
```

#### Ouvrir le navigateur à l'adresse 
- http://127.0.0.1:7860
- Interface : Gradio
- Documentation API : http://127.0.0.1:7860/docs
- Vérification de santé : http://127.0.0.1:7860/health

### 5. En ligne avec Hugging Face Spaces
Accessible via ce lien :

https://huggingface.co/spaces/FlorianSC/Deploiement_modele_machine_learning

---

## Organisation du projet
```
Deploiement_modele_machine_learning/
 ├── .github/workflows/      # Configuration du pipeline CI/CD
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

## Documentation technique complète
Une documentation détaillée du projet (API, modèle, CI/CD, base de données) est disponible via **MkDocs** :
```bash
mkdocs serve
```