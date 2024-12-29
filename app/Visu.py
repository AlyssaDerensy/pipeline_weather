from dash import Dash, html, dcc, Input, Output
from dash import dash_table
import pandas as pd
from pymongo import MongoClient
import plotly.express as px
from dash_ag_grid import AgGrid
from flask import send_from_directory
from datetime import datetime

import os

# Date du jour
today_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(today_date)

# Connexion à MongoDB
client = MongoClient("mongodb://mongodb:27017/")
db = client["meteo"]
collection = db["villes"]



# Fonction pour récupérer les données depuis MongoDB
def get_data_from_mongodb():
    data = list(collection.find({}))  # Récupération des documents
    df = pd.DataFrame(data)
    if "_id" in df.columns:
        df.drop("_id", axis=1, inplace=True)  # Supprimer la colonne MongoDB "_id"
    
    # Modifier la valeur de Longitude et la latitude pour Brest
    df.loc[df['Ville'] == "Brest", 'Longitude'] = -4.5000
    df.loc[df['Ville'] == "Brest", 'Latitude'] = 48.4000
    
    return df
print("debut init dash")

# Initialisation de l'application Dash
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Visualisation Météo"
server=app.server
print("init dash")

@app.server.route('/')
def hello():
    return "Bonjour, l'API fonctionne !"

# Définir la route Flask pour servir le fichier PDF
# Ajouter une route Flask pour le téléchargement

from flask import Flask, send_file, make_response
import os

# Définir le chemin du dossier static
STATIC_DIR = os.path.join(os.getcwd(), 'static')

# Ajouter une route Flask pour le téléchargement
@app.server.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory(STATIC_DIR, filename, as_attachment=True)




