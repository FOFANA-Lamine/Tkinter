

import tkinter as tk
import customtkinter as ctk

# -----------------------------------------------------
# Configuration globale CustomTkinter
# -----------------------------------------------------
ctk.set_appearance_mode("Dark")       # "Light" / "Dark" / "System"
ctk.set_default_color_theme("blue")


class Morphion:
    def __init__(self):
        # ===============================
        # Fenêtre principale (MODERNE)
        # ===============================
        self.root = ctk.CTk()
        self.root.title("Jeu du Morphion")
        self.root.geometry("360x450")
        self.root.resizable(False, False)

        # ===============================
        # Titre du jeu (UI uniquement)
        # ===============================
        self.titre = ctk.CTkLabel(
            self.root,
            text="Jeu du Morphion",
            font=("Arial", 20, "bold")
        )
        self.titre.pack(pady=10)

        # ===============================
        # Zone graphique du jeu (Canvas)
        # ===============================
        self.taille = 300
        self.case = self.taille // 3

        self.canvas = tk.Canvas(
            self.root,
            width=self.taille,
            height=self.taille,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack(pady=5)

        # ===============================
        # Bouton Rejouer (UI uniquement)
        # ===============================
        self.btn_reset = ctk.CTkButton(
            self.root,
            text="Rejouer",
            command=self.reinitialiser
        )
        self.btn_reset.pack(pady=15)

        # ===============================
        # Logique du jeu 
        # ===============================
        self.joueur = "X"  # X = Croix rouge, O = Rond bleu
        self.plateau = [None] * 9
        self.partie_terminee = False

        self.dessiner_grille()
        self.canvas.bind("<Button-1>", self.clic)

    # -------------------------------------------------
    # DESSIN DE LA GRILLE 
    # -------------------------------------------------
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

    # -------------------------------------------------
    # GESTION DU CLIC 
    # -------------------------------------------------
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
            self.afficher_message(f"Le joueur {self.joueur} a gagné !")
            self.partie_terminee = True
        elif None not in self.plateau:
            self.afficher_message("Match nul !")
            self.partie_terminee = True
        else:
            self.joueur = "O" if self.joueur == "X" else "X"

    # -------------------------------------------------
    # DESSIN DES SYMBOLES 
    # -------------------------------------------------
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

    # -------------------------------------------------
    # VÉRIFICATION DE LA VICTOIRE 
    # -------------------------------------------------
    def verifier_victoire(self, symbole):
        combinaisons = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in combinaisons:
            if self.plateau[a] == self.plateau[b] == self.plateau[c] == symbole:
                return True
        return False

    # -------------------------------------------------
    # AFFICHAGE MESSAGE FIN DE PARTIE 
    # -------------------------------------------------
    def afficher_message(self, texte):
        self.canvas.create_rectangle(40, 120, 260, 180, fill="white")
        self.canvas.create_text(
            150, 150,
            text=texte,
            font=("Arial", 14, "bold")
        )

    # -------------------------------------------------
    # RÉINITIALISATION (AJOUT UI, LOGIQUE SIMPLE)
    # -------------------------------------------------
    def reinitialiser(self):
        self.canvas.delete("all")
        self.plateau = [None] * 9
        self.joueur = "X"
        self.partie_terminee = False
        self.dessiner_grille()

    # -------------------------------------------------
    # LANCEMENT
    # -------------------------------------------------
    def lancer(self):
        self.root.mainloop()


if __name__ == "__main__":
    jeu = Morphion()
    jeu.lancer()
