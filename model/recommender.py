import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, movies_path='data/movies.csv', ratings_path='data/ratings.csv'):
        print("Chargement des données...")
        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)
        print(f"Données chargées : {len(self.movies)} films et {len(self.ratings)} notes")
        self.user_movie_matrix = None
        self.model = None
        self.movie_genre_matrix = None

    def preprocess(self):
        """Prétraite les données pour créer les matrices nécessaires."""
        print("Création de la matrice utilisateur-film...")
        # Réduire la taille des données pour l'exemple
        min_ratings = 5  # Utilisateurs ayant noté au moins 5 films
        user_counts = self.ratings['userId'].value_counts()
        valid_users = user_counts[user_counts >= min_ratings].index
        self.ratings = self.ratings[self.ratings['userId'].isin(valid_users)]
        
        self.user_movie_matrix = self.ratings.pivot(
            index='userId', 
            columns='movieId', 
            values='rating'
        ).fillna(0)
        
        print("Filtrage des films...")
        # Filtrer les films qui ont des notes
        self.movies = self.movies[self.movies['movieId'].isin(self.ratings['movieId'])].copy()
        
        print("Création de la matrice des genres...")
        # Créer la matrice des genres
        self.movie_genre_matrix = self.movies['genres'].str.get_dummies('|')
        
        print("Prétraitement terminé.")

    def train_collaborative(self, n_factors=50):
        """Entraîne le modèle de filtrage collaboratif avec SVD."""
        print(f"Entraînement du modèle SVD avec {n_factors} facteurs...")
        self.model = TruncatedSVD(n_components=n_factors, random_state=42)
        self.model.fit(self.user_movie_matrix)
        print("Entraînement terminé.")

    def recommend_collaborative(self, user_id, n=5):
        """Recommande des films basés sur le filtrage collaboratif."""
        if self.model is None:
            return []
            
        if user_id not in self.user_movie_matrix.index:
            print(f"Utilisateur {user_id} non trouvé.")
            return []
            
        # Transformer les notes de l'utilisateur
        user_ratings = self.model.transform(
            self.user_movie_matrix.loc[user_id].values.reshape(1, -1)
        )
        
        # Calculer les scores pour tous les films
        scores = np.dot(user_ratings, self.model.components_)
        
        # Obtenir les indices des n meilleurs films
        top_movie_ids = np.argsort(-scores[0])[:n]
        
        # Retourner les titres des films recommandés
        return self.movies[
            self.movies['movieId'].isin(
                self.user_movie_matrix.columns[top_movie_ids]
            )
        ]['title'].tolist()

    def recommend_by_content(self, movie_title, n=5):
        """Recommande des films basés sur la similarité du contenu."""
        if self.movie_genre_matrix is None:
            return []
            
        # Trouver l'index du film recherché
        movie_idx = self.movies[
            self.movies['title'].str.contains(movie_title, case=False, na=False)
        ].index
        
        if len(movie_idx) == 0:
            print(f"Film '{movie_title}' non trouvé.")
            return []
            
        movie_idx = movie_idx[0]
        
        # Calculer la similarité cosinus
        print("Calcul des similarités...")
        similarity = cosine_similarity(self.movie_genre_matrix)
        
        # Obtenir les indices des n films les plus similaires
        similar_indices = np.argsort(-similarity[movie_idx])[1:n+1]
        
        # Retourner les titres des films recommandés
        return self.movies.iloc[similar_indices]['title'].tolist() 