
# =====================================================
# ÉDITEUR DE TEXTE MODERNE — CUSTOMTKINTER
# =====================================================

import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

# -----------------------------------------------------
# Configuration globale de CustomTkinter
# -----------------------------------------------------

ctk.set_appearance_mode("System")   # "Light", "Dark", ou "System"
ctk.set_default_color_theme("blue") # Thème moderne par défaut


# =====================================================
# CLASSE PRINCIPALE DE L'APPLICATION
# =====================================================

class EditeurTexteModerne(ctk.CTk):

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Configuration de la fenêtre
        # -----------------------------
        self.title("Éditeur Moderne — Sans titre")
        self.geometry("900x600")

        # Fichier actuellement ouvert
        self.fichier_actuel = None

        # -----------------------------
        # Création de l'interface
        # -----------------------------
        self.creer_toolbar()
        self.creer_zone_texte()
        self.creer_barre_statut()
        self.creer_raccourcis()

    # =================================================
    # TOOLBAR (BARRE SUPÉRIEURE)
    # =================================================
    def creer_toolbar(self):
        """Barre d’outils avec boutons principaux"""

        self.toolbar = ctk.CTkFrame(self, height=40)
        self.toolbar.pack(fill="x", padx=5, pady=5)

        ctk.CTkButton(
            self.toolbar, text="Nouveau",
            command=self.nouveau
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.toolbar, text="Ouvrir",
            command=self.ouvrir
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.toolbar, text="Sauvegarder",
            command=self.sauvegarder
        ).pack(side="left", padx=5)

        # Bouton changement de thème
        ctk.CTkButton(
            self.toolbar, text="☀ / ☾",
            width=40,
            command=self.changer_theme
        ).pack(side="right", padx=5)

    # =================================================
    # ZONE DE TEXTE
    # =================================================
    def creer_zone_texte(self):
        """Zone principale d’édition"""

        self.zone_texte = ctk.CTkTextbox(
            self,
            wrap="word",
            font=("Consolas", 14)
        )
        self.zone_texte.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=(0, 5)
        )

    # =================================================
    # BARRE DE STATUT
    # =================================================
    def creer_barre_statut(self):
        """Affiche l'état du document"""

        self.barre_statut = ctk.CTkLabel(
            self,
            text="Prêt",
            anchor="w"
        )
        self.barre_statut.pack(fill="x", padx=10, pady=5)

    # =================================================
    # RACCOURCIS CLAVIER
    # =================================================
    def creer_raccourcis(self):
        """Raccourcis clavier standards"""

        self.bind("<Control-n>", lambda e: self.nouveau())
        self.bind("<Control-o>", lambda e: self.ouvrir())
        self.bind("<Control-s>", lambda e: self.sauvegarder())

    # =================================================
    # FONCTIONS FICHIER
    # =================================================
    def nouveau(self):
        """Nouveau document"""
        self.zone_texte.delete("1.0", "end")
        self.fichier_actuel = None
        self.title("Éditeur Moderne — Sans titre")
        self.barre_statut.configure(text="Nouveau document")

    def ouvrir(self):
        """Ouvrir un fichier texte"""
        chemin = filedialog.askopenfilename(
            filetypes=[("Fichiers texte", "*.txt"),
                       ("Tous les fichiers", "*.*")]
        )

        if chemin:
            with open(chemin, "r", encoding="utf-8") as f:
                contenu = f.read()

            self.zone_texte.delete("1.0", "end")
            self.zone_texte.insert("1.0", contenu)

            self.fichier_actuel = chemin
            self.title(f"Éditeur Moderne — {os.path.basename(chemin)}")
            self.barre_statut.configure(text="Fichier ouvert")

    def sauvegarder(self):
        """Sauvegarde du fichier"""
        if not self.fichier_actuel:
            self.sauvegarder_sous()
            return

        with open(self.fichier_actuel, "w", encoding="utf-8") as f:
            f.write(self.zone_texte.get("1.0", "end"))

        self.barre_statut.configure(text="Fichier sauvegardé")

    def sauvegarder_sous(self):
        """Sauvegarde sous"""
        chemin = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichiers texte", "*.txt")]
        )

        if chemin:
            self.fichier_actuel = chemin
            self.sauvegarder()
            self.title(f"Éditeur Moderne — {os.path.basename(chemin)}")

    # =================================================
    # THÈME CLAIR / SOMBRE
    # =================================================
    def changer_theme(self):
        """Bascule clair / sombre"""
        actuel = ctk.get_appearance_mode()
        nouveau = "Dark" if actuel == "Light" else "Light"
        ctk.set_appearance_mode(nouveau)
        self.barre_statut.configure(text=f"Thème : {nouveau}")


# =====================================================
# LANCEMENT DE L'APPLICATION
# =====================================================

if __name__ == "__main__":
    app = EditeurTexteModerne()
    app.mainloop()
