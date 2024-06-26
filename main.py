"""
Générateur de Profil Aérodynamique NACA
Ce programme génère et affiche le profil d'une aile symétrique en utilisant les équations du National Advisory Committee
for Aeronautics (NACA).

Fonctions:
    - validate_input: Valide les entrées utilisateur.
    - naca00xx_profile: Génère et affiche le profil d'une aile NACA 4 chiffres.

Auteur: Lou-Anne Villette
Date: 03/06/2024
"""

# Import des modules
import numpy as np
import matplotlib.pyplot as plt

# Liste des types de distribution valides
VALID_DISTRIBUTIONS = ['linéaire', 'non-uniforme']


def validate_input(demand, min_value=None, input_type=float, max_value=None):
    """
    Valide les entrées utilisateur en vérifiant si elles sont de type numérique,
    et optionnellement, si elles se situent dans une plage spécifiée.

    Arguments:
        demand (str): Message demandant à l'utilisateur de saisir une valeur.
        min_value (float ou int, optionnel): Valeur minimale autorisée (par défaut None).
        input_type (type, optionnel): Type de données attendu (par défaut float).
        max_value (float ou int, optionnel): Valeur maximale autorisée (par défaut None).

    Retour:
        user_type: Entrée utilisateur validée.
    """
    while True:
        try:
            user_input = input_type(input(demand))
            # Vérification de la valeur minimale si spécifiée
            if min_value is not None and user_input < min_value:
                raise ValueError(f"La valeur doit être supérieure ou égale à {min_value}.")
            # Vérification de la valeur maximale si spécifiée
            if max_value is not None and user_input > max_value:
                raise ValueError(f"La valeur doit être inférieure ou égale à {max_value}.")
            return user_input
        except ValueError as numerical_ve:
            print(numerical_ve)


def naca00xx_profile(profile_nb, chord_lgth, points_nb, distrib_type):
    """
    Génère et affiche le profil d'une aile symétrique NACA à 4 chiffres.

    Arguments:
        profile_nb (int): Numéro du profil NACA.
        chord_lgth (float): Longueur de la corde du profil (en mètres).
        points_nb (int): Nombre de points le long de la corde pour le tracé.
        distrib_type (str): Type de distribution de points le long de la corde ('linéaire' ou 'non-uniforme').

    Retours:
        (tuple)
        max_thickness (float): Épaisseur maximale.
        max_thickness_position (float): Position de l'épaisseur maximale.
    """
    # Calcul du paramètre t basé sur le numéro de profil
    t = profile_nb / 100

    # Génération des coordonnées adimensionnelles x_c selon le type de distribution
    if distrib_type == "linéaire":
        x_c = np.linspace(0, 1, points_nb)
    else:
        theta = np.linspace(0, np.pi, points_nb)
        x_c = 0.5 * (1 - np.cos(theta))

    # Calcul de l'épaisseur du profil selon l'équation NACA
    y_t = 5 * t * (0.2969 * np.sqrt(x_c) - 0.1260 * x_c - 0.3516 * x_c ** 2 + 0.2843 * x_c ** 3 - 0.1036 * x_c ** 4)

    # Calcul des coordonnées pour l'extrados (au-dessus de la corde)
    x_up = x_c * chord_lgth
    y_up = y_t * chord_lgth

    # Calcul des coordonnées pour l'intrados (en-dessous de la corde)
    x_down = x_c * chord_lgth
    y_down = -y_t * chord_lgth

    # Calcul de l'épaisseur maximale et de sa position le long de la corde
    max_thickness = np.max(y_up) * 2
    max_thickness_position = x_up[np.argmax(y_up)]

    # Affichage des résultats
    print(f"\nEpaisseur maximale: {max_thickness:.4f} m")
    print(f"Position de l'épaisseur maximale: {max_thickness_position:.4f} m")

    # Affichage du graphique avec le profil de l'aile
    fig, ax = plt.subplots()
    # Double-flèche pour le maximum d'épaisseur
    ax.annotate('', xy=[max_thickness_position, max_thickness / 2], xytext=[max_thickness_position, -max_thickness / 2],
                arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(max_thickness_position + 0.02 * chord_lgth, 0, f'Epaisseur maximale: {max_thickness:.2f} m', color='black',
            ha='left', va='center', fontsize=10)
    # Courbes du profil
    plt.plot(x_up, y_up, label='extrados')
    plt.plot(x_down, y_down, label='intrados')
    plt.legend()
    plt.grid(True)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.axis('equal')
    plt.title(f'Profil aérodynamique NACA 00{profile_nb}')
    plt.show()

    return max_thickness, max_thickness_position


# Point d'entrée du programme
if __name__ == "__main__":
    # Validation des entrées utilisateur pour chaque paramètre requis
    profile_number = validate_input("Entrez le numéro du profil NACA 4 chiffres symétrique 00xx (ex: 0012 ou 12): ", 0,
                                    int, 99)
    chord_length = validate_input("Entrez la longueur de la corde du profil (en mètres): ", 0)
    points_number = validate_input("Entrez le nombre de points le long de la corde pour le tracé: ", 2, int)
    while True:
        try:
            distribution_type = input(
                "Entrez le type de distribution de points le long de la corde (linéaire/non-uniforme): ").lower()
            if distribution_type not in VALID_DISTRIBUTIONS:  # Vérification si le type de distribution est valide
                raise ValueError("Type de distribution invalide. Utilisez 'linéaire' ou 'non-uniforme'.")
            break
        except ValueError as literal_ve:
            print(literal_ve)

    # Appel de la fonction pour générer et afficher le profil
    naca00xx_profile(profile_number, chord_length, points_number, distribution_type)
