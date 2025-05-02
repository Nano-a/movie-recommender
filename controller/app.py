from flask import Flask, render_template, request, jsonify
from model.recommender import Recommender
from model.evaluation import split_data, calculate_rmse
import time

app = Flask(__name__, 
            template_folder='../view/templates',
            static_folder='../view/static')

# Initialiser le recommandeur
print("Initialisation du système de recommandation...")
recommender = Recommender()

@app.route('/')
def index():
    """Page d'accueil avec le formulaire de recherche."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    """Route pour obtenir les recommandations."""
    movie_title = request.form['movie']
    print(f"Recherche de recommandations pour : {movie_title}")
    
    start_time = time.time()
    # Obtenir les recommandations basées sur le contenu
    content_recommendations = recommender.recommend_by_content(movie_title)
    
    # Si un utilisateur est spécifié, obtenir aussi les recommandations collaboratives
    user_id = request.form.get('user_id')
    collaborative_recommendations = []
    if user_id and user_id.isdigit():
        print(f"Recherche de recommandations collaboratives pour l'utilisateur {user_id}")
        collaborative_recommendations = recommender.recommend_collaborative(
            int(user_id)
        )
    
    print(f"Recommandations générées en {time.time() - start_time:.2f} secondes")
    return render_template(
        'results.html',
        movie=movie_title,
        content_recommendations=content_recommendations,
        collaborative_recommendations=collaborative_recommendations
    )

def init_app():
    """Initialise l'application en prétraitant les données et entraînant le modèle."""
    print("\nInitialisation de l'application...")
    start_time = time.time()
    
    print("\nPrétraitement des données...")
    recommender.preprocess()
    
    print("\nEntraînement du modèle collaboratif...")
    recommender.train_collaborative()
    
    # Calculer le RMSE sur un ensemble de test
    print("\nÉvaluation du modèle...")
    train_ratings, test_ratings = split_data(recommender.ratings)
    rmse = calculate_rmse(recommender, test_ratings)
    print(f"RMSE du modèle: {rmse:.4f}")
    
    total_time = time.time() - start_time
    print(f"\nInitialisation terminée en {total_time:.2f} secondes")
    print("\nL'application est prête !")

if __name__ == '__main__':
    init_app()
    app.run(debug=True) 