# Layout de la page d'accueil avec alignement à gauche dans le premier cadre
app.Accueil_layout = html.Div([
    
    # Titre principal de la page
    html.Div([
        html.H1("Bienvenue sur le Mini-Projet : ", style={"textAlign": "center", "color": "#4a4e69", "marginBottom": "10px"}),
        html.H1("Création d'un Pipeline de données météorologiques avec Flask et MongoDB", 
                style={"textAlign": "center", "color": "#4a4e69", "marginBottom": "30px"})
    ]),

    # Section des cadres
    html.Div([
        # Cadre de gauche : Informations générales
        html.Div([
            html.H2(html.U("Informations générales"), style={"color": "#4a4e69", "marginBottom": "15px"}),
            html.H3([html.U("Source :"), " openweathermap.org"], style={"color": "#4a4e69", "marginBottom": "10px"}),
            html.H3([html.U("Périmètre d'étude :"), " les 60 villes les plus peuplées de France"], style={"color": "#4a4e69", "marginBottom": "10px"}),


            html.Div([
            html.Div([
                html.H3(html.U('Documentation :'), style={"marginRight": "10px", "display": "inline", "color": "#4a4e69"}),
                html.A('Télécharger le PDF', href='/static/documentation.pdf', target='_blank', style={"fontSize": "18px", "color": "#3498db", "textDecoration": "underline", "display": "inline"})
            ], style={"display": "flex", "alignItems": "center", "marginBottom": "10px"})
])



        ], style={"flex": "1", "padding": "20px", "border": "1px solid #4a4e69", "borderRadius": "10px", "backgroundColor": "#e9ecef", "textAlign": "left"}),  # Alignement à gauche

        # Cadre de droite : Membres de l'équipe
        html.Div([
            html.H2(html.U("Membres de l'équipe"), style={"color": "#4a4e69", "marginBottom": "15px"}),
            html.Ul([
                html.Li("Alexy GABORIAUD", style={"fontSize": "18px", "marginBottom": "5px"}),
                html.Li("Alyssa DERENSY", style={"fontSize": "18px", "marginBottom": "5px"}),
                html.Li("Kenzo SALAUN", style={"fontSize": "18px", "marginBottom": "5px"}),
                html.Li("Maryline FONTA", style={"fontSize": "18px", "marginBottom": "5px"}),
                html.Li("Solène ISSANES", style={"fontSize": "18px", "marginBottom": "5px"})
            ], style={"listStyleType": "none", "paddingLeft": "0"}),

        ], style={"flex": "1", "padding": "20px", "border": "1px solid #4a4e69", "borderRadius": "10px", "backgroundColor": "#e9ecef"}),

        # Cadre de droite : École et professeur
        html.Div([
            html.H2(html.U("École"), style={"color": "#4a4e69", "marginBottom": "15px"}),
            html.P("PMN (La Passerelle des Métiers du Numérique)", style={"fontSize": "20px", "color": "#222", "marginBottom": "10px"}),
            html.P("DAN25.1 - Data Analyst. 2024-2025", style={"fontSize": "20px", "color": "#222", "marginBottom": "20px"}),

            html.H3("Encadré par :", style={"color": "#4a4e69", "marginBottom": "10px"}),
            html.P("Mokhtar SELLAMI", style={"fontSize": "20px", "fontWeight": "bold", "color": "#222"})
        ], style={"flex": "1", "padding": "20px", "border": "1px solid #4a4e69", "borderRadius": "10px", "backgroundColor": "#e9ecef"})
    ], style={"display": "flex", "gap": "20px", "marginBottom": "30px"}),


    # Section de navigation sous les cadres pour accéder aux différentes pages
    html.Div([
        html.H3("Navigation vers les différentes pages :", style={"color": "#4a4e69", "marginBottom": "10px"}),
        html.Div([
            dcc.Link("Dashboard global", href='/Dashboard', style={"color": "#3498db", "fontSize": "18px", "textDecoration": "underline"}), 
            dcc.Link("Top 10 des villes selon leur température du jour", href='/Top10', style={ "color": "#3498db", "fontSize": "18px", "textDecoration": "underline"}),
            dcc.Link("Nuage de points des températures du jour par ville", href='/Nuage_Temp', style={ "color": "#3498db", "fontSize": "18px", "textDecoration": "underline"}),
            dcc.Link("Comparaisons entre la température du jour, la vitesse du vent et la latitude", href='/Comparaison', style={"color": "#3498db", "fontSize": "18px", "textDecoration": "underline"}),
            dcc.Link("Tableau récapitulatif des données météorologiques", href='/Tableau', style={"color": "#3498db", "fontSize": "18px", "textDecoration": "underline"})
        ], style={"display": "flex", "flexDirection": "column", "alignItems": "center", "gap": "10px"})
    ], style={"textAlign": "center", "marginTop": "20px"})
])
# Page : Top 10 des villes les plus chaudes et les plus froides
Top10_layout = html.Div([

    # Titre de la page
    html.H1("Top 10 des villes selon leur température", style={"textAlign": "center"}),

    # Date du jour
    html.Div(f"Date du jour : {today_date}", style={"textAlign": "center", "marginBottom": "20px", "fontSize": "18px", "color": "#222"}),

    # Lien pour revenir à la page d'accueil
    html.Div([dcc.Link("Retour à la page d'accueil", href='/')]),

    # Section pour les villes les plus chaudes
    html.Div([

        # Titre pour les villes les plus chaudes
        html.H2("Top 10 des villes les plus chaudes"),

        # Section contenant le tableau et le box plot pour les villes les plus chaudes
        html.Div([

            # Tableau des 10 villes les plus chaudes (assurez-vous que cet ID soit bien celui du tableau)
            html.Div(id="Top10-hot-content", style={
                "width": "50%",  # Largeur du tableau
                "paddingRight": "10px",  # Espace entre le tableau et le box plot
                "overflowX": "auto"  # Ajoute un défilement horizontal si le tableau est trop large
            }),

            # Box plot à droite (plus petit)
            html.Div([
                dcc.Graph(id="temperature-hot-boxplot")
            ], style={
                "width": "50%",  # Largeur du box plot
                "overflowX": "auto"  # Ajoute un défilement horizontal si nécessaire
            })

        ], style={
            "display": "flex",  # Flexbox pour aligner les éléments côte à côte
            "justifyContent": "space-between",  # Espacement entre le tableau et le graphique
            "gap": "10px",  # Espace entre les éléments
            "maxWidth": "100%",  # Largeur maximale en pourcentage de l'écran
            "width": "100%"  # Ajuste la largeur totale à 100%
        }),

        # Input caché pour déclencher le callback
        dcc.Input(id="Top10-hot-load", type="hidden", value=1)  # Déclenchement automatique du callback

    ], style={"marginBottom": "40px"}),  # Marge entre les sections

    # Section pour les villes les plus froides
    html.Div([

        # Titre pour les villes les plus froides
        html.H2("Top 10 des villes les plus froides"),

        # Section contenant le tableau et le box plot pour les villes les plus froides
        html.Div([

            # Tableau des 10 villes les plus froides
            html.Div(id="Top10-cold-content", style={
                "width": "50%",  # Largeur du tableau
                "paddingRight": "10px",  # Espace entre le tableau et le box plot
                "overflowX": "auto"  # Ajoute un défilement horizontal si le tableau est trop large
            }),

            # Box plot à droite (plus petit)
            html.Div([
                dcc.Graph(id="temperature-cold-boxplot")
            ], style={
                "width": "50%",  # Largeur du box plot
                "overflowX": "auto"  # Ajoute un défilement horizontal si nécessaire
            })

        ], style={
            "display": "flex",  # Flexbox pour aligner les éléments côte à côte
            "justifyContent": "space-between",  # Espacement entre le tableau et le graphique
            "gap": "10px",  # Espace entre les éléments
            "maxWidth": "100%",  # Largeur maximale en pourcentage de l'écran
            "width": "100%"  # Ajuste la largeur totale à 100%
        }),

        # Input caché pour déclencher le callback
        dcc.Input(id="Top10-cold-load", type="hidden", value=1)  # Déclenchement automatique du callback

    ])
])

