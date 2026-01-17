

# Jeu morphion — Interface modernisée avec CustomTkinter
# LOGIQUE STRICTEMENT IDENTIQUE

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import random
import json

# -----------------------------------------------------
# CONFIGURATION CUSTOMTKINTER
# -----------------------------------------------------
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# =====================================================
# CLASSE SCORE
# =====================================================
class Score:
    def __init__(self):
        self.croix = 0
        self.rond = 0
        self.nuls = 0


# =====================================================
# IA (logique pure — inchangée)
# =====================================================
def verifier_victoire(plateau, s):
    combinaisons = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(plateau[a] == plateau[b] == plateau[c] == s for a,b,c in combinaisons)


def coup_ordinateur(plateau, symbole_ordi, symbole_joueur):
    for i in range(9):
        if plateau[i] is None:
            plateau[i] = symbole_ordi
            if verifier_victoire(plateau, symbole_ordi):
                plateau[i] = None
                return i
            plateau[i] = None

    for i in range(9):
        if plateau[i] is None:
            plateau[i] = symbole_joueur
            if verifier_victoire(plateau, symbole_joueur):
                plateau[i] = None
                return i
            plateau[i] = None

    if plateau[4] is None:
        return 4

    coins = [0,2,6,8]
    libres = [c for c in coins if plateau[c] is None]
    if libres:
        return random.choice(libres)

    return random.choice([i for i in range(9) if plateau[i] is None])


