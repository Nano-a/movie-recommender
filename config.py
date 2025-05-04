"""
Configuration du système de recommandation de films.
"""

# Chemins des fichiers
DATA_DIR = "data"
MODEL_DIR = "model"
VISUALIZATION_DIR = "visualizations"

# Paramètres du modèle
N_FACTORS = 100
RANDOM_STATE = 42
TEST_SIZE = 0.2

# Paramètres de l'API
API_HOST = "0.0.0.0"
API_PORT = 5000
DEBUG = False

# Paramètres de cache
CACHE_TIMEOUT = 3600  # 1 heure

# Paramètres de logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" 