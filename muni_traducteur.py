# Muni traducteur

import tkinter as tk
from tkinter import messagebox

# -----------------------------------------------------
# Fonction de traduction
# -----------------------------------------------------
def traduire():
    mot = entree.get().strip().lower()

    if mot == "":
        resultat.config(text="Veuillez entrer un mot", fg="red")
        return

    # Dictionnaires
    fr_en = {
        "bonjour": "hello",
        "chat": "cat",
        "chien": "dog",
        "maison": "house",
        "merci": "thank you"
    }

    en_fr = {v: k for k, v in fr_en.items()}

    # Sens de traduction
    if sens.get() == "fr_en":
        traduction = fr_en.get(mot)
    else:
        traduction = en_fr.get(mot)

    if traduction:
        resultat.config(text=traduction, fg="green")
    else:
        resultat.config(text="Mot inconnu", fg="orange")


# -----------------------------------------------------
# Fonction pour effacer les champs
# -----------------------------------------------------
def effacer():
    entree.delete(0, tk.END)
    resultat.config(text="")


# -----------------------------------------------------
# Création de la fenêtre principale
# -----------------------------------------------------
fenetre = tk.Tk()
fenetre.title("Mini-traducteur")
fenetre.geometry("350x300")
fenetre.resizable(False, False)

# -----------------------------------------------------
# Titre
# -----------------------------------------------------
tk.Label(
    fenetre,
    text="Traducteur Français / Anglais",
    font=("Arial", 14, "bold")
).pack(pady=10)

# -----------------------------------------------------
# Choix du sens de traduction
# -----------------------------------------------------
sens = tk.StringVar(value="fr_en")

tk.Radiobutton(
    fenetre,
    text="Français → Anglais",
    variable=sens,
    value="fr_en"
).pack(anchor="w", padx=20)

tk.Radiobutton(
    fenetre,
    text="Anglais → Français",
    variable=sens,
    value="en_fr"
).pack(anchor="w", padx=20)

# -----------------------------------------------------
# Champ de saisie
# -----------------------------------------------------
tk.Label(fenetre, text="Mot à traduire :").pack(pady=(15, 5))

entree = tk.Entry(fenetre, width=25)
entree.pack()
entree.focus()

# -----------------------------------------------------
# Boutons
# -----------------------------------------------------
tk.Button(
    fenetre,
    text="Traduire",
    command=traduire
).pack(pady=10)

tk.Button(
    fenetre,
    text="Effacer",
    command=effacer
).pack()

# -----------------------------------------------------
# Résultat
# -----------------------------------------------------
resultat = tk.Label(
    fenetre,
    text="",
    font=("Arial", 12)
)
resultat.pack(pady=15)

# Raccourci clavier : touche Entrée
fenetre.bind("<Return>", lambda event: traduire())

# -----------------------------------------------------
# Boucle principale
# -----------------------------------------------------
fenetre.mainloop()
