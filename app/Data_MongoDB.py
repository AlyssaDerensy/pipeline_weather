# Connexion à MongoDB
from pymongo import MongoClient
import requests

API_KEY = "votre API KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Liste des 60 villes les plus peuplées de France
cities = [
    "Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier",
    "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Saint-Étienne", "Toulon",
    "Grenoble", "Dijon", "Angers", "Nîmes", "Villeurbanne", "Clermont-Ferrand", "Le Mans",
    "Aix-en-Provence", "Brest", "Tours", "Amiens", "Limoges", "Annecy", "Perpignan", "Boulogne-Billancourt",
    "Metz", "Besançon", "Orléans", "Saint-Denis", "Argenteuil", "Rouen", "Montreuil", "Mulhouse",
    "Caen", "Nancy", "Saint-Paul", "Roubaix", "Tourcoing", "Nanterre", "Avignon", "Vitry-sur-Seine",
    "Créteil", "Dunkerque", "Poitiers", "Asnières-sur-Seine", "Courbevoie", "Versailles", "Colombes",
    "Aulnay-sous-Bois", "Rueil-Malmaison", "Pau", "Aubervilliers", "Champigny-sur-Marne", "Antibes", "La Roche-sur-Foron"
]

# Connexion à MongoDB
client = MongoClient("mongodb://mongodb:27017")
db = client["meteo"]
collection = db["villes"]

# Récupération des données de l'API
for city in cities:
    try:
        response = requests.get(BASE_URL, params={
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "fr"
        })
        if response.status_code == 200:
            data = response.json()
            
            # Document pour MongoDB
            city_data = {
                "Ville": city,
                "ID_OpenWeather": data["id"],  # Identifiant unique fourni par l'API
                "Latitude": data["coord"]["lat"],
                "Longitude": data["coord"]["lon"],
                "Temperature": data["main"]["temp"],
                "Description": data["weather"][0]["description"],
                "Humidité": data["main"]["humidity"],
                "Pression": data["main"]["pressure"],
                "Vent": data["wind"]["speed"],
                "timestamp" : data["dt"]
            }
            
            # Insérer ou mettre à jour dans MongoDB
            collection.update_one(
                {"ID_OpenWeather": data["id"]},  # Critère d'identification unique
                {"$set": city_data},
                upsert=True
            )
            print(f"Données pour {city} insérées ou mises à jour.")
        else:
            print(f"Erreur pour {city}: {response.status_code}")
    except Exception as e:
        print(f"Erreur pour {city}: {e}")

print("Insertion terminée.")


print(client.list_database_names())  # Liste des bases de données disponibles
db = client["meteo"]
print(db.list_collection_names())   # Liste des collections dans la base "meteo"
collection = db["villes"]
print(collection.count_documents({}))  # Nombre de documents dans la collection "villes"
print("Documents dans la collection après insertion:")
print(list(collection.find()))