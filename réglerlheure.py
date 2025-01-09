import time  # Importation de la bibliothèque pour gérer le temps

# Heure initiale fixée à 20:00:00
heures = 20
minutes = 0
secondes = 0

# Fonction pour afficher l'heure sous le format hh:mm:ss
def afficher_heure():
    print(f"L'heure actuelle est : {heures:02}:{minutes:02}:{secondes:02}")

# Fonction pour régler l'heure
def regler_heure():
    global heures, minutes, secondes  # Utilisation des variables globales
    print("\nVeuillez régler l'heure :")
    heures = int(input("Entrez l'heure (0-23): "))
    minutes = int(input("Entrez les minutes (0-59): "))
    secondes = int(input("Entrez les secondes (0-59): "))

# Afficher une seule fois l'heure initiale
afficher_heure()

# Boucle infinie pour afficher l'heure et permettre de la régler
while True:
    # Demander si Mamie veut régler l'heure
    choix = input("\nAppuyez sur 'R' pour régler l'heure ou 'Q' pour quitter: ").lower()

    if choix == 'R':
        regler_heure()  # Permet de modifier l'heure
        print("\nL'heure a été réglée.")
        afficher_heure()  # Affiche l'heure après réglage
    elif choix == 'Q':
        print("Au revoir Mamie Jeannine!")
        break  # Quitte le programme
    else:
        print("Choix invalide, veuillez réessayer.")

    # Attendre une seconde avant de mettre à jour l'heure
    time.sleep(1)

    # Ajouter 1 seconde
    secondes += 1

    # Vérifier si il faut passer à la minute suivante
    if secondes == 60:
        secondes = 0
        minutes += 1

    # Vérifier si il faut passer à l'heure suivante
    if minutes == 60:
        minutes = 0
        heures += 1

    # Réinitialiser l'heure à 00:00:00 si il y a 24 heures
    if heures == 24:
        heures = 0
