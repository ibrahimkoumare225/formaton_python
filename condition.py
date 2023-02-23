age = input("Veuillez ebtrez votre age :")
age = int(age)
if(age<18):
    print("Vous êtes mineur")
elif(age==18):
    print("Félicitation vous êtes majeur")
else:
    print("Vous avez plus de 18 ans")