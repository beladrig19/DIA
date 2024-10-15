import openrouteservice
import pandas as pd
import time

# Initialiser le client OpenRouteService avec votre clé API
client = openrouteservice.Client(key='5b3ce3597851110001cf6248a2d67d3b0a9e4917b11f1e83ab06a71c')

# Charger le fichier contenant les codes postaux et leurs coordonnées
file_path = 'codePostauxBourgogneFrancheComte.xlsx'
data = pd.read_excel(file_path)

# Extraire les coordonnées géographiques
data['geo_point_2d'] = data['geo_point_2d'].apply(lambda x: tuple(map(float, x.split(','))))
coordinates = data[['Code Postal', 'geo_point_2d']]

# Préparer une matrice pour les distances
distance_matrix = pd.DataFrame(index=coordinates['Code Postal'], columns=coordinates['Code Postal'])

# Fonction pour obtenir la distance via l'API
def get_distance(coord1, coord2):
    try:
        routes = client.directions([coord1, coord2])
        distance = routes['routes'][0]['summary']['distance']  # en mètres
        return distance / 1000  # Convertir en km
    except:
        return None

# Boucler sur chaque paire de codes postaux pour calculer les distances
for i, (code_i, coord_i) in enumerate(coordinates['geo_point_2d'].items()):
    for j, (code_j, coord_j) in enumerate(coordinates['geo_point_2d'].items()):
        if i != j and pd.isna(distance_matrix.at[code_i, code_j]):
            distance = get_distance(coord_i, coord_j)
            distance_matrix.at[code_i, code_j] = distance
            distance_matrix.at[code_j, code_i] = distance  # Symétrie
            time.sleep(1)  # Pause pour éviter de dépasser le quota API

# Enregistrer la matrice de distances
distance_matrix.to_excel('distances_routieres_bourgogne_franche_comte.xlsx')
