chemin = r"C:\Users\simplon\Desktop\TP.txt"
print("*******Bienvenu sur notre site de renseignement******")
print("Pour commencer, veuillez choisir l'un des deux numéros selon votre préocupation")
choix = input("Veuillez taper (1)si vous-voulez vous inscrit et (2)si vous-voulez vous consulter la liste des personnes enregistrer : ")
choix = int(choix)
if(choix==1):
    nom = input("Veuillez entrez votre nom : ")
    with open(chemin, "a") as f:
        f.write("\nNom : " + nom)
    prenom = input("Veuillez entrez votre prenom : ")
    with open(chemin, "a") as f:
        f.write("\nPrenom : " + prenom)
    numero_telephone = input("Veuillez entrez votre numéro de téléphone : ")
    with open(chemin, "a") as f:
        f.write("\nnuméro de téléphone : " + numero_telephone)
    email = input("veuillez entrez votre email : ")
    with open(chemin, "a") as f:
        f.write("\nemail: " + email)
elif(choix == 2):
    with open(chemin,"r")as f :
        contenu = f.read()
        print(contenu)
else:
    print("choix non disponible assurez-vous de choisir entre l'option (1 et 2)!")