# Callback pour générer le boxplot des villes les plus chaudes
@app.callback(
    Output("temperature-hot-boxplot", "figure"),
    Input("Top10-hot-load", "value")  # Déclenchement lorsque la page est chargée
)
def generate_temperature_hot_boxplot(_):
    df = get_data_from_mongodb()  # Ajustez cette fonction si nécessaire

    # Filtrer pour les 10 villes les plus chaudes
    top_10_hot_cities = df.nlargest(10, "Temperature")

    # Générer le boxplot pour les 10 villes les plus chaudes
    fig_box_hot = px.box(
        top_10_hot_cities,
        y="Temperature",
        title="Boxplot des températures des 10 villes les plus chaudes",
        labels={"Temperature": "Température (°C)"}
    )
    

    # Mise à jour du layout pour ajuster la largeur et la hauteur
    fig_box_hot.update_layout(
        xaxis_title="Indicateurs",
        yaxis_title="Température (°C)",
        showlegend=False,
        margin=dict(l=50, r=50, t=50, b=50),  # Marges
        height=400,  # Hauteur du graphique
        width=600    # Largeur du graphique
    )

    return fig_box_hot


# Callback pour générer le boxplot des villes les plus froides
@app.callback(
    Output("temperature-cold-boxplot", "figure"),
    Input("Top10-cold-load", "value")  # Déclenchement lorsque la page est chargée
)
def generate_temperature_cold_boxplot(_):
    df = get_data_from_mongodb()  # Ajustez cette fonction si nécessaire

    # Filtrer pour les 10 villes les plus froides
    top_10_cold_cities = df.nsmallest(10, "Temperature")

    # Générer le boxplot pour les 10 villes les plus froides
    fig_box_cold = px.box(
        top_10_cold_cities,
        y="Temperature",
        title="Boxplot des températures des 10 villes les plus froides",
        labels={"Temperature": "Température (°C)"}
    )

    fig_box_cold.update_traces(
    hovertemplate="<b>Température :</b> %{y}°C<br><b>Ville :</b> %{text}<extra></extra>",
    text=top_10_cold_cities["Ville"]  # Afficher les noms des villes dans l'info-bulle
)


    # Mise à jour du layout pour ajuster la largeur et la hauteur
    fig_box_cold.update_layout(
        xaxis_title="Indicateurs",
        yaxis_title="Température (°C)",
        showlegend=False,
        margin=dict(l=50, r=50, t=50, b=50),  # Marges
        height=400,  # Hauteur du graphique
        width=600    # Largeur du graphique
    )

    return fig_box_cold


