# 🎬 CineRecommend – Système de Recommandation de Films

Projet universitaire développé par **Abderrahman AJINOU** (Université Paris Cité, N° Étudiant : 22116322)

---

## 🚀 Présentation

CineRecommend est un système de recommandation de films basé sur la similarité cosinus et le filtrage collaboratif, développé en **Python 3.10+** avec **Flask** pour l’interface web. Il propose une interface moderne inspirée du cinéma (design Tailwind) et des outils d’analyse et de visualisation des données.

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