# =====================================================
# CLASSE PRINCIPALE
# =====================================================
class Morphion:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Jeu du Morphion — Version moderne")
        self.root.resizable(False, False)

        self.score = Score()
        self.joueur = "X"
        self.plateau = [None] * 9
        self.historique = []
        self.partie_terminee = False

        self.taille = 300
        self.case = self.taille // 3

        self.mode = tk.StringVar(value="JvJ")

        self.creer_menu()
        self.creer_interface()
        self.dessiner_grille()

    # -------------------------------------------------
    def creer_menu(self):
        menu = tk.Menu(self.root)

        jeu = tk.Menu(menu, tearoff=0)
        jeu.add_command(label="Nouvelle partie", command=self.reinitialiser)
        jeu.add_command(label="Sauvegarder", command=self.sauvegarder_partie)
        jeu.add_command(label="Charger", command=self.charger_partie)
        jeu.add_separator()
        jeu.add_command(label="Quitter", command=self.root.quit)

        aide = tk.Menu(menu, tearoff=0)
        aide.add_command(label="Règles du jeu", command=self.afficher_regles)

        menu.add_cascade(label="Jeu", menu=jeu)
        menu.add_cascade(label="Aide", menu=aide)

        self.root.config(menu=menu)

    # -------------------------------------------------
    def creer_interface(self):
        top = ctk.CTkFrame(self.root)
        top.pack(pady=10, fill="x")

        self.label_joueur = ctk.CTkLabel(
            top,
            text="Tour : Croix (Rouge)",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.label_joueur.pack(side="left", padx=20)

        self.label_score = ctk.CTkLabel(
            top,
            text=self.texte_score(),
            font=ctk.CTkFont(size=13)
        )
        self.label_score.pack(side="right", padx=20)

        modes = ctk.CTkFrame(self.root)
        modes.pack(pady=5)

        ctk.CTkRadioButton(modes, text="Joueur vs Joueur",
                           variable=self.mode, value="JvJ").pack(anchor="w")
        ctk.CTkRadioButton(modes, text="Joueur vs Ordinateur (Facile)",
                           variable=self.mode, value="IA_FACILE").pack(anchor="w")
        ctk.CTkRadioButton(modes, text="Joueur vs Ordinateur (Difficile)",
                           variable=self.mode, value="IA_DIFFICILE").pack(anchor="w")

        # Canvas Tkinter (inchangé)
        self.canvas = tk.Canvas(self.root, width=self.taille,
                                height=self.taille, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.clic)

        histo_frame = ctk.CTkFrame(self.root)
        histo_frame.pack(pady=5, fill="x")

        ctk.CTkLabel(histo_frame, text="Historique des coups").pack()

        self.zone_historique = ctk.CTkTextbox(
            histo_frame, height=100, width=360
        )
        self.zone_historique.pack(pady=5)

    # -------------------------------------------------
    def texte_score(self):
        return f"Croix : {self.score.croix} | Rond : {self.score.rond} | Nuls : {self.score.nuls}"

    def dessiner_grille(self):
        for i in range(1,3):
            self.canvas.create_line(i*self.case, 0, i*self.case, self.taille, width=2)
            self.canvas.create_line(0, i*self.case, self.taille, i*self.case, width=2)

    # -------------------------------------------------
    def clic(self, event):
        if self.partie_terminee:
            return

        col = event.x // self.case
        lig = event.y // self.case
        index = lig * 3 + col

        if index < 0 or index > 8 or self.plateau[index] is not None:
            return

        self.jouer_coup(index)

        if self.mode.get().startswith("IA") and not self.partie_terminee and self.joueur == "O":
            self.root.after(500, self.jouer_ordinateur)

    # -------------------------------------------------
    def jouer_coup(self, index):
        self.plateau[index] = self.joueur
        self.historique.append((self.joueur, index))
        self.dessiner_symbole(index)
        self.afficher_historique()

        if verifier_victoire(self.plateau, self.joueur):
            self.fin_partie(f"{self.joueur} gagne")
        elif None not in self.plateau:
            self.score.nuls += 1
            self.fin_partie("Match nul")
        else:
            self.joueur = "O" if self.joueur == "X" else "X"
            self.mettre_a_jour_joueur()

    # -------------------------------------------------
    def jouer_ordinateur(self):
        if self.mode.get() == "IA_FACILE":
            index = random.choice([i for i in range(9) if self.plateau[i] is None])
        else:
            index = coup_ordinateur(self.plateau, "O", "X")
        self.jouer_coup(index)

    # -------------------------------------------------
    def dessiner_symbole(self, index):
        lig, col = divmod(index, 3)
        x1 = col*self.case + 20
        y1 = lig*self.case + 20
        x2 = (col+1)*self.case - 20
        y2 = (lig+1)*self.case - 20

        if self.joueur == "X":
            self.canvas.create_line(x1,y1,x2,y2,width=4,fill="red")
            self.canvas.create_line(x1,y2,x2,y1,width=4,fill="red")
        else:
            self.canvas.create_oval(x1,y1,x2,y2,width=4,outline="blue")

    # -------------------------------------------------
    def fin_partie(self, message):
        self.partie_terminee = True

        if message.startswith("X"):
            self.score.croix += 1
        elif message.startswith("O"):
            self.score.rond += 1

        self.label_score.configure(text=self.texte_score())
        self.animation_victoire(message)

    def animation_victoire(self, texte, c=0):
        couleurs = ["green", "white"]
        if c < 6:
            self.canvas.delete("msg")
            self.canvas.create_text(
                150,150,text=texte,
                font=("Arial",18,"bold"),
                fill=couleurs[c%2],tag="msg"
            )
            self.root.after(400, lambda: self.animation_victoire(texte, c+1))

    # -------------------------------------------------
    def afficher_historique(self):
        self.zone_historique.delete("1.0", "end")
        for i,(j,p) in enumerate(self.historique,1):
            self.zone_historique.insert("end", f"Tour {i} : {j} → case {p+1}\n")

    # -------------------------------------------------
    def mettre_a_jour_joueur(self):
        txt = "Croix (Rouge)" if self.joueur == "X" else "Rond (Bleu)"
        self.label_joueur.configure(text=f"Tour : {txt}")

    # -------------------------------------------------
    def sauvegarder_partie(self):
        data = {
            "plateau": self.plateau,
            "joueur": self.joueur,
            "score": self.score.__dict__,
            "historique": self.historique
        }
        with open("sauvegarde_morpion.json","w") as f:
            json.dump(data,f)
        messagebox.showinfo("Sauvegarde","Partie sauvegardée")

    def charger_partie(self):
        try:
            with open("sauvegarde_morpion.json","r") as f:
                data = json.load(f)
            self.plateau = data["plateau"]
            self.joueur = data["joueur"]
            self.historique = data["historique"]
            self.score.__dict__.update(data["score"])
            self.reconstruire()
        except:
            messagebox.showerror("Erreur","Aucune sauvegarde trouvée")

    def reconstruire(self):
        self.canvas.delete("all")
        self.dessiner_grille()
        for i,s in enumerate(self.plateau):
            if s:
                self.joueur = s
                self.dessiner_symbole(i)
        self.mettre_a_jour_joueur()
        self.afficher_historique()
        self.label_score.configure(text=self.texte_score())

    # -------------------------------------------------
    def afficher_regles(self):
        messagebox.showinfo(
            "Règles du jeu",
            "• Deux joueurs : Croix et Rond\n"
            "• Jouez chacun votre tour\n"
            "• Alignez 3 symboles pour gagner\n"
            "• Sinon : match nul"
        )

    def reinitialiser(self):
        self.canvas.delete("all")
        self.plateau = [None]*9
        self.historique.clear()
        self.partie_terminee = False
        self.joueur = "X"
        self.mettre_a_jour_joueur()
        self.dessiner_grille()
        self.zone_historique.delete("1.0","end")

    # -------------------------------------------------
    def lancer(self):
        self.root.mainloop()


# =====================================================
# LANCEMENT
# =====================================================
if __name__ == "__main__":
    Morphion().lancer()