# Callback pour générer le tableau des 10 villes les plus chaudes
@app.callback(
    Output("Top10-hot-content", "children"),
    Input("Top10-hot-load", "value")
)
def generate_top10_hot_table(_):
    df = get_data_from_mongodb()  # Ajustez cette fonction si nécessaire

    # Filtrer pour les 10 villes les plus chaudes
    top_10_hot_cities = df.nlargest(10, "Temperature")
    top_10_hot_cities = top_10_hot_cities.iloc[:, ::-1]  # Inversion de l'ordre des colonnes

    # Créer le tableau des villes les plus chaudes
    return dash_table.DataTable(
        data=top_10_hot_cities.drop(columns=["timestamp", "ID_OpenWeather"]).to_dict('records'),
        columns=[{"name": col, "id": col} for col in top_10_hot_cities.columns if col not in ["timestamp", "ID_OpenWeather"]],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '10px'},
        style_header={"fontWeight": "bold", "textAlign": "center", "backgroundColor": "#FFD6D6"},  # Fond rosé pour l'en-tête
        style_data={"backgroundColor": "#FFEFEF"},  # Fond rosé clair pour les données
    )


# Callback pour générer le tableau des 10 villes les plus froides
@app.callback(
    Output("Top10-cold-content", "children"),
    Input("Top10-cold-load", "value")
)
def generate_top10_cold_table(_):
    df = get_data_from_mongodb()  # Ajustez cette fonction si nécessaire

    # Filtrer pour les 10 villes les plus froides
    top_10_cold_cities = df.nsmallest(10, "Temperature")
    top_10_cold_cities = top_10_cold_cities.iloc[:, ::-1]  # Inversion de l'ordre des colonnes

    # Créer le tableau des villes les plus froides
    return dash_table.DataTable(
        data=top_10_cold_cities.drop(columns=["timestamp", "ID_OpenWeather"]).to_dict('records'),
        columns=[{"name": col, "id": col} for col in top_10_cold_cities.columns if col not in ["timestamp", "ID_OpenWeather"]],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '10px'},
        style_header={
            "fontWeight": "bold",
            "textAlign": "center",
            "backgroundColor": "#D6EAF8"  # Couleur de fond bleutée pour les en-têtes
        },
        style_data={
            "backgroundColor": "#EBF5FB",  # Couleur de fond bleu clair pour les données
            "textAlign": "center"  # Centrage horizontal des cellules
        }
    )


# Page 2 : Températures selon les villes
Nuage_Temp_layout = html.Div([
    html.H1("Visualisation des températures par ville", style={"textAlign": "center"}),
    html.Div(f"Date du jour : {today_date}", style={"textAlign": "center", "marginBottom": "20px", "fontSize": "18px", "color": "#222"}),

    # Lien pour revenir à la page d'accueil
    html.Div([dcc.Link("Retour à la page d'accueil", href='/')]),

    # Option pour choisir entre l'ensemble des données ou une sélection de villes
    html.Div([
        html.H3("Sélectionnez une option :"),
        dcc.RadioItems(
            id="data-selection",
            options=[
                {"label": "Visualiser l'ensemble des données", "value": "all"},
                {"label": "Visualiser les données pour une sélection de villes", "value": "selected"}
            ],
            value="all",
            style={"marginBottom": "20px"}
        )
    ]),

    # Liste déroulante pour sélectionner une ou plusieurs villes
    html.Div([
        html.H3("Sélectionnez des villes pour visualiser les données :"),
        dcc.Dropdown(
            id="city-dropdown",
            multi=True,
            placeholder="Sélectionnez une ou plusieurs villes",
        )
    ]),

    # Conteneur pour le graphique
    html.Div(id="temperature-graph"),

    # Conteneur pour le tableau
    html.Div(id="temperature-table"),
])

# Charger les données de MongoDB
df = get_data_from_mongodb()


