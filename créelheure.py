import time  # Importation de la bibliothèque pour gérer le temps

# Heure initiale fixée à 20:00:00
heures = 20
minutes = 0
secondes = 0

# Boucle infinie pour afficher et mettre à jour l'heure chaque seconde
while True:
    # Affichage de l'heure sous la forme hh:mm:ss sur la même ligne
    print(f"\r{heures:02}:{minutes:02}:{secondes:02}", end="")

    # Attente d'une seconde avant de passer à la suivante
    time.sleep(1)

    # Ajouter 1 seconde à l'heure actuelle
    secondes += 1

    # Vérification pour passer à la minute suivante si secondes = 60
    if secondes == 60:
        secondes = 0  # Réinitialiser les secondes
        minutes += 1  # Ajouter 1 minute

    # Vérification pour passer à l'heure suivante si minutes = 60
    if minutes == 60:
        minutes = 0  # Réinitialiser les minutes
        heures += 1  # Ajouter 1 heure

    # Réinitialisation de l'heure à 00:00:00 si heures = 24
    if heures == 24:
        heures = 0
