import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

def split_data(ratings, test_size=0.2):
    """Divise les données en ensembles d'entraînement et de test."""
    train = ratings.sample(frac=1-test_size, random_state=42)
    test = ratings.drop(train.index)
    return train, test

def calculate_rmse(recommender, test_ratings):
    """Calcule le RMSE (Root Mean Square Error) du modèle."""
    predictions = []
    actual = []
    
    for _, row in test_ratings.iterrows():
        user_id = row['userId']
        movie_id = row['movieId']
        actual_rating = row['rating']
        
        # Vérifier si l'utilisateur et le film existent dans la matrice
        if (user_id in recommender.user_movie_matrix.index and 
            movie_id in recommender.user_movie_matrix.columns):
            
            # Prédire la note
            user_ratings = recommender.model.transform(
                recommender.user_movie_matrix.loc[user_id].values.reshape(1, -1)
            )
            scores = np.dot(user_ratings, recommender.model.components_)
            movie_idx = recommender.user_movie_matrix.columns.get_loc(movie_id)
            predicted_rating = scores[0][movie_idx]
            
            predictions.append(predicted_rating)
            actual.append(actual_rating)
    
    if not predictions:
        return 0
        
    return np.sqrt(mean_squared_error(actual, predictions)) 