# Page 3 : Comparaison entre la température, la vitesse du vent et la latitude ---
# Préparation du layout de la page
Comparaison_layout = html.Div([
    html.H1("Comparaisons entre la température du jour, la vitesse du vent et la latitude", style={"textAlign": "center"}),
    html.Div(f"Date du jour : {today_date}", style={"textAlign": "center", "marginBottom": "20px", "fontSize": "18px", "color": "#222"}),

    # Lien pour revenir à la page d'accueil
    html.Div([dcc.Link("Retour à la page d'accueil", href='/')]),

    # Vérification de la structure des données
    html.Div(id='debug-info', style={'display': 'none'}, children=[str(df.head())]),

    # Graphique de la Comparaison entre la température et la vitesse du vent
    html.H2("Comparaison entre la température et la vitesse du vent"),
    dcc.Graph(
        id="temperature-wind-correlation",
        figure=px.scatter(
            df,
            x="Temperature",
            y="Vent",
            color="Ville",
            title="Comparaison entre la température et la vitesse du vent",
            labels={"Temperature": "Température", "Vent": "Vitesse du vent"}
        )
    ),

    # Graphique de la Comparaison entre la température et la latitude
    html.H2("Comparaison entre la température et la latitude"),
    dcc.Graph(
        id="temperature-latitude-correlation",
        figure=px.scatter(
            df,
            x="Temperature",
            y="Latitude",
            color="Ville",
            title="Comparaison entre la température et la latitude",
            labels={"Température (°C)": "Température", "Latitude": "Latitude"}
        )
    ),
])


# Page 4 : Tableau global de toutes les villes

# Calculer les occurrences de la variable "Description"
description_counts = df["Description"].value_counts()

# Créer le graphique circulaire
import plotly.express as px
fig = px.pie(
    names=description_counts.index,  # Les catégories uniques de "Description"
    values=description_counts.values,  # Les occurrences de chaque catégorie
    labels={"Description": "Type de description", "value": "Nombre d'occurrences"}
)


# Création de la page de tableau global
global_table_layout = html.Div([
    html.H1("Tableau récapitulatif des données météorologiques", style={"textAlign": "center"}),
    html.Div(f"Date du jour : {today_date}", style={"textAlign": "center", "marginBottom": "20px", "fontSize": "18px", "color": "#222"}),

    # Lien pour revenir à la page d'accueil
    html.Div([dcc.Link("Retour à la page d'accueil", href='/')]),
    html.Br(),

    # Tableau des données avec Ag-Grid
    AgGrid(
        id="global-table",
        rowData=df.to_dict("records"),
        columnDefs=[
            {"headerName": "Ville", "field": "Ville", "sortable": True, "filter": True},
            {"headerName": "Temperature", "field": "Temperature", "sortable": True, "filter": True}
        ] + [
            {"headerName": col, "field": col, "sortable": True, "filter": True}
            for col in df.columns if col not in ["Ville", "Temperature", "ID_OpenWeather"]
        ],
        defaultColDef={
            "resizable": True,
            "autoSize": True,  # Ajuste automatiquement la largeur des colonnes au contenu
            "filter": "agTextColumnFilter",
        },
        style={"width": "100%", "overflowX": "auto"}
    )

])

