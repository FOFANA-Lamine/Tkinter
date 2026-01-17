

import tkinter as tk
import customtkinter as ctk

# Configuration globale CustomTkinter
ctk.set_appearance_mode("light")      # "dark" possible
ctk.set_default_color_theme("blue")   # thèmes disponibles : blue, green, dark-blue


class Score:
    def __init__(self):
        self.croix = 0
        self.rond = 0
        self.nuls = 0


class Morphion:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Morphion — Interface moderne")
        self.root.geometry("420x500")

        self.score = Score()
        self.joueur = "X"
        self.plateau = [None] * 9
        self.taille = 300
        self.case = self.taille // 3
        self.partie_terminee = False

        self.creer_interface()
        self.dessiner_grille()

    # ---------------- INTERFACE ----------------

    def creer_interface(self):
        # Titre
        titre = ctk.CTkLabel(
            self.root,
            text="Jeu du Morphion",
            font=("Arial", 20, "bold")
        )
        titre.pack(pady=10)

        # Zone informations
        info = ctk.CTkFrame(self.root)
        info.pack(pady=10, fill="x", padx=20)

        self.label_joueur = ctk.CTkLabel(
            info,
            text="Tour : Croix (Rouge)",
            font=("Arial", 14, "bold")
        )
        self.label_joueur.pack(pady=5)

        self.label_score = ctk.CTkLabel(
            info,
            text=self.texte_score(),
            font=("Arial", 12)
        )
        self.label_score.pack(pady=5)

        # Canvas (Tkinter classique — volontairement conservé)
        self.canvas = tk.Canvas(
            self.root,
            width=self.taille,
            height=self.taille,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.clic)

        # Bouton Nouvelle partie
        ctk.CTkButton(
            self.root,
            text="Nouvelle partie",
            command=self.reinitialiser,
            width=200
        ).pack(pady=15)

    # ---------------- LOGIQUE DU JEU (INCHANGÉ) ----------------

    def texte_score(self):
        return (
            f"Croix : {self.score.croix}   "
            f"Rond : {self.score.rond}   "
            f"Nuls : {self.score.nuls}"
        )

    def dessiner_grille(self):
        for i in range(1, 3):
            self.canvas.create_line(
                i * self.case, 0,
                i * self.case, self.taille,
                width=2
            )
            self.canvas.create_line(
                0, i * self.case,
                self.taille, i * self.case,
                width=2
            )

    def clic(self, event):
        if self.partie_terminee:
            return

        col = event.x // self.case
        lig = event.y // self.case
        index = lig * 3 + col

        if self.plateau[index] is not None:
            return

        self.plateau[index] = self.joueur
        self.dessiner_symbole(lig, col)

        if self.verifier_victoire(self.joueur):
            self.partie_terminee = True
            if self.joueur == "X":
                self.score.victoire_croix()
            else:
                self.score.victoire_rond()
            self.afficher_fin(f"{self.joueur} gagne !")
        elif None not in self.plateau:
            self.partie_terminee = True
            self.score.match_nul()
            self.afficher_fin("Match nul")
        else:
            self.joueur = "O" if self.joueur == "X" else "X"
            self.mettre_a_jour_joueur()

    def dessiner_symbole(self, lig, col):
        x1 = col * self.case + 20
        y1 = lig * self.case + 20
        x2 = (col + 1) * self.case - 20
        y2 = (lig + 1) * self.case - 20

        if self.joueur == "X":
            self.canvas.create_line(x1, y1, x2, y2, width=4, fill="red")
            self.canvas.create_line(x1, y2, x2, y1, width=4, fill="red")
        else:
            self.canvas.create_oval(x1, y1, x2, y2, width=4, outline="blue")

    def verifier_victoire(self, s):
        combinaisons = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        return any(
            self.plateau[a] == self.plateau[b] == self.plateau[c] == s
            for a, b, c in combinaisons
        )

    def afficher_fin(self, message):
        self.label_score.configure(text=self.texte_score())
        self.canvas.create_text(
            150, 150,
            text=message,
            font=("Arial", 16, "bold")
        )

    def mettre_a_jour_joueur(self):
        if self.joueur == "X":
            self.label_joueur.configure(text="Tour : Croix (Rouge)")
        else:
            self.label_joueur.configure(text="Tour : Rond (Bleu)")

    def reinitialiser(self):
        self.canvas.delete("all")
        self.plateau = [None] * 9
        self.partie_terminee = False
        self.joueur = "X"
        self.mettre_a_jour_joueur()
        self.dessiner_grille()

    def lancer(self):
        self.root.mainloop()


if __name__ == "__main__":
    jeu = Morphion()
    jeu.lancer()
