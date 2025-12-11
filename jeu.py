import Mots_liste
import affichage

# Importer le mot à partir du fichier Mots_liste.py
mots = Mots_liste.choisir_mot()
mot_secret = mots

# Registre des informations
jeu = {
        "mot_secret": mot_secret,
        "mot_cache": "_" * len(mot_secret),
        "erreurs": 0,
        "lettres_jouees": set(),
    }

# *** Début du jeu ***

# Importer l'affichage du fichier affichage.py
affichage.afficher_pendu(jeu["erreurs"])
print("Votre mot à deviner :", " ".join(jeu["mot_cache"]), "\n")

# Gestion des lettres entrées
def demander_lettre():
    while True:
        lettre = input("Veuillez entrer une lettre : ").lower()

        if len(lettre) != 1:
            print("Entrez UNE seule lettre à la fois.")
            continue

        if not lettre.isalpha():
            print("Entrez seulement des lettres, pas des chiffres ou symboles.")
            continue

        if lettre in jeu["lettres_jouees"]:
            print("Tu as déjà essayé cette lettre.")
            continue

        return lettre
    
def jouer_tour():
    while True:
        lettre = demander_lettre()

        # Ajouter lettres jouées au registre
        jeu["lettres_jouees"].add(lettre)

        # Si la lettre est dans le mot secret, on affiche la lettre
        if lettre in jeu["mot_secret"]:
            mot_cache_liste = list(jeu["mot_cache"])

            for index, lettres_trouvees in enumerate(jeu["mot_secret"]):
                if lettres_trouvees == lettre:
                    mot_cache_liste[index] = lettre
                   
            jeu["mot_cache"] = "".join(mot_cache_liste)

        # Sinon, on ajoute une partie du corps
        else:
            jeu["erreurs"] += 1

        affichage.afficher_pendu(jeu["erreurs"])
        print("Vos derniers essais :", " | ".join(sorted(jeu["lettres_jouees"])))
        print("\nVotre mot à deviner :", " ".join(jeu["mot_cache"]), "\n")

        # Si toutes les lettres sont trouvées, le joueur a gagné
        if "_" not in jeu["mot_cache"]:
            print("BRAVO champion ! Tu as gagné !")
            break

        # Si le nombre d'erreur arrive à 6, le joueur a perdu
        elif jeu["erreurs"] >= 6:
            print("Dommage, tu as perdu !\n")
            print(f"Le mot secret était : {jeu["mot_secret"]} !")
            break

jouer_tour()