# Layout de la page Dashboard
Dashboard_layout = html.Div([
    # Encadré pour le titre avec date et heure
    html.Div([
        html.H1("Dashboard - Analyse globale de données météorologiques en France", style={"marginBottom": "10px"}),
        html.P(f"Date et heure du jour : {today_date}", style={"fontSize": "18px", "color": "#222"})
    ], style={
        "padding": "20px",
        "border": "1px solid #4a4e69",
        "borderRadius": "10px",
        "backgroundColor": "#e9ecef",  # Gris clair
        "marginBottom": "30px",
        "textAlign": "center"
    }),
    
    # Lien pour revenir à la page d'accueil
    html.Div([dcc.Link("Retour à la page d'accueil", href='/')]),

    # Ajouter un espace entre le lien et la suite
    html.Div(style={"marginBottom": "20px"}),  # Cela ajoute un espace de 20px

    # Section des indicateurs clés
    html.Div([
        html.Div([
            html.H3("Nombre de villes françaises analysées"),
            html.P(id="total-cities", style={"fontSize": "24px", "fontWeight": "bold"})
        ], style={
            "flex": "1", 
            "padding": "5px", 
            "textAlign": "center", 
            "border": "1px solid #4a4e69", 
            "borderRadius": "10px", 
            "backgroundColor": "#e3f2fd", 
            "marginBottom": "5px"       
        }),

        html.Div([
            html.H3("Température moyenne du jour"),
            html.P(id="average-temperature", style={"fontSize": "24px", "fontWeight": "bold"})
        ], style={
            "flex": "1", 
            "padding": "5px", 
            "textAlign": "center", 
            "border": "1px solid #4a4e69", 
            "borderRadius": "10px", 
            "backgroundColor": "#e3f2fd", 
            "marginBottom": "5px"        
        }),

        html.Div([
            html.H3("Vitesse moyenne du vent"),
            html.P(id="average-wind", style={"fontSize": "24px", "fontWeight": "bold"})
        ], style={
            "flex": "1", 
            "padding": "5px", 
            "textAlign": "center", 
            "border": "1px solid #4a4e69", 
            "borderRadius": "10px", 
            "backgroundColor": "#e3f2fd", 
            "marginBottom": "5px"
        })
    ], style={"display": "flex", "gap": "20px", "marginBottom": "20px"}),
    # Section graphique
    html.Div([
        html.H2("Visualisations des données météorologiques", style={"color": "#4a4e69", "marginBottom": "15px"}), 
        
        # Rangée unique pour les trois graphiques
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Distribution de la température selon le nombre de villes françaises", 
                            style={"textAlign": "center", "marginBottom": "10px", "height": "50px"})  # Hauteur fixe pour le titre
                ], style={"marginBottom": "10px"}),  # Conteneur pour le titre
                dcc.Graph(id="temperature-distribution", style={"width": "100%", "height": "400px"})
            ], style={
                "width": "32%", "display": "inline-block", "padding": "10px", 
                "border": "1px solid #4a4e69", "borderRadius": "10px"
            }),

            html.Div([
                html.Div([
                    html.H3("Conditions météorologiques en France (en %)", 
                            style={"textAlign": "center", "marginBottom": "10px", "height": "50px"})  # Hauteur fixe pour le titre
                ], style={"marginBottom": "10px"}),  # Conteneur pour le titre
                dcc.Graph(id="description-pie-chart", figure=fig, style={"width": "100%", "height": "400px"})
            ], style={
                "width": "32%", "display": "inline-block", "padding": "10px", 
                "border": "1px solid #4a4e69", "borderRadius": "10px"
            }),

            html.Div([
                html.Div([
                    html.H3("Carte des températures en France", 
                            style={"textAlign": "center", "marginBottom": "10px", "height": "50px"})  # Hauteur fixe pour le titre
                ], style={"marginBottom": "10px"}),  # Conteneur pour le titre
                dcc.Graph(id="temperature-map", style={"width": "100%", "height": "400px"})
            ], style={
                "width": "32%", "display": "inline-block", "padding": "10px", 
                "border": "1px solid #4a4e69", "borderRadius": "10px"
            })
        ], style={"display": "flex", "justifyContent": "space-between", "gap": "1%"})
    ], style={
        "padding": "20px",
        "border": "1px solid #4a4e69",
        "borderRadius": "10px",
        "backgroundColor": "#e9ecef",
        "marginBottom": "30px",
        "textAlign": "center"
    })

])


