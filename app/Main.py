import subprocess
import os

from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017")
client = MongoClient(mongo_uri)

print("Avant le print du répertoire")
# Définir le chemin du dossier contenant les scripts
app_directory = os.path.join(os.getcwd(), "app")

# Exécuter Data_MongoDB.py
try:
    subprocess.run(["python3", os.path.join(app_directory, "Data_MongoDB.py")], check=True)
    print("Data_MongoDB.py a été exécuté avec succès.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'exécution de Data_MongoDB.py : {e}")
    exit(1)  # Arrêter le script si une erreur survient

# Exécuter app.py
print(os.path.join(app_directory,"Visu.py"))
print(os.path.join(app_directory, "Data_MongoDB.py"))
print (app_directory)
try:
    subprocess.run(["python3",  os.path.join(app_directory,"Visu.py")], check=True)
    print("app.py a été exécuté avec succès.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'exécution de Visu.py : {e}")
