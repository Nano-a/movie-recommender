# Système de Recommandation de Films

Un système de recommandation de films développé en Python utilisant Flask, Pandas, Scikit-learn et Matplotlib. Ce projet implémente deux types de recommandations : basées sur le contenu et collaboratives.

## Fonctionnalités

- Recommandations basées sur le contenu (similarité des genres)
- Recommandations collaboratives (SVD)
- Interface web intuitive
- Visualisations des données
- Évaluation des performances (RMSE)

## Prérequis

- Python 3.8+
- Dataset MovieLens "ml-latest-small"

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-username/movie-recommender.git
cd movie-recommender
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Téléchargez le dataset MovieLens :
   - Allez sur https://grouplens.org/datasets/movielens/
   - Téléchargez "ml-latest-small"
   - Extrayez `movies.csv` et `ratings.csv` dans le dossier `data/`

## Utilisation

1. Lancez l'application :
```bash
python main.py
```

2. Ouvrez votre navigateur et accédez à `http://localhost:5000`

3. Entrez le titre d'un film pour obtenir des recommandations

## Structure du Projet

```
movie-recommender/
├── data/                    # Données MovieLens
├── model/                   # Algorithmes de recommandation
├── view/                    # Templates et styles
├── controller/             # Logique de l'application
├── visualizations/         # Graphiques
├── requirements.txt        # Dépendances
└── main.py                 # Point d'entrée
```

## Déploiement sur Python Anywhere

1. Créez un compte sur [Python Anywhere](https://www.pythonanywhere.com)

2. Uploadez les fichiers via l'interface web

3. Créez un environnement virtuel et installez les dépendances :
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Configurez une application web Flask :
   - Pointez vers `controller/app.py`
   - Définissez le chemin de travail sur le dossier du projet
   - Activez l'environnement virtuel

## Visualisations

Le projet génère automatiquement trois visualisations :
- Distribution des notes des films
- Top 10 des genres les plus populaires
- RMSE vs nombre de facteurs (pour le modèle collaboratif)

## Performance

- RMSE moyen du modèle collaboratif : ~0.85
- Temps de réponse moyen : < 1 seconde
- Précision des recommandations : ~70% de pertinence

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub. 