# page pour la visualisation par ville
@app.callback(
    [Output("city-dropdown", "options"),
     Output("temperature-graph", "children"),
     Output("temperature-table", "children")],
    [Input("data-selection", "value"),
     Input("city-dropdown", "value")]
)
def update_Nuage_Temp(selection, selected_cities):
    # Charger les données depuis MongoDB
    df = get_data_from_mongodb()

    # Vérifier les colonnes de df
    print(df.head())
    
    # Créer les options pour la liste déroulante
    options = [{"label": city, "value": city} for city in df["Ville"].unique()]

    if selection == "selected" and selected_cities:
        df_filtered = df[df["Ville"].isin(selected_cities)]
        if df_filtered.empty:
            return options, html.Div("Aucune donnée disponible pour les villes sélectionnées."), html.Div("Aucune donnée disponible.")
        
        # Créer le graphique pour les villes sélectionnées
        fig = px.scatter(
            df_filtered,
            x="Ville",
            y="Temperature",
            color="Ville",
            title="Températures par ville",
            labels={"Ville": "Ville","Temperature": "Température (°C)","Latitude": "Latitude", "Vent": "Vitesse du vent"},
            opacity=0.8,  # Augmenter l'opacité pour la visibilité
            hover_data={
                "Temperature": True,
                "Latitude": True,
                "Longitude": True,
                "Vent": True,
                "Ville": True  # Désactive l'affichage redondant
            }
        )
        fig.update_traces(marker=dict(size=10))  # Uniformiser la taille des points

        # Créer la table pour les villes sélectionnées
        table = html.Table(
            [html.Tr([html.Th("Ville"), html.Th("Température (°C)")])] +
            [html.Tr([html.Td(row["Ville"]), html.Td(f"{row['Temperature']} °C")]) for _, row in df_filtered.iterrows()]
        )
        return options, dcc.Graph(figure=fig), table

    elif selection == "all":
        if df.empty:
            return options, html.Div("Aucune donnée disponible."), html.Div("Aucune donnée disponible.")

        # Créer le graphique pour l'ensemble des données
        fig = px.scatter(
            df,
            y="Temperature",
            color="Ville",
            title="Températures par ville",
            labels={"Ville": "Ville","Temperature": "Température (°C)","Latitude": "Latitude", "Vent": "Vitesse du vent"},
            
        )
        fig.update_traces(marker=dict(size=10))  # Uniformiser la taille des points

        # Créer la table pour l'ensemble des données
        table = html.Table(
            [html.Tr([html.Th("Ville"), html.Th("Température (°C)")])] +
            [html.Tr([html.Td(row["Ville"]), html.Td(f"{row['Temperature']} °C")]) for _, row in df.iterrows()]
        )
        return options, dcc.Graph(figure=fig), table

    return options, html.Div("Veuillez sélectionner une option."), html.Div("Aucune donnée disponible.")

# Page des Comparaisons

