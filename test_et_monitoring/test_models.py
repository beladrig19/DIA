import pytest
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from data_utils import load_and_prepare_data

# Charger et préparer les données
X_train, X_test, y_train, y_test, label_encoders = load_and_prepare_data()

# Liste des modèles avec hyperparamètres différents
models = [
    {"name": "RandomForest", "model": RandomForestClassifier(n_estimators=10, max_depth=2, random_state=42)},
    {"name": "LogisticRegression", "model": LogisticRegression(max_iter=500, random_state=42)},
    {"name": "SVC", "model": SVC(kernel="rbf", C=10.0, random_state=42)}
]

# Test pour vérifier que les modèles s'entraînent correctement
@pytest.mark.parametrize("model_info", models)
def test_model_training(model_info):
    model = model_info["model"]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert len(y_pred) == len(y_test), "Le modèle n'a pas produit la bonne taille de prédictions"