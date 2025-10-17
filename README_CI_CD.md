# Déploiement d'un modèle de Machine Learning - Explication CI/CD

## Conventions de code
- Respecter le style Python PEP8.
- Bien commenter le code et ajouter des docstrings simples pour les fonctions.

## Organisation Gitflow
Le cycle de vie du projet suit strictement le workflow **Gitflow** :  

1. **Feature branches**  
2. **Develop**
3. **Release**
4. **Main**

**Exemple de cycle :**  
- **feature/** → Développement d’une nouvelle fonctionnalité  
    - ex. `feature/add_dockerfile`
- **develop** → Intègre toutes les fonctionnalités terminées et testées.
- **Pull Request** → Une PR est ouverte de `develop` vers `main`  
   - La CI s’exécute automatiquement (tests + validation)
   - Le merge n’est possible que si la CI passe avec succès
- **release/vX.X.X** → Stabilisation avant production et création du tag de version.  
    - ex. `v3.2.0`
- **main** → Branche de production, déployée automatiquement sur **Hugging Face Spaces**.

---

## CI/CD
- Les actions GitHub se trouvent dans .github/workflows/ci.yaml
- Le pipeline s’exécute automatiquement quand :
    - On fait un push sur main,
    - Ou une pull request vers main.

---

## Étapes du pipeline :
	1.	Installer Python et les dépendances.
	2.	Lancer les tests (dans tests/).
	3.	Déployer sur Hugging Face Spaces si les tests passent.

---

## Tests
- Les tests se trouvent dans tests/.
- Pour lancer les tests en local :
```bash
    pytest tests/
```