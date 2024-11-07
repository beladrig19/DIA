# data_utils.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_prepare_data():
    # Charger le dataset
    url = "https://raw.githubusercontent.com/RiccardoAncarani/mushrooms-machine-learning/refs/heads/master/mushrooms.csv"
    data = pd.read_csv(url)

    # Encoder toutes les colonnes catégoriques en valeurs numériques
    label_encoders = {}
    for column in data.columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

    # Séparer les caractéristiques (X) et la cible (y)
    X = data.drop("class", axis=1)
    y = data["class"]

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test, label_encoders
