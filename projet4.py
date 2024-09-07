def calculatrice(num1, num2):
    operateur = input("Saisir un opérateur (+, -, *, /) : ")
    
    if operateur == '+':
        return num1 + num2
    elif operateur == '-':
        return num1 - num2
    elif operateur == '*':
        return num1 * num2
    elif operateur == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Opérateur invalide"

try:
    numero1 = float(input("Entrez le premier chiffre : "))
    numero2 = float(input("Entrez le deuxième chiffre : "))

    resultat = calculatrice(numero1, numero2)
    print("Le résultat est :", resultat)
except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")
