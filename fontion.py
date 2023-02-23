
def moyenne(notes):
    moyenne=0
    resultat=0
    for chiffres in notes:
        resultat =resultat+chiffres
    moyenne=resultat/3
    return moyenne

notes=[15,17,19]
moyenne(notes)
print(moyenne(notes))