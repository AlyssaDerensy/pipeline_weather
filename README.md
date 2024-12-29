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
3. **Docker Desktop** : Téléchargez depuis [docker.com](https://www.docker.com/products/docker-desktop).
4. **IDE Python** : Comme Visual Studio Code depuis [code.visualstudio.com](https://code.visualstudio.com/).

### Installation

#### 1. Cloner le projet
Cloner ce dépôt sur votre machine locale :
```bash
git clone https://github.com/AlyssaDerensy/pipeline_weather
cd weather_pipeline
```

#### 2. Utilisation

##### 2.1 Conteunarisation avec Docker
Démarrez Docker Desktop <br>
Dans un terminal python, positionnez-vous dans la racine du projet, lancez :

```bash
docker-compose up --build
```

Un conteneur va apparaître dans Docker Desktop, vous pouvez accéder aux lien du tableau de bord en cliquant dessus et en cliquant sur le port de "pipeline_weather_4" (8050:8050)

#### 3. Fonctionnalité

- Ajout de données métérologies du jour-même pour les 60 villes les plus peuplés de France

#### 3. Structure du projet
Voici la structure actuelle du projet :
```plaintext
weather_pipeline/
├── app/
|   ├── static/                 # Fichiers statiques comme CSS ou JavaScript
├── templates/              # Modèles HTML pour le front-end
├── Data/                   # Données brutes ou fichiers de configuration
├── Dockerfile              # Fichier Docker pour conteneuriser l'application
├── docker-compose.yml      # Configuration pour orchestrer MongoDB et Flask
├── requirements.txt        # Liste des dépendances Python
└── README.md               # Documentation du projet
```

---

## Auteurs
- **Alyssa, Alexy, Solène, Maryline, Kenzo**


Chef de projet : Alyssa DERENSY <br>
Développeur Backend : Kenzo SALAUN, Maryline FONTA , Alyssa DERENSY <br>
Intégrateur API : Solène ISSANES <br>
Spécialiste DevOps :  Maryline FONTA, Alyssa DERENSY,  Alexy GABORIAUD <br>
Analyste de données : Maryline FONTA, Solène ISSANES <br>