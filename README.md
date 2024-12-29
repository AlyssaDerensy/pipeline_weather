 # Weather Data Pipeline

## Description
Ce projet consiste à créer un pipeline de données météorologiques en utilisant les technologies suivantes :
- **Python**
- **Flask** : pour exposer une API REST.
- **MongoDB** : pour stocker les données météorologiques.
- **Dash & Plotly** : pour analyser et visualiser les données à l'aide d'un tableau de bord interactif.
- **Docker** : pour conteneuriser et déployer l'application.

L'objectif est de collecter des données météorologiques via l'API OpenWeather, de les stocker dans MongoDB, et de les rendre accessibles via une API REST avec des options de visualisation.

---

## Configuration initiale

### Prérequis
Assurez-vous d'avoir installé les outils suivants :
1. **Python 3.x** : Téléchargez depuis [python.org](https://www.python.org/).
2. **MongoDB** : Téléchargez depuis [mongodb.com](https://www.mongodb.com/try/download/community).
3. **Docker** : Téléchargez depuis [docker.com](https://www.docker.com/products/docker-desktop).
4. **Pip** : Géré par défaut avec Python pour installer les bibliothèques.

### Installation

#### 1. Cloner le projet
Cloner ce dépôt sur votre machine locale :
```bash
git clone <url-du-dépôt>
cd weather_pipeline
```

#### 2. Configurer l'environnement Python
Créer et activer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate   # Sous macOS/Linux
venv\Scripts\activate      # Sous Windows
```

#### 3. Installer les dépendances
Installez les bibliothèques nécessaires :
```bash
pip install flask pymongo requests dash plotly
```

#### 4. Lancer MongoDB
Démarrez le serveur MongoDB localement ou configurez un cluster cloud via [MongoDB Atlas](https://www.mongodb.com/atlas).

#### 5. Structure du projet
Voici la structure actuelle du projet :
```plaintext
weather_pipeline/
├── app/
│   ├── __init__.py         # Initialisation de l'application Flask
│   ├── routes.py           # Les routes Flask
│   ├── database.py         # Gestion des interactions avec MongoDB
├── static/                 # Fichiers statiques comme CSS ou JavaScript
├── templates/              # Modèles HTML pour le front-end
├── data/                   # Données brutes ou fichiers de configuration
├── Dockerfile              # Fichier Docker pour conteneuriser l'application
├── docker-compose.yml      # Configuration pour orchestrer MongoDB et Flask
├── requirements.txt        # Liste des dépendances Python
└── README.md               # Documentation du projet
```

#### 6. Lancer l'application Flask (temporaire)
Pour tester Flask (avant l'implémentation des routes) :
```bash
python app/__init__.py
```

---

## Prochaines étapes
1. Implémenter un script pour interroger l'API OpenWeather et collecter des données.
2. Configurer MongoDB pour stocker ces données.
3. Créer un tableau de bord interactif avec Dash et Plotly.
4. Déployer l'application avec Docker.

---

## Auteurs
- **Alyssa, Alexy, Solène, Maryline, Kenzo**


1. Chef de Projet : (Alyssa)
    o Coordination des tâches.
    o Rédaction de la documentation.
2. Développeur Backend : (Alexy)
    o Implémentation des routes Flask.
    o Gestion des interactions avec MongoDB.
3. Intégrateur API : (Solène)
    o Écriture du script de collecte de données depuis l’API Open Weather.
    o Gestion des erreurs et des cas limites.
4. Spécialiste DevOps : (Kenzo)
    o Configuration et optimisation des fichiers Docker.
    o Gestion du déploiement.
5. Analyste de Données : (Maryline)
    o Création des visualisations et du tableau de bord interactif.
    o Analyse des données pour produire des insights pertinents.