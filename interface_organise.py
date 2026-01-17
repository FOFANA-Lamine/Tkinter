
# Application Tkinter — Interface organisée 

import tkinter as tk

# =====================================================
# Fenêtre principale
# =====================================================
fenetre = tk.Tk()
fenetre.title("Application organisée avec Tkinter")
fenetre.geometry("800x500")
fenetre.minsize(600, 400)

# =====================================================
# Frame supérieur (en-tête)
# =====================================================
frame_haut = tk.Frame(fenetre, bg="#2c3e50", height=60)
frame_haut.pack(fill=tk.X)

titre = tk.Label(
    frame_haut,
    text="Application Tkinter bien organisée",
    bg="#2c3e50",
    fg="white",
    font=("Arial", 16, "bold")
)
titre.pack(pady=15)

# =====================================================
# Zone centrale redimensionnable (PanedWindow)
# =====================================================
paned = tk.PanedWindow(fenetre, orient=tk.HORIZONTAL)
paned.pack(fill=tk.BOTH, expand=True)

# -----------------------------------------------------
# Zone gauche : menu
# -----------------------------------------------------
frame_gauche = tk.Frame(paned, bg="#ecf0f1", width=200)
paned.add(frame_gauche)

label_menu = tk.Label(
    frame_gauche,
    text="Menu",
    bg="#ecf0f1",
    font=("Arial", 12, "bold")
)
label_menu.pack(pady=10)

def afficher_message():
    contenu.config(text="Vous avez cliqué sur un bouton du menu.")

btn_action = tk.Button(
    frame_gauche,
    text="Action",
    command=afficher_message
)
btn_action.pack(pady=5)

def ouvrir_apropos():
    apropos = tk.Toplevel(fenetre)
    apropos.title("À propos")
    apropos.geometry("300x150")
    apropos.resizable(False, False)

    tk.Label(
        apropos,
        text="Application pédagogique Tkinter\nVersion 1.0",
        font=("Arial", 11)
    ).pack(pady=20)

    tk.Button(
        apropos,
        text="Fermer",
        command=apropos.destroy
    ).pack()

btn_apropos = tk.Button(
    frame_gauche,
    text="À propos",
    command=ouvrir_apropos
)
btn_apropos.pack(pady=5)

# -----------------------------------------------------
# Zone droite : contenu principal
# -----------------------------------------------------
frame_droite = tk.Frame(paned, bg="white")
paned.add(frame_droite)

label_contenu = tk.Label(
    frame_droite,
    text="Zone de travail",
    bg="white",
    font=("Arial", 14)
)
label_contenu.pack(pady=20)

contenu = tk.Label(
    frame_droite,
    text="Sélectionnez une action dans le menu de gauche.",
    bg="white",
    font=("Arial", 11)
)
contenu.pack(pady=10)

# =====================================================
# Lancement de l'application
# =====================================================
fenetre.mainloop()
