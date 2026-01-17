
#   CALCULATRICE AVEC TKINTER

import tkinter as tk


class Calculatrice:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Calculatrice")

        # Écran
        # tk.Entry() crée un champ de saisie texte (l'écran de la calculatrice)
        """ Explication :
        self.fenetre : place le widget dans la fenêtre principale
        font=("Arial", 20) : police Arial taille 20  
        justify="right" : aligne le texte à droite (comme une vraie calculatrice) 
        bd=10 : bordure de 10 pixels
        relief=tk.SUNKEN : effet visuel "enfoncé" pour l'écran
        columnspan=4 : occupe 4 colonnes
        sticky="nsew" : s'étend dans toutes les directions (nord, sud, est, ouest) 
        padx=5, pady=5 : marges horizontales et verticales de 5 pixels
        """
        self.ecran = tk.Entry(self.fenetre,
                              font=("Arial", 20),
                              justify="right",
                              bd=10,
                              relief=tk.SUNKEN
                              )

        self.ecran.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Boutons
        boutons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('AC', 5, 0), ('DEL', 5, 1)
        ]

        for (texte, ligne, colonne) in boutons:
            btn = tk.Button(self.fenetre,
                            text=texte,
                            font=("Arial", 14),
                            height=2,
                            width=5,
                            command =lambda t=texte: self.cliquer(t) )  # t=texte capture la valeur actuelle de texte (évite un problème commun avec les closures)

            btn.grid(row=ligne, column=colonne, sticky="nsew", padx=2, pady=2)

        # Ajustement des tailles : Le poids détermine comment l'espace supplémentaire est distribué
        for i in range(6):
            self.fenetre.rowconfigure(i, weight=1)  # rowconfigure(i, weight=1) : donne un poids de 1 à chaque ligne (0 à 5)
        for i in range(4):
            self.fenetre.columnconfigure(i, weight=1)  # columnconfigure(i, weight=1) : donne un poids de 1 à chaque colonne (0 à 3)

    def cliquer(self, valeur):
        if valeur == '=':
            try:
                resultat = eval(self.ecran.get())
                self.ecran.delete(0, tk.END)
                self.ecran.insert(0, str(resultat))
            except:
                self.ecran.delete(0, tk.END)
                self.ecran.insert(0, "Erreur")
        elif valeur == 'AC':
            self.ecran.delete(0, tk.END)
        elif valeur == 'DEL':
            self.ecran.delete(len(self.ecran.get()) - 1, tk.END)
        else:
            self.ecran.insert(tk.END, valeur)

    def lancer(self):
        self.fenetre.mainloop()

calc = Calculatrice()
calc.lancer()






