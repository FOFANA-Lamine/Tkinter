
import customtkinter as ctk

# Configuration globale
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class CalculatriceModerne:

    def __init__(self):
        self.fenetre = ctk.CTk()
        self.fenetre.title("Calculatrice Moderne")
        self.fenetre.geometry("360x420")
        self.fenetre.resizable(False, False)

        self.creer_interface()

    # -------------------------------------------------
    def creer_interface(self):

        # Écran
        self.ecran = ctk.CTkEntry(
            self.fenetre,
            font=("Arial", 22),
            justify="right"
        )
        self.ecran.grid(
            row=0, column=0,
            columnspan=4,
            sticky="nsew",
            padx=10, pady=15
        )

        # Boutons
        boutons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('CE', 5, 1)
        ]

        for (texte, ligne, colonne) in boutons:
            btn = ctk.CTkButton(
                self.fenetre,
                text=texte,
                font=("Arial", 16),
                height=45,
                command=lambda t=texte: self.cliquer(t)
            )
            btn.grid(
                row=ligne,
                column=colonne,
                sticky="nsew",
                padx=5,
                pady=5
            )

        # Responsive grid
        for i in range(6):
            self.fenetre.rowconfigure(i, weight=1)

        for i in range(4):
            self.fenetre.columnconfigure(i, weight=1)

    # -------------------------------------------------
    def cliquer(self, valeur):

        if valeur == "=":
            try:
                resultat = eval(self.ecran.get())
                self.ecran.delete(0, ctk.END)
                self.ecran.insert(0, str(resultat))
            except:
                self.ecran.delete(0, ctk.END)
                self.ecran.insert(0, "Erreur")

        elif valeur == "C":
            self.ecran.delete(0, ctk.END)

        elif valeur == "CE":
            contenu = self.ecran.get()
            self.ecran.delete(0, ctk.END)
            self.ecran.insert(0, contenu[:-1])

        else:
            self.ecran.insert(ctk.END, valeur)

    # -------------------------------------------------
    def lancer(self):
        self.fenetre.mainloop()


# Lancement
calc = CalculatriceModerne()
calc.lancer()

