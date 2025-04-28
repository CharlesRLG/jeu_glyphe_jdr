import tkinter as tk
from tkinter import simpledialog, messagebox
import random

def game():
    # Initialisation des variables
    MIN_VALUE, MAX_VALUE = 0, 100
    value = random.randint(MIN_VALUE, MAX_VALUE)
    bonneFortune = random.randint(1, 150) + 500
    mauvaiseFortune = random.randint(25, 200)

    MAX_ATTEMPTS = 12
    punition = ["-10 à la force !", "-10 à l'agilité !", "-10 à l'endurance !",
                "-10 à la force mentale !", "-10 au CC !", "-10 au CT", "-10 à la dextérité !",
                "une boule de feu 2d100 dégâts !", "-10 à la chance !", "-1d100 Po"]
    attempts = 0

    # Liste des panoplies et items
    list_panoplie = [
        "du Barde des étoiles", 
        "du Sorcier des Bulles", "du Chevalier des Nuages", "du Voleur de Rêves", "du Druide des Champignons",
        "du Guerrier des Étoiles Filantes", "de l'Archer des Arc-en-Ciel", "du Moine des Éclairs", 
        "du Nécromancien des Papillons", "du Chevalier du temps", "du Mage des Éclats de Cristal", 
        "du Voleur de Lune", "du Druide des Fleurs", "du Guerrier des Flammes Bleues", "de l'Archer de lumière",
        "du Moine de Magma", "du Nécromancien des Ombres Dansantes", "du Paladin des Tempêtes", 
        "de l'Assassin des Brumes", "de l'éclat céleste", "des ailes de lumière", "de l'armure Séraphique", 
        "de la fureur infernale", "de l'armure du Chaos", "du pacte sombre", "de la bénédiction Sacrée",
        "de la lumière du sanctuaire", "du secret hermétique", "des arcane de la transmutation", 
        "de la panoplie du négociant", "de l'ensemble du courtier"
    ]
    list_items = ["le casque", "la cuirasse", "les bottes", "le gant", "la cape", "l'arme"]

    # Sélection des récompenses
    selection_panoplie = random.choice(list_panoplie)
    item = random.choice(list_items)

    # Phrase et localisation
    phrase_enigme = simpledialog.askstring("Mot mystère", "Tapez votre mot à deviner (8 caractères max) :")
    localisation = simpledialog.askstring("Localisation", "Écrivez la localisation de l'objet :")
    
    # Fenêtre de jeu
    affichage = "-" * len(phrase_enigme)
    lettre_trouve = ""
    
    # Boucle de jeu
    for attempts in range(MAX_ATTEMPTS):
        answer = simpledialog.askinteger("Tentative", f"Un Glyphe apparaît avec des chiffres de 1 à 100.\nEssais restants : {MAX_ATTEMPTS - attempts}")
        if not answer:
            break

        if answer == value:
            tentative_restante = MAX_ATTEMPTS - attempts
            messagebox.showinfo("Victoire", f"Un coffre apparaît et s'ouvre !\nVous trouvez {bonneFortune} Pièces d'or !!!\n"
                                            f"Vous pouvez deviner {tentative_restante} caractères.")
            

            # Deviner les lettres du mot
            while tentative_restante > 0:
                affichage = "".join([l if l in lettre_trouve else "-" for l in phrase_enigme])
                if affichage == phrase_enigme:  # Vérifie si le mot entier est deviné
                    break
                lettre = simpledialog.askstring("Devinez une lettre", f"Mot : {affichage}\nIl vous reste {tentative_restante} chances.")
                if lettre and lettre in phrase_enigme:
                    lettre_trouve += lettre
                    messagebox.showinfo("Bravo", f"La lettre '{lettre}' est correcte !")
                else:
                    tentative_restante -= 1
                    if lettre:  # Vérifie que `lettre` n'est pas vide
                        messagebox.showwarning("Erreur", f"La lettre '{lettre}' n'est pas dans le mot.")


            
            # Résultat du mot mystère
            if affichage == phrase_enigme:
                messagebox.showinfo("Félicitations", f"Vous avez découvert le mot : {phrase_enigme}\n"
                                                     f"Vous recevez {item} de la panoplie {selection_panoplie}.\n"
                                                     f"Localisation : {localisation} \n"
                                                     f"Vous recevez {tentative_restante} gemmes bleu !")
            else:
                messagebox.showinfo("Échec", f"Vous n'avez pas deviné le mot : {phrase_enigme}")
            break
        else:
            attempts += 1
            if answer > value:
                messagebox.showinfo("Indice", "Une lumière bleue apparaît et descend.")
            else:
                messagebox.showinfo("Indice", "Une lumière rouge apparaît et monte.")
            punishment = random.choice(punition)
            messagebox.showwarning("Punition", f"C'est raté ! Vous subissez : {punishment}")
    
    else:
        messagebox.showerror("Défaite", f"---> Non !!! Bande d'incapables !!!\n"
                                        f"---> La bonne réponse était {value}\n"
                                        f"Vous trouvez {mauvaiseFortune} Pièces de cuivre dans un coffre.")
        
# Interface Tkinter
root = tk.Tk()
root.withdraw()  # Masquer la fenêtre principale
game()

