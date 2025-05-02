import tkinter as tk
import random

class JeuMystere:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Le Glyphe de Rand-Hôm")

        # Initialisation
        self.MIN_VALUE, self.MAX_VALUE = 0, 100
        self.value = random.randint(self.MIN_VALUE, self.MAX_VALUE)
        self.bonneFortune = random.randint(1, 150) + 500
        self.mauvaiseFortune = random.randint(25, 200)
        self.damage = random.randint(2, 200)
        self.perteArgent = random.randint(1, 100)
        self.MAX_ATTEMPTS = 12
        self.punition = ["-10 à la force !", "-10 à l'agilité !", "-10 à l'endurance !",
                         "-10 à la force mentale !", "-10 au CC !", "-10 au CT", "-10 à la dextérité !",
                         f"une boule de feu {self.damage} dégâts !", "-10 à la chance !", f" vous perdez {self.perteArgent} Po"]
        self.list_panoplie = [
            "du Barde des étoiles", "du Sorcier des Bulles", "du Chevalier des Nuages", "du Voleur de Rêves",
            "du Druide des Champignons", "du Guerrier des Étoiles Filantes", "de l'Archer des Arc-en-Ciel",
            "du Moine des Éclairs", "du Nécromancien des Papillons", "du Chevalier du temps",
            "du Mage des Éclats de Cristal", "du Voleur de Lune", "du Druide des Fleurs",
            "du Guerrier des Flammes Bleues", "de l'Archer de lumière", "du Moine de Magma",
            "du Nécromancien des Ombres Dansantes", "du Paladin des Tempêtes", "de l'Assassin des Brumes",
            "de l'éclat céleste", "des ailes de lumière", "de l'armure Séraphique", "de la fureur infernale",
            "de l'armure du Chaos", "du pacte sombre", "de la bénédiction Sacrée", "de la lumière du sanctuaire",
            "du secret hermétique", "des arcane de la transmutation", "de la panoplie du négociant",
            "de l'ensemble du courtier"
        ]
        self.list_items = ["le casque", "la cuirasse", "les bottes", "le gant", "la cape", "l'arme"]
        self.selection_panoplie = random.choice(self.list_panoplie)
        self.item = random.choice(self.list_items)

        self.attempts = 0
        self.etape = "mot"  # "mot", "localisation", "jeu", "lettres"
        self.lettres_restantes = 0
        self.lettres_trouvees = ""
        
        # Interface
        self.label = tk.Label(root, text="Tapez le mot à deviner (8 lettres max)", font=("Arial", 16))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 16))
        self.entry.pack()

        self.bouton = tk.Button(root, text="Valider", font=("Arial", 14), command=self.etape_suivante)
        self.bouton.pack(pady=10)

        self.resultat = tk.Label(root, text="", font=("Arial", 14), wraplength=780, justify="left")
        self.resultat.pack(pady=10)

    def etape_suivante(self):
        texte = self.entry.get()
        self.entry.delete(0, tk.END)

        if self.etape == "mot":
            if not texte or len(texte) > 8:
                self.resultat.config(text="Mot invalide. Veuillez entrer un mot de 8 caractères max.")
                return
            self.phrase_enigme = texte
            self.affichage = "-" * len(self.phrase_enigme)
            self.etape = "localisation"
            self.label.config(text="Écrivez la localisation de l'objet :")
            self.resultat.config(text="")
        elif self.etape == "localisation":
            if not texte:
                self.resultat.config(text="Veuillez entrer une localisation.")
                return
            self.localisation = texte
            self.etape = "jeu"
            self.label.config(text=f"Trouvez le nombre entre {self.MIN_VALUE} et {self.MAX_VALUE}")
            self.resultat.config(text=f"Vous avez {self.MAX_ATTEMPTS} essais.\nEntrez un nombre :")
        elif self.etape == "jeu":
            try:
                guess = int(texte)
            except ValueError:
                self.resultat.config(text="Veuillez entrer un nombre valide.")
                return

            if guess == self.value:
                self.lettres_restantes = self.MAX_ATTEMPTS - self.attempts
                self.etape = "lettres"
                self.label.config(text="Nombre trouvé ! Devinez les lettres du mot :")
                self.resultat.config(text=f"Vous avez trouvé {self.bonneFortune} pièces d'or !\n"
                                          f"Devinez le mot. Il vous reste {self.lettres_restantes} essais.")
                self.update_affichage()
            else:
                self.attempts += 1
                if self.attempts >= self.MAX_ATTEMPTS:
                    self.fin_de_jeu(False)
                    return
                indice = "bleue et descend." if guess > self.value else "rouge et monte."
                punition = random.choice(self.punition)
                self.resultat.config(text=f"Mauvais numéro ! La lumière est {indice}\nPunition : {punition}\n"
                                          f"Essais restants : {self.MAX_ATTEMPTS - self.attempts}")
        elif self.etape == "lettres":
            if not texte or len(texte) != 1:
                self.resultat.config(text="Veuillez entrer une seule lettre.")
                return
            lettre = texte.lower()
            if lettre in self.phrase_enigme and lettre not in self.lettres_trouvees:
                self.lettres_trouvees += lettre
                self.resultat.config(text=f"Bonne lettre ! Il vous reste {self.lettres_restantes} essais.")
            else:
                self.lettres_restantes -= 1
                self.resultat.config(text=f"Mauvaise lettre ! Il vous reste {self.lettres_restantes} essais.")

            self.update_affichage()

            if "-" not in self.affichage:
                self.fin_de_jeu(True)
            elif self.lettres_restantes == 0:
                self.fin_de_jeu(False)

    def update_affichage(self):
        self.affichage = "".join([l if l in self.lettres_trouvees else "-" for l in self.phrase_enigme])
        self.label.config(text=f"Mot : {self.affichage}")

    def fin_de_jeu(self, victoire):
        if victoire:
            self.resultat.config(
                text=f"Bravo ! Vous avez réussi l'épreuve de Rand-Ohm !\n"
                     f"Vous recevez : {self.item} de la panoplie {self.selection_panoplie}\n"
                     f"Localisation : {self.localisation}\n"
                     f"+{self.lettres_restantes} gemmes bleues"
            )
        else:
            self.resultat.config(
                text=f"Échec ! Rand-Ohm a encore gagné !\n"
                     f"Vous trouvez seulement {self.mauvaiseFortune} pièces de cuivre..."
            )
        self.label.config(text="Fin de la partie.")
        self.entry.config(state="disabled")
        self.bouton.config(state="disabled")

# Lancer le jeu
root = tk.Tk()
app = JeuMystere(root)
root.mainloop()
