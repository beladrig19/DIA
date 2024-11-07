import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score
from data_utils import load_and_prepare_data

# Charger et préparer les données
X_train, X_test, y_train, y_test, label_encoders = load_and_prepare_data()

# Liste des modèles avec hyperparamètres différents
models = [
    {"name": "RandomForest", "model": RandomForestClassifier(n_estimators=10, max_depth=2, random_state=42)},
    {"name": "LogisticRegression", "model": LogisticRegression(max_iter=500, random_state=42)},
    {"name": "SVC", "model": SVC(kernel="rbf", C=10.0, random_state=42)}
]

# Démarrer MLflow
mlflow.end_run()  # Terminer toute session MLflow en cours

# Boucle sur chaque modèle pour les entraîner et enregistrer les résultats
for model_info in models:
    model_name = model_info["name"]
    model = model_info["model"]

    # Démarrer une nouvelle session MLflow pour chaque modèle
    with mlflow.start_run(run_name=model_name):
        # Entraîner le modèle
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Calculer les métriques
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)

        # Loguer le nom du modèle et les hyperparamètres
        mlflow.log_param("model_name", model_name)
        if model_name == "RandomForest":
            mlflow.log_param("n_estimators", model.n_estimators)
            mlflow.log_param("max_depth", model.max_depth)
        elif model_name == "LogisticRegression":
            mlflow.log_param("max_iter", model.max_iter)
        elif model_name == "SVC":
            mlflow.log_param("kernel", model.kernel)
            mlflow.log_param("C", model.C)

        # Loguer les métriques
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)

        print(f"Modèle {model_name} - Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}")

print("Les modèles ont été enregistrés dans MLflow pour comparaison.")