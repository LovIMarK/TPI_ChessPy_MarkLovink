ChessPy - Jeu d'échecs en Python

Description

ChessPy est une application de jeu d'échecs développée en Python avec Pygame. Ce projet a été conçu dans le cadre d'un Travail de Fin d'Année (TFA), visant à proposer une simulation interactive et fonctionnelle du jeu d'échecs, incluant un mode multijoueur local et la gestion des règles du jeu.

Fonctionnalités

✅ Interface graphique interactive avec Pygame
✅ Jeu en mode 2 joueurs
✅ Sauvegarde et chargement de la dernière partie
✅ Gestion des règles officielles des échecs (déplacements valides, échec et mat, promotion, roque...)
✅ Horloge pour mesurer le temps de chaque joueur
✅ Unités de test intégrées pour assurer la robustesse des fonctions clés

Technologies utilisées

Langage : Python (3.x)

Framework : Pygame

Tests : unittest

Fichiers JSON pour la sauvegarde des pièces

Gestion de versions : Git / GitHub

Installation

Cloner le dépôt

git clone https://github.com/votre_nom/ChessPy.git
cd ChessPy

Installer les dépendances

pip install pygame

Lancer l'application

python Menu.py

Structure du projet

ChessPy/
│── Pieces/            # Classes des pièces d'échecs (Roi, Reine, Cavalier...)
│── Var.py             # Variables globales
│── Board.py           # Gestion de l'échiquier
│── Game.py            # Logique du jeu
│── Menu.py            # Menu principal
│── Player.py          # Gestion des joueurs
│── Square.py          # Définition des cases de l'échiquier
│── UnitTest.py        # Tests unitaires
│── pieces.json        # Sauvegarde des positions
└── README.md          # Présentation du projet

Comment jouer ?

Lancer le jeu : python Menu.py

Choisir un mode :

"2 Players" pour jouer à deux sur le même ordinateur

"Last Game" pour charger la dernière partie enregistrée

Jouer en déplaçant les pièces avec la souris selon les règles du jeu d'échecs

Améliorations futures

Ajouter une intelligence artificielle pour jouer contre l'ordinateur

Ajouter un mode en ligne

Améliorer l'interface graphique

Auteur

📌 Mark Lovink🔗 LinkedIn📩 Contact : mark@lovink.ch

Licence

Ce projet est sous licence MIT. Vous êtes libre de le modifier et de l'améliorer ! 🎉
