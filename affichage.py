
def afficher_pendu(erreurs):
    if erreurs == 0:
        print("""\n========Y=
||/
||
||
||
||\\
=============\n
""")
    elif erreurs == 1:
        print("""\n========Y=
||/     |
||      O
||
||
||\\
=============\n
""")
    elif erreurs == 2:
        print("""\n========Y=
||/     |
||      O
||      |
||
||\\
=============\n
""")
    elif erreurs == 3:
        print("""\n========Y=
||/     |
||      O
||     /|
||
||\\
=============\n
""")
    elif erreurs == 4:
        print("""\n========Y=
||/     |
||      O
||     /|\\
||
||\\
=============\n
""")

    elif erreurs == 5:
        print("""\n========Y=
||/     |
||      O
||     /|\\
||     /
||\\
=============\n
""")

    else:
        print("""\n========Y=
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