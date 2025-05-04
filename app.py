from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Données simplifiées pour la démo
movies = {
    1: "The Shawshank Redemption",
    2: "The Godfather",
    3: "The Dark Knight",
    4: "Pulp Fiction",
    5: "Forrest Gump",
    6: "Inception",
    7: "The Matrix",
    8: "Goodfellas",
    9: "The Silence of the Lambs",
    10: "Fight Club"
}

# Matrice de similarité pré-calculée (simplifiée)
similarity_matrix = np.array([
    [1.0, 0.8, 0.6, 0.7, 0.5, 0.4, 0.3, 0.6, 0.5, 0.4],
    [0.8, 1.0, 0.5, 0.8, 0.4, 0.3, 0.2, 0.7, 0.6, 0.3],
    [0.6, 0.5, 1.0, 0.6, 0.3, 0.7, 0.8, 0.4, 0.3, 0.5],
    [0.7, 0.8, 0.6, 1.0, 0.5, 0.4, 0.3, 0.8, 0.6, 0.7],
    [0.5, 0.4, 0.3, 0.5, 1.0, 0.4, 0.3, 0.5, 0.4, 0.3],
    [0.4, 0.3, 0.7, 0.4, 0.4, 1.0, 0.8, 0.3, 0.4, 0.6],
    [0.3, 0.2, 0.8, 0.3, 0.3, 0.8, 1.0, 0.2, 0.3, 0.5],
    [0.6, 0.7, 0.4, 0.8, 0.5, 0.3, 0.2, 1.0, 0.7, 0.6],
    [0.5, 0.6, 0.3, 0.6, 0.4, 0.4, 0.3, 0.7, 1.0, 0.5],
    [0.4, 0.3, 0.5, 0.7, 0.3, 0.6, 0.5, 0.6, 0.5, 1.0]
])

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name'].strip()
    num_recommendations = int(request.form['num_recommendations'])
    
    # Trouver l'ID du film
    movie_id = None
    for id, title in movies.items():
        if title.lower() == movie_name.lower():
            movie_id = id
            break
    
    if movie_id is None:
        return render_template('index.html', 
                             movies=movies, 
                             error="Film non trouvé. Veuillez vérifier le nom du film.")
    
    # Obtenir les indices des films les plus similaires
    similar_indices = np.argsort(similarity_matrix[movie_id-1])[::-1][1:num_recommendations+1]
    
    recommendations = {
        'movie': movies[movie_id],
        'recommendations': [movies[i+1] for i in similar_indices],
        'num_recommendations': num_recommendations
    }
    
    return render_template('results.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True) 