

import customtkinter as ctk
from tkinter import messagebox


# --------------------------------------------------
# Configuration globale
# --------------------------------------------------
ctk.set_appearance_mode("system")       # light / dark / system
ctk.set_default_color_theme("blue")     # blue / green / dark-blue


# --------------------------------------------------
# Fenêtre secondaire après connexion
# --------------------------------------------------
class FenetreAccueil(ctk.CTkToplevel):

    def __init__(self, parent, utilisateur):
        super().__init__(parent)

        self.title("Accueil")
        self.geometry("400x250")
        self.resizable(False, False)

        label = ctk.CTkLabel(
            self,
            text=f"Bienvenue {utilisateur} 👋",
            font=("Arial", 20, "bold")
        )
        label.pack(pady=40)

        btn_quitter = ctk.CTkButton(
            self,
            text="Quitter",
            command=self.destroy
        )
        btn_quitter.pack(pady=20)


# --------------------------------------------------
# Application principale
# --------------------------------------------------
class ApplicationConnexion(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Application Moderne - Connexion")
        self.geometry("420x420")
        self.resizable(False, False)

        self.creer_interface()

    # --------------------------------------------------
    # Interface graphique
    # --------------------------------------------------
    def creer_interface(self):

        # Titre
        self.label_titre = ctk.CTkLabel(
            self,
            text="Connexion",
            font=("Arial", 26, "bold")
        )
        self.label_titre.pack(pady=25)

        # Champ utilisateur
        self.entry_user = ctk.CTkEntry(
            self,
            placeholder_text="Nom d'utilisateur"
        )
        self.entry_user.pack(padx=40, pady=10, fill="x")

        # Champ mot de passe
        self.entry_password = ctk.CTkEntry(
            self,
            placeholder_text="Mot de passe",
            show="*"
        )
        self.entry_password.pack(padx=40, pady=10, fill="x")

        # Message d'information
        self.label_message = ctk.CTkLabel(
            self,
            text="",
            text_color="red"
        )
        self.label_message.pack(pady=5)

        # Bouton connexion
        self.btn_connexion = ctk.CTkButton(
            self,
            text="Se connecter",
            command=self.verifier_connexion
        )
        self.btn_connexion.pack(pady=15)

        # Bouton thème
        self.btn_theme = ctk.CTkButton(
            self,
            text="Changer le thème",
            command=self.changer_theme,
            fg_color="gray"
        )
        self.btn_theme.pack(pady=5)

    # --------------------------------------------------
    # Logique métier
    # --------------------------------------------------
    def verifier_connexion(self):
        utilisateur = self.entry_user.get()
        mot_de_passe = self.entry_password.get()

        if not utilisateur or not mot_de_passe:
            self.label_message.configure(
                text="Veuillez remplir tous les champs."
            )
            return

        # Identifiants fictifs (pédagogiques)
        if utilisateur == "admin" and mot_de_passe == "1234":
            self.label_message.configure(text="")
            messagebox.showinfo(
                "Succès",
                "Connexion réussie"
            )
            FenetreAccueil(self, utilisateur)
        else:
            self.label_message.configure(
                text="Identifiants incorrects."
            )

    # --------------------------------------------------
    # Gestion du thème
    # --------------------------------------------------
    def changer_theme(self):
        mode_actuel = ctk.get_appearance_mode()

        if mode_actuel == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")


# --------------------------------------------------
# Lancement de l'application
# --------------------------------------------------
if __name__ == "__main__":
    app = ApplicationConnexion()
    app.mainloop()
