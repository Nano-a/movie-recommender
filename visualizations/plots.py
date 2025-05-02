import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def plot_rating_distribution(ratings_path='data/ratings.csv', save_path='visualizations/rating_distribution.png'):
    """Génère un graphique de la distribution des notes."""
    # Lire les données
    ratings = pd.read_csv(ratings_path)
    
    # Créer le graphique
    plt.figure(figsize=(10, 6))
    plt.hist(ratings['rating'], bins=10, edgecolor='black', color='#3498db')
    plt.title('Distribution des notes des films', fontsize=14)
    plt.xlabel('Note', fontsize=12)
    plt.ylabel('Nombre de notes', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Sauvegarder le graphique
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_rmse_vs_factors(n_factors_list, rmse_list, save_path='visualizations/rmse_plot.png'):
    """Génère un graphique du RMSE en fonction du nombre de facteurs."""
    plt.figure(figsize=(10, 6))
    plt.plot(n_factors_list, rmse_list, marker='o', color='#e74c3c', linewidth=2)
    plt.title('RMSE vs Nombre de facteurs', fontsize=14)
    plt.xlabel('Nombre de facteurs', fontsize=12)
    plt.ylabel('RMSE', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Sauvegarder le graphique
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_top_genres(movies_path='data/movies.csv', save_path='visualizations/top_genres.png'):
    """Génère un graphique des genres les plus populaires."""
    # Lire les données
    movies = pd.read_csv(movies_path)
    
    # Compter les genres
    genres = movies['genres'].str.split('|', expand=True).stack()
    genre_counts = genres.value_counts().head(10)
    
    # Créer le graphique
    plt.figure(figsize=(12, 6))
    genre_counts.plot(kind='bar', color='#2ecc71')
    plt.title('Top 10 des genres les plus populaires', fontsize=14)
    plt.xlabel('Genre', fontsize=12)
    plt.ylabel('Nombre de films', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    
    # Sauvegarder le graphique
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close() 