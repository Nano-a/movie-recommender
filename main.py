from controller.app import app, init_app
from visualizations.plots import plot_rating_distribution, plot_top_genres

def main():
    """Point d'entrée principal de l'application."""
    # Générer les visualisations
    plot_rating_distribution()
    plot_top_genres()
    
    # Initialiser et lancer l'application
    init_app()
    app.run(debug=True)

if __name__ == '__main__':
    main() 