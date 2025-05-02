def test_environment():
    """Test basique pour vérifier que l'environnement de test fonctionne."""
    assert True

def test_import_dependencies():
    """Test pour vérifier que les dépendances principales sont correctement installées."""
    import pandas as pd
    import numpy as np
    import sklearn
    import flask
    import matplotlib
    assert pd.__version__
    assert np.__version__
    assert sklearn.__version__
    assert flask.__version__
    assert matplotlib.__version__ 