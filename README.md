# Générateur de Profil Aérodynamique NACA

Ce projet est un générateur de profil d'aile symétrique en utilisant les équations du National Advisory Committee for Aeronautics (NACA). Ces profils sont couramment utilisés en aéronautique pour concevoir des ailes et d'autres surfaces portantes.

## Objectif

Le but de ce programme est de permettre aux utilisateurs de générer et d'afficher facilement le profil d'une aile aérodynamique en utilisant les spécifications NACA 4 chiffres. De plus, le programme calcule l'épaisseur maximale du profil et sa position le long de la corde.

## Structure du Code

- Le code est structuré en deux fonctions principales :

    1. **`validate_input`** :
        - **Description** : Valide les entrées utilisateur en vérifiant leur type et leur plage de valeurs.
        - **Arguments** :
            - `demand` (str) : Message demandant à l'utilisateur de saisir une valeur.
            - `min_value` (float ou int, optionnel) : Valeur minimale autorisée (par défaut None).
            - `input_type` (type, optionnel) : Type de données attendu (par défaut float).
            - `max_value` (float ou int, optionnel) : Valeur maximale autorisée (par défaut None).
        - **Retour** : Entrée utilisateur validée.

    2. **`naca00xx_profile`** :
        - **Description** : Génère et affiche le profil d'une aile symétrique NACA à 4 chiffres.
        - **Arguments** :
            - `profile_nb` (int) : Numéro du profil NACA.
            - `chord_lgth` (float) : Longueur de la corde du profil (en mètres).
            - `points_nb` (int) : Nombre de points le long de la corde pour le tracé.
            - `distrib_type` (str) : Type de distribution de points le long de la corde ('linéaire' ou 'non-uniforme').
        - **Retours** : Tuple contenant l'épaisseur maximale et la position de l'épaisseur maximale.

- Le point d'entrée du programme se trouve à la fin du script. Il guide l'utilisateur à travers les étapes d'entrée des données et appelle la fonction principale pour générer et afficher le profil.

## Utilisation

1. Clonez le dépôt ou téléchargez les fichiers sur votre machine locale.

2. Assurez-vous d'avoir installé les bibliothèques nécessaires. Vous pouvez les installer via `pip` :
    ```bash
    pip install numpy matplotlib
    ```

3. Exécutez le script `main.py` avec Python 3

4. Le programme vous demandera de saisir les informations suivantes :
    - **Numéro du profil NACA (00xx)** : Par exemple, entrez `0012` ou `12` pour le profil NACA 0012.
    - **Longueur de la corde du profil (en mètres)** : Entrez la longueur de la corde.
    - **Nombre de points le long de la corde pour le tracé** : Entrez le nombre de points pour définir la précision du tracé.
    - **Type de distribution de points le long de la corde** : Choisissez entre `linéaire` ou `non-uniforme`.

5. Le programme génère et affiche le profil de l'aile avec l'extrados et l'intrados basé sur vos entrées, ainsi que l'épaisseur maximale du profil et sa position le long de la corde.

---

*Auteur: [Lou-Anne Villette](https://github.com/Louettelliv), Date : 03/06/2024*
