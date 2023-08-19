![Python Version](https://img.shields.io/badge/Python-3.7-blue.svg)![Flake8](https://img.shields.io/badge/Flake8-Passing-brightgreen.svg)
# Gestionnaire de Tournoi d'Échecs

## Table des matières

- [Introduction](#introduction)
- [Configuration requise](#configuration-requise)
- [Installation](#installation)
- [Fonctionnalités](#fonctionnalités)
- [Structure du projet](#structure-du-projet)
- [Utilisation](#utilisation)
- [Rapport Flake8](#rapport-flake8)

## Introduction

Le Gestionnaire de Tournoi d'Échecs est un logiciel Python permettant de gérer des tournois d'échecs selon le système de tournoi "suisse". Il a été développé dans le cadre d'un projet visant à aider un club d'échecs local à organiser ses tournois de manière plus efficace et conviviale. Le programme offre des fonctionnalités pour créer, gérer et sauvegarder des tournois, ajouter des joueurs, lancer des matchs, saisir les résultats et afficher le classement des joueurs.

## Configuration requise

* Python 3 installé sur votre système : [Téléchargement Python 3](https://www.python.org/downloads/)
* Git installé sur votre système : [Téléchargement Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

## Installation

1. Téléchargez et installez Python 3 depuis le site officiel : https://www.python.org/downloads/
2. Ouvrez l'invite de commande (ou terminal).
3. Créez un dossier pour l'application avec la commande : `mkdir GestionnaireTournoiEchecs`.
4. Accédez au dossier nouvellement créé : `cd GestionnaireTournoiEchecs`.
5. Créez un environnement virtuel avec la commande (Windows) : `python -m venv .env` ou (Mac/Linux) : `python3 -m venv .env`.
6. Activez l'environnement virtuel (Windows) : `.env\Scripts\activate` ou (Mac/Linux) : `source .env/bin/activate`.
7. Installez les dépendances requises avec la commande : `pip install -r requirements.txt`.
8. Ajoutez les fichiers du Gestionnaire de Tournoi d'Échecs dans le dossier.

ou :

1. Téléchargez le projet sur votre répertoire local : 
```
git clone https://github.com/MarcOutt/OC_p4.git
```

2. Mettez en place un environnement virtuel :
   * Créez l'environnement virtuel: `python -m venv venv`
   * Activez l'environnement virtuel :
       * Windows : `venv\Scripts\activate.bat`
       * Unix/MacOS : `source venv/bin/activate`

3. Installez les dépendances du projet :

```
pip install -r requirements.txt
```



### Navigation du menu gestionnaire de tournoi:

1. **Créer un tournoi** : Permet de créer un nouveau tournoi et d'ajouter les joueurs.
2. **Menu tournoi** : Permet d'accéder au menu du tournoi pour gérer les tours, les matchs, etc.
3. **Charger un tournoi** : Permet de récupérer les tournois sauvegardés.
4. **Editer un rapport** : Permet d'éditer un rapport sur les tournois et les joueurs de la base de données (matchs, rounds, etc.).
5. **Mettre à jour le classement** : Permet de mettre à jour le classement des joueurs de la base de données.
6. **Exit** : Permet de quitter le programme.

### Navigation du menu tournoi:

1. **Lancer le tour** : Permet de démarrer les matchs du tournoi.
2. **Finir le tour** : Permet d'arrêter le tour lorsque tous les matchs ont été joués.
3. **Entrer les résultats des matchs** : Permet de saisir les scores des matchs.
4. **Affiche le classement** : Permet d'afficher le classement des joueurs en fonction de leur classement et de leur score.
5. **Sauvegarder le tournoi** : Permet de sauvegarder le tournoi à tout moment.
0. **Retour** : Permet de revenir au menu précédent.

## Fonctionnalités

- Créer, gérer et sauvegarder des tournois d'échecs.
- Ajouter et gérer les joueurs participant aux tournois.
- Lancer et gérer les matchs selon le système de tournoi "suisse".
- Saisir les résultats des matchs et mettre à jour le classement des joueurs.
- Générer des rapports sur les tournois et les joueurs.

## Structure du projet

Le projet est organisé de la manière suivante :

- `main.py` : Le point d'entrée du programme.
- `models.py` : Contient les classes modèles pour les tournois, les joueurs, les matchs, etc.
- `views.py` : Contient les vues pour afficher les menus et les rapports.
- `controllers.py` : Contient les contrôleurs pour gérer la logique du programme.
- `data/` : Dossier contenant les fichiers de sauvegarde des tournois (format JSON).
- `flake8-rapport/` : Dossier contenant le rapport Flake8.
  
## Utilisation

Pour lancer le programme, suivez les étapes suivantes :

1. Dans l'invite de commande, assurez-vous que l'environnement virtuel est activé.
2. Accédez au dossier contenant le gestionnaire de tournoi : `cd GestionnaireTournoiEchecs`.
3. Exécutez le programme en entrant la commande : `python main.py`.

### Exemple d'utilisation :

1. Dans le menu gestionnaire de tournoi, sélectionnez `1` + Entrée pour créer un tournoi.
2. Remplissez les champs du tournoi.
3. Lancez le 1er tour, sélectionnez `1` + Entrée.
4. Une fois les matchs terminés, sélectionnez `2` + Entrée pour finir le tour.
5. Saisissez les résultats des matchs, sélectionnez `3` + Entrée.
6. Répétez les étapes 3 à 5 jusqu'à la fin du tournoi.
7. Pour sauvegarder le tournoi, sélectionnez `5` + Entrée dans le menu tournoi.
8. Pour revenir en arrière, appuyez sur `0` + Entrée.
   
## Rapport Flake8

Pour générer un rapport Flake8, suivez ces étapes :

1. Ouvrez l'invite de commande (ou terminal).
2. Activez votre environnement virtuel (Windows) : `.env\Scripts\activate` ou (Mac/Linux) : `source .env/bin/activate`.
3. Entrez la commande suivante : `flake8 --exclude=.env/ --max-line-length=119 --format=html --htmldir=flake8-rapport`.
4. Accédez au dossier `flake8-rapport`.
5. Ouvrez le fichier `index.html` pour consulter le rapport.


