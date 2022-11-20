# DEVELOPPER UN PROGRAMME LOGICIEL EN PYTHON / OC_p4
---------------------------------------------------------------


## TABLE DES MATIERES
---------------------

* Introduction
* Configuration requise
* Installation
* Configuration
* Utilisation


## INTRODUCTION
----------------

* Le programme est un logiciel permettant de gérer des tournois selon le système de tournoi "suisse" et de produire des rapports.


## CONFIGURATION REQUISE
--------------------------

* Ce programme n'a pas besoin de module spécifique


## INSTALLATION
------------------

* Télécharger python 3
* Installer python 3 
* Ouvrir l'invite de commande
* Créer un dossier au nom de l'application avec mkdir
* Créer votre environnement virtuel avec python3.xx -m venv .env
* Sourcer cette environnement virtuel avec avec source .env/Scripts/activate
* Installer la configuration à l'aide du fichier requirements.txt avec pip3 install -r requirements.txt
* Ajouter les fichiers dans le dossier créé
* Le programme peut être lancé


## CONFIGURATION
--------------------

* Ce programme n'a pas d'option modifiable et ni de configuration spécial.


## UTILISATION
-------------------

Navigation du menu gestionnaire de tournoi:
* ```1``` Créer un tournoi permet de créer un nouveau tournoi et d'ajouter les joueurs
* ```2``` Menu tournoi permet d'aller dans le menu tournoi
* ```3``` Charger un tournoi permet de récupérer les tournois sauvegardés
* ```4``` Editer un rapport permet d'éditer un rapport sur les tournois et les joueurs de la base de données (matchs, round, etc.)
* ```5``` Mettre à jour le classement permet de mettre à jour le classement des joueurs de la base de données
* ```6``` Exit permet de quitter le programme

Navigation du menu tournoi:
* ```1``` Lancer le tour permet de démarrer les matchs
* ```2``` Finir le tour permet d'arreter le tour lorsque les matchs ont tous finis
* ```3``` Entrer les résultats des matchs permet de rentrer les scores
* ```4``` Affiche le classement permet d'afficher le classement des joueurs en fonction de leur classement et de leur score
* ```5``` Permet de sauvegarder le tournoi à tout moment
* ```0``` Retour permet de revenir au menu précédent

Exemple d'utilisation:
* Dans le menu gestionnaire de tournoi, faites ```1``` + ```entrée``` pour créer un tournoi
* Remplir les champs
* Lancer le 1er tour, faites ```1``` + ```Entrée```
* Finir le tour, faites ```2``` + ```Entrée```
* Remplir les résultats, faites ```3``` + ```Entrée```
* Répéter les 3 étapes précédentes, jusqu'à la fin du tournoi
* Pour sauvegarder le tournoi, appuyer sur ```5``` + ```entrée``` dans le menu tournoi
* Pour revenir en arrière appuyez sur ```0``` + ```entrée```

