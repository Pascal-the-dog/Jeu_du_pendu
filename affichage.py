
def afficher_pendu(erreurs):
    if erreurs == 0:
        print("""========Y=
||/
||
||
||
||\\
=============\n
""")
    elif erreurs == 1:
        print("""========Y=
||/     |
||      O
||
||
||\\
=============\n
""")
    elif erreurs == 2:
        print("""========Y=
||/     |
||      O
||      |
||
||\\
=============\n
""")
    elif erreurs == 3:
        print("""========Y=
||/     |
||      O
||     /|
||
||\\
=============\n
""")
    elif erreurs == 4:
        print("""========Y=
||/     |
||      O
||     /|\\
||
||\\
=============\n
""")

    elif erreurs == 5:
        print("""========Y=
||/     |
||      O
||     /|\\
||     /
||\\
=============\n
""")

    else:
        print("""========Y=
||/     |
||      O
||     /|\\       t
||     / \\      / \\
||\\            |rip|
=====================\n
""")

    # Dessins ASCII selon le nombre d'erreurs

# #tests
# afficher_pendu(0)
# afficher_pendu(1)
# afficher_pendu(2)
# afficher_pendu(3)
# afficher_pendu(4)
# afficher_pendu(5)
# afficher_pendu(6)