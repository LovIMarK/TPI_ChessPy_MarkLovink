# ChessPy - Jeu d'échecs en Python

## Description

**ChessPy** est une application de jeu d'échecs développée en **Python** avec **Pygame**. Ce projet a été conçu dans le cadre d'un Travail de fin d'Année **(TPI)** validé avec une note de **6/6**, visant à proposer une simulation interactive et fonctionnelle du jeu d'échecs, incluant un mode multijoueur local et la gestion des règles du jeu.

## Fonctionnalités

- **Interface graphique interactive** avec *Pygame*
- **Mode 2 joueurs** sur le même ordinateur
- **Sauvegarde et chargement** de la dernière partie
- **Gestion complète des règles officielles des échecs** :
  1. Déplacements valides des pièces
  2. Échec et mat
  3. Promotion des pions
  4. Roque
- **Horloge** pour mesurer le temps des joueurs
- **Unités de test** intégrées pour assurer la robustesse du jeu

## Technologies utilisées

- **Langage** : Python (3.11)
- **Framework** : Pygame
- **Tests** : unittest
- **Fichiers JSON** pour la sauvegarde des positions
- **Gestion de versions** : Git / GitHub

## Installation

1. **Cloner le dépôt** :
   ```sh
   git clone https://github.com/votre_nom/ChessPy.git
   cd ChessPy
   ```
2. **Installer les dépendances** :
   ```sh
   pip install pygame
   ```
3. **Lancer l'application** :
   ```sh
   python Menu.py
   ```

## Structure du projet

```
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
```

## Comment jouer ?

1. **Lancer le jeu** :
   ```sh
   python Menu.py
   ```
2. **Choisir un mode** :
   - "2 Players" pour jouer à deux sur le même ordinateur
   - "Last Game" pour charger la dernière partie enregistrée
3. **Déplacer les pièces** avec la souris selon les règles du jeu d'échecs

## Améliorations futures

- Ajouter une **intelligence artificielle** pour jouer contre l'ordinateur
- Ajouter un **mode en ligne**
- Améliorer l'**interface graphique**

## Auteur

- **Nom** : Mark Lovink

## Licence

Ce projet est sous licence **MIT**. Vous êtes libre de le modifier et de l'améliorer ! 🎉

