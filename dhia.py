class Calculs:
    # Méthode pour calculer la somme d'un tableau d'entiers
   
    def calculerSomme(tableau):
        somme = 0
        for nombre in tableau:
            somme += nombre
        return somme
    




    # Méthode pour calculer la moyenne d'un tableau d'entiers
    
    def calculerMoyenne(tableau):
        if len(tableau) == 0:
            return 0.0  
        somme = Calculs.calculerSomme(tableau)
        return somme / len(tableau)

# Exemple d'utilisation
tableau = [10, 20, 30, 40, 50]
print("Somme:", Calculs.calculerSomme(tableau))
print("Moyenne:", Calculs.calculerMoyenne(tableau))

