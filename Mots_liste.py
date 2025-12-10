import random

# Liste des mots

def choisir_mot():
    mots = ["python", "programmation", "github", "collaboration", "erreur", "definition", "fonctions", "variable", "synthax"]
    return(random.choice(mots))
# Prend un mots alleatoire dans la liste indiquee dans la fonction
print(choisir_mot())
 