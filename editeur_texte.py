
# Editeur de texte avec menu

import tkinter as tk
from tkinter import filedialog, messagebox


class EditeurTexte:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Éditeur de Texte - Sans titre")
        self.fenetre.geometry("800x600")

        self.fichier_actuel = None

        self.creer_menu()
        self.creer_zone_texte()

        # Liaisons clavier
        self.fenetre.bind("<Control-s>", self.sauvegarder)
        self.fenetre.bind("<Control-o>", self.ouvrir)
        self.fenetre.bind("<Control-n>", self.nouveau)

    def creer_menu(self):
        menubar = tk.Menu(self.fenetre)

        # Menu Fichier
        menu_fichier = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fichier", menu=menu_fichier)
        menu_fichier.add_command(label="Nouveau", accelerator="Ctrl+N", command=self.nouveau)
        menu_fichier.add_command(label="Ouvrir", accelerator="Ctrl+O", command=self.ouvrir)
        menu_fichier.add_command(label="Sauvegarder", accelerator="Ctrl+S", command=self.sauvegarder)
        menu_fichier.add_command(label="Sauvegarder sous...", command=self.sauvegarder_sous)
        menu_fichier.add_separator()
        menu_fichier.add_command(label="Quitter", command=self.quitter)

        # Menu Édition
        menu_edition = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Édition", menu=menu_edition)
        menu_edition.add_command(label="Annuler", command=self.annuler)
        menu_edition.add_command(label="Rétablir", command=self.retablir)
        menu_edition.add_separator()
        menu_edition.add_command(label="Couper", command=self.couper)
        menu_edition.add_command(label="Copier", command=self.copier)
        menu_edition.add_command(label="Coller", command=self.coller)

        self.fenetre.config(menu=menubar)

    def creer_zone_texte(self):
        # Cadre pour la zone de texte et la scrollbar
        cadre = tk.Frame(self.fenetre)
        cadre.pack(fill="both", expand=True)

        # Zone de texte
        self.zone_texte = tk.Text(cadre, wrap="word", undo=True)
        self.zone_texte.pack(side="left", fill="both", expand=True)

        # Scrollbar verticale
        scrollbar = tk.Scrollbar(cadre, command=self.zone_texte.yview)
        scrollbar.pack(side="right", fill="y")
        self.zone_texte.config(yscrollcommand=scrollbar.set)

        # Scrollbar horizontale
        scrollbar_h = tk.Scrollbar(self.fenetre, orient="horizontal",
                                   command=self.zone_texte.xview)
        scrollbar_h.pack(side="bottom", fill="x")
        self.zone_texte.config(xscrollcommand=scrollbar_h.set)

    def nouveau(self, event=None):
        if self.verifier_sauvegarde():
            self.zone_texte.delete(1.0, tk.END)
            self.fichier_actuel = None
            self.fenetre.title("Éditeur de Texte - Sans titre")

    def ouvrir(self, event=None):
        if self.verifier_sauvegarde():
            fichier = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=[("Fichiers texte", "*.txt"),
                           ("Tous les fichiers", "*.*")]
            )
            if fichier:
                try:
                    with open(fichier, 'r', encoding='utf-8') as f:
                        contenu = f.read()
                    self.zone_texte.delete(1.0, tk.END)
                    self.zone_texte.insert(1.0, contenu)
                    self.fichier_actuel = fichier
                    self.fenetre.title(f"Éditeur de Texte - {fichier}")
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier:\n{e}")

    def sauvegarder(self, event=None):
        if self.fichier_actuel:
            try:
                with open(self.fichier_actuel, 'w', encoding='utf-8') as f:
                    f.write(self.zone_texte.get(1.0, tk.END))
                messagebox.showinfo("Sauvegarde", "Fichier sauvegardé avec succès!")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur de sauvegarde:\n{e}")
        else:
            self.sauvegarder_sous()

    def sauvegarder_sous(self):
        fichier = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichiers texte", "*.txt"),
                       ("Tous les fichiers", "*.*")]
        )
        if fichier:
            self.fichier_actuel = fichier
            self.sauvegarder()
            self.fenetre.title(f"Éditeur de Texte - {fichier}")

    def verifier_sauvegarde(self):
        if self.zone_texte.edit_modified():
            reponse = messagebox.askyesnocancel(
                "Sauvegarder",
                "Voulez-vous sauvegarder les modifications?"
            )
            if reponse is None:  # Annuler
                return False
            elif reponse:  # Oui
                self.sauvegarder()
        return True

    def annuler(self):
        self.zone_texte.edit_undo()

    def retablir(self):
        self.zone_texte.edit_redo()

    def couper(self):
        self.zone_texte.event_generate("<<Cut>>")

    def copier(self):
        self.zone_texte.event_generate("<<Copy>>")

    def coller(self):
        self.zone_texte.event_generate("<<Paste>>")

    def quitter(self):
        if self.verifier_sauvegarde():
            self.fenetre.quit()

    def lancer(self):
        self.fenetre.mainloop()


# Lancer l'éditeur
if __name__ == "__main__":
    editeur = EditeurTexte()
    editeur.lancer()