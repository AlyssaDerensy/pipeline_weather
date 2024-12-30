 # Weather Data Pipeline

## Description
Ce projet consiste à créer un pipeline de données météorologiques en utilisant les technologies suivantes :
- **Python**
- **MongoDB** : Stockage des données météorologiques.
- **Flask, Dash & Plotly** : Création de l'application, analyse et visualisation des données à l'aide d'un tableau de bord interactif.
- **Docker** : Conteneurisation et déploiement l'application.

L'objectif est de collecter des données météorologiques via l'API OpenWeather, de les stocker dans MongoDB, et de les rendre accessibles via une API REST avec des options de visualisation.

---

## Configuration initiale

### Prérequis
Assurez-vous d'avoir installé les outils suivants :
1. **Python 3.x** : Téléchargez depuis [python.org](https://www.python.org/).
2. **MongoDB** : Téléchargez depuis [mongodb.com](https://www.mongodb.com/try/download/community).
3. **Docker Desktop** : Téléchargez depuis [docker.com](https://www.docker.com/products/docker-desktop).
4. **IDE Python** : Comme Visual Studio Code depuis [code.visualstudio.com](https://code.visualstudio.com/).

### Structure du projet
Voici la structure actuelle du projet :
```plaintext
weather_pipeline/
├── app/
|   ├── static/                 # Fichiers statiques comme la documentation
|   |   ├── documentation.pdf                 
|   ├── Data_MongoDB.py         # Algorithme de récupération des données à partir de l'API
|   ├── Main.py                 
|   ├── Visu.py                 # Définition de l'application dash et des différents visuels
├── templates/              # Modèles HTML pour le front-end
├── Data/                   # Données brutes ou fichiers de configuration
|   ├── city.list.json
|   ├── ID_Ville_France.csv
├── Dockerfile              # Fichier Docker pour conteneuriser l'application
├── docker-compose.yml      # Configuration pour orchestrer MongoDB et Flask
├── requirements.txt        # Liste des dépendances Python
└── README.md              
```

### Installation

#### 1. Cloner le projet
Cloner ce dépôt sur votre machine locale :
```bash
git clone https://github.com/AlyssaDerensy/pipeline_weather
cd weather_pipeline
```

## 1. Utilisation

### 1.1 Ajout de l'API Key

Rendez vous sur https://openweathermap.org/api pour vous créer un compte et demander une API Key, lorsque celle-ci est activée, dans le fichier "Data_MongoDB.py" (ligne 5), modifier cette ligne de code en remplaçant avec votre API Key :

```Bash
    API_KEY = "votre API KEY"
```


### 1.2 Conteneurisation avec Docker
Démarrez Docker Desktop <br>
Dans un terminal python, positionnez-vous dans la racine du projet, lancez :

```bash
docker-compose up --build
```

Un conteneur va apparaître dans Docker Desktop, vous pouvez accéder au lien local du tableau de bord en cliquant dessus puis en appuyant sur le port de "pipeline_weather-main" (8050:8050). <br>

Sinon vous pouvez directement vous rendre sur http://localhost:8050/ dans votre navigateur. 

## 2. Fonctionnalité

- Tableau de bord dynamique

---

## Auteurs
- **Alyssa, Alexy, Solène, Maryline, Kenzo**


Chef de projet : Alyssa DERENSY <br>
Développeur Backend : Kenzo SALAUN, Maryline FONTA , Alyssa DERENSY <br>
Intégrateur API : Solène ISSANES <br>
Spécialiste DevOps :  Maryline FONTA, Alyssa DERENSY,  Alexy GABORIAUD <br>
Analyste de données : Maryline FONTA, Solène ISSANES <br>