@app.callback(
    [Output("temperature-wind-correlation", "figure"),
     Output("temperature-latitude-correlation", "figure")],
    Input("correlation-load", "value")
)
def display_correlation_graph(_):
    # Charger les données depuis MongoDB
    df = get_data_from_mongodb()

    # Afficher les informations pour déboguer
    print("Colonnes du DataFrame :", df.columns)
    print("Premières lignes du DataFrame :", df.head())
    
    # Vérifiez si le DataFrame est vide
    if df.empty:
        return (dcc.Graph(figure={"data": [], "layout": {"title": "Aucune donnée disponible"}}),
                dcc.Graph(figure={"data": [], "layout": {"title": "Aucune donnée disponible"}}))

    # Conversion des colonnes nécessaires en numérique si elles ne le sont pas déjà
    for col in ["Température (°C)", "Vent (km/h)", "Latitude"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Suppression des lignes avec des valeurs NaN après conversion
    df = df.dropna(subset=["Température (°C)", "Vent (km/h)", "Latitude"])

    # Vérification après nettoyage des données
    print("DataFrame après nettoyage :", df.head())

    # Vérifiez s'il reste des données
    if df.empty:
        return (dcc.Graph(figure={"data": [], "layout": {"title": "Aucune donnée valide après nettoyage"}}),
                dcc.Graph(figure={"data": [], "layout": {"title": "Aucune donnée valide après nettoyage"}}))

    # Graphique de la Comparaison entre la température et la vitesse du vent
    fig1 = px.scatter(
        df,
        x="Température (°C)",
        y="Vent (km/h)",
        color="Ville",
        title="Comparaison entre la température et la vitesse du vent",
        labels={"Température (°C)": "Température", "Vent (km/h)": "Vitesse du vent"}
    )
    fig1.update_traces(marker=dict(size=10))  # Taille uniforme pour tous les points

    # Graphique de la Comparaison entre la température et la latitude
    fig2 = px.scatter(
        df,
        x="Température (°C)",
        y="Latitude",
        color="Ville",
        title="Comparaison entre la température et la latitude",
        labels={"Température (°C)": "Température", "Latitude": "Latitude"}
    )
    fig2.update_traces(marker=dict(size=10, opacity=0.6))  # Taille et opacité des points

    return fig1, fig2


@app.callback(
    Output("global-report", "children"),
    Input("report-load", "value")
)
def display_global_report(_):
    df = get_data_from_mongodb()
    summary = df.describe().transpose()
    return dash_table.DataTable(
        columns=[{"name": col, "id": col} for col in summary.columns],
        data=summary.reset_index().to_dict("records"),
        style_table={"overflowX": "auto"},

    )

# Page pour le Dashboard
@app.callback(
    [Output("total-cities", "children"),
     Output("average-temperature", "children"),
     Output("average-wind", "children"),
     Output("temperature-distribution", "figure"),
     Output("temperature-map", "figure")],
     Input("url", "pathname")  # Déclenche uniquement sur changement de page
)
def update_Dashboard(pathname):
    # Charger les données depuis MongoDB
    df = get_data_from_mongodb()

    # Calculs des indicateurs
    total_cities = len(df["Ville"].unique())
    avg_temperature = round(df["Temperature"].mean(), 2)
    avg_wind = round(df["Vent"].mean(), 2)

    # Création du graphique de distribution des températures
    fig_hist = px.histogram(
        df,
        x="Temperature",
        nbins=20,
        labels={"Temperature": "Température (°C)"},
        color_discrete_sequence=["#70A9D1"]
    )

    # Création de la carte des températures
    fig_map = px.scatter_geo(
        df,
        lat="Latitude",  # Latitude des villes
        lon="Longitude",  # Longitude des villes
        color="Temperature",  # Couleur en fonction de la température
        hover_name="Ville",  # Affiche le nom de la ville
        hover_data={"Temperature": True, "Description": True},  # Affiche température et description
        projection="mercator"  # Projection Mercator pour la carte
    )
    # Ajustement des styles pour la carte
    fig_map.update_traces(marker=dict(
        colorscale=[
            [0, "blue"],  # Bleu pour les températures les plus basses
            [0.25, "white"],  # Blanc pour les températures moyennes
            [0.5, "yellow"],  # Jaune pour les températures moyennes-élevées
            [0.75, "orange"],  # Orange pour les températures élevées
            [1, "red"]  # Rouge pour les températures très élevées
        ],
        colorbar=dict(title="Température (°C)")  # Ajout d'une barre de couleur
    ))

    fig_map.update_geos(
        resolution=50,  # Détail des côtes
        showcoastlines=True,
        coastlinecolor="LightGray",
        showland=True,
        landcolor="white",
        showocean=True,
        oceancolor="LightBlue",
        center={"lat": 46.603354, "lon": 1.888334},  # Latitude et longitude de la France
        projection_scale=15,  # Zoom (ajustez selon vos besoins)
        projection_type="mercator"
    )

    # Retourner les données et les figures mises à jour
    return total_cities, f"{avg_temperature} °C", f"{avg_wind} km/h", fig_hist, fig_map

pdf_layout = html.Div([])


# Gestion de la navigation
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == '/Top10':
        return Top10_layout
    elif pathname == '/Nuage_Temp':
        return Nuage_Temp_layout
    elif pathname == '/Comparaison':
        return Comparaison_layout
    elif pathname == '/Tableau':
        return global_table_layout
    elif pathname == '/Dashboard':  # Ajoutez la route pour le Dashboard
        return Dashboard_layout
    elif pathname == '/static/Documentation.pdf' :
        return pdf_layout
    else:
        return app.Accueil_layout

# Layout principal
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])

# Lancement de l'application
#if __name__ == "__main__":
#    app.run_server(debug=True)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
