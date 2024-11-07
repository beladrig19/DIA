import schedule
import time
import subprocess

# Fonction pour exécuter les tests avec pytest et enregistrer les résultats
def run_tests():
    print("Exécution des tests unitaires en cours...")
    try:
        # Exécuter pytest et capturer la sortie
        result = subprocess.run(["pytest", "test_models.py"], capture_output=True, text=True)

        # Enregistrer la sortie dans un fichier de log
        with open("test_results_log.txt", "a") as log_file:
            log_file.write("\n--- Exécution des Tests à " + time.strftime("%Y-%m-%d %H:%M:%S") + " ---\n")
            log_file.write(result.stdout)
            log_file.write("\n--- Fin de l'Exécution ---\n")

        print("Résultats des tests enregistrés dans test_results_log.txt")

    except Exception as e:
        print(f"Erreur lors de l'exécution des tests : {e}")

# Planifier l'exécution de la fonction toutes les 30 minutes
schedule.every(30).minutes.do(run_tests)

# Boucle infinie pour exécuter le planificateur
while True:
    schedule.run_pending()
    time.sleep(1)  # Attendre une seconde avant de vérifier à nouveau