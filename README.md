# 🎬 CineRecommend – Système de Recommandation de Films

Projet universitaire développé par **Abderrahman AJINOU** (Université Paris Cité, N° Étudiant : 22116322)

---

## 🤖 Pourquoi ce projet est-il un vrai projet d'intelligence artificielle ?

Ce projet n'est pas une simple application algorithmique ou une interface web : il s'agit d'un **véritable système d'intelligence artificielle appliquée** (machine learning) pour la recommandation de films. Voici pourquoi :

- **Utilisation de techniques de machine learning** : le cœur du système repose sur le filtrage collaboratif (SVD) et la similarité cosinus, deux méthodes classiques de l'IA pour la recommandation personnalisée.
- **Manipulation de données réelles** : le projet utilise des jeux de données MovieLens (notes d'utilisateurs, genres de films), construit des matrices utilisateur-film, et apprend des préférences à partir de ces données.
- **Modélisation et évaluation** : le code inclut la séparation train/test, le calcul du RMSE (Root Mean Square Error) pour évaluer la performance du modèle, et la possibilité de générer des visualisations pour analyser les résultats.
- **Personnalisation intelligente** : les recommandations ne sont pas statiques, mais générées dynamiquement en fonction des choix et des préférences de l'utilisateur.
- **Respect des standards IA** : le projet suit les bonnes pratiques du machine learning (prétraitement, entraînement, évaluation, visualisation, modularité du code).

> **En résumé :** CineRecommend est un projet d'intelligence artificielle (machine learning appliqué à la recommandation), et non un simple projet d'algorithmique ou d'interface. Il peut être présenté comme tel dans un contexte académique ou professionnel.

---

## 🚀 Présentation

CineRecommend est un système de recommandation de films basé sur la similarité cosinus et le filtrage collaboratif, développé en **Python 3.10+** avec **Flask** pour l’interface web. Il propose une interface moderne inspirée du cinéma (design Tailwind) et des outils d’analyse et de visualisation des données.

---

## 📸 Captures d'écran

<div align="center">
  <img src="Photo%20Presentation/1.png" alt="Interface d'accueil" width="45%" />
  <img src="Photo%20Presentation/2.png" alt="Résultats de recommandation" width="45%" /> 
  <img src="Photo%20Presentation/3.png" alt="Visualisation des données" width="90%" style="margin-top: 20px;" />
</div>

*Interface utilisateur et résultats du système de recommandation*

---

## 🗂️ Structure du projet

```
movie-recommender/
├── app.py                # Application web Flask (point d'entrée principal)
├── main.py               # Point d'entrée avancé (visualisations, initialisation)
├── config.py             # Paramètres de configuration globaux
├── requirements.txt      # Dépendances Python (versions exactes)
├── templates/            # Templates HTML (Jinja2, design moderne)
│   ├── index.html        # Page d'accueil (formulaire)
│   └── results.html      # Page des résultats
├── static/               # Fichiers statiques (favicon, images, etc.)
├── data/                 # Jeux de données (movies.csv, ratings.csv)
├── model/                # Scripts de recommandation et d'évaluation
│   ├── recommender.py    # Logique de recommandation (SVD, contenu)
│   └── evaluation.py     # Outils d'évaluation (RMSE, split)
├── visualizations/       # Scripts et images de visualisation
│   ├── plots.py          # Génération de graphiques
│   ├── top_genres.png    # Exemple de visualisation
│   └── rating_distribution.png
├── tests/                # Tests unitaires
│   └── test_basic.py     # Vérification de l'environnement et des dépendances
└── README.md             # Documentation complète
```

---

## 🛠️ Installation et environnement

### 1. **Via Miniconda (recommandé)**
```bash
# Installer Miniconda si besoin : https://docs.conda.io/en/latest/miniconda.html
source ~/miniconda3/etc/profile.d/conda.sh
conda create -n movie-reco python=3.10
conda activate movie-reco
pip install -r requirements.txt
```

### 2. **Via venv (si Python 3.10+ installé)**
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📦 Dépendances principales

- Flask==3.0.0
- numpy==1.26.4
- scikit-learn==1.3.0
- matplotlib (pour les visualisations)
- pandas (pour la manipulation de données)

> Toutes les versions sont précisées dans `requirements.txt`.

---

## ⚙️ Configuration

Le fichier `config.py` centralise les paramètres :
- Chemins des dossiers (`data/`, `model/`, `visualizations/`)
- Paramètres du modèle (nombre de facteurs SVD, seed, etc.)
- Paramètres API (hôte, port, debug)
- Timeout cache, logging, etc.

---

## 📊 Données

- `data/movies.csv` : Liste des films (ID, titre, genres)
- `data/ratings.csv` : Notes des utilisateurs (userId, movieId, rating)

> Les jeux de données sont nécessaires pour entraîner et tester les modèles.

---

## 🧠 Fonctionnement & points d’entrée

- **app.py** : Lance l’interface web Flask (formulaire, recommandations, résultats)
- **main.py** : Point d’entrée avancé (génère les visualisations, initialise l’app, lance Flask)
- **model/recommender.py** : Logique de recommandation (SVD, similarité cosinus, contenu)
- **model/evaluation.py** : Outils d’évaluation (RMSE, split)
- **visualizations/plots.py** : Génération de graphiques (distribution des notes, genres)

---

## 🌐 Utilisation

1. **Lancer l’application web**
   ```bash
   conda activate movie-reco  # ou source venv/bin/activate
   python app.py
   ```
2. **Accéder à l’interface** : [http://localhost:5000](http://localhost:5000)
3. **Saisir un film** parmi la liste proposée
4. **Choisir le nombre de recommandations**
5. **Obtenir les résultats**

---

## 🧪 Tests

- Les tests unitaires sont dans `tests/`.
- Pour lancer les tests :
  ```bash
  pytest tests/
  ```
- Les tests vérifient l’environnement et l’installation des dépendances principales.

---

## 📈 Visualisations

- Génération de graphiques avec `visualizations/plots.py` :
  - Distribution des notes (`rating_distribution.png`)
  - Top genres (`top_genres.png`)
- Pour générer les graphiques :
  ```bash
  python visualizations/plots.py
  ```

---

## 📝 Bonnes pratiques & conseils

- **Ne versionnez pas** les fichiers volumineux ou sensibles (`.gitignore` déjà configuré)
- **Gardez l’environnement isolé** (conda ou venv)
- **Documentez vos modifications** dans le devbook.md pour un suivi optimal

---

## 👤 Auteur

Abderrahman AJINOU  
Étudiant en 2ᵉ année licence Informatique Générale  
Université Paris Cité, Campus Grand Moulin  
Mail : abderrahman.ajinou@etu.u-paris.fr

---

## 📚 Ressources utiles

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Documentation scikit-learn](https://scikit-learn.org/)
- [Documentation pandas](https://pandas.pydata.org/)
- [Documentation matplotlib](https://matplotlib.org/)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

---

## 🏆 Pour toute question ou suggestion, n’hésitez pas à me contacter !
