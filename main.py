from souhaiel import GestionListe;
from dhia import Calculs
from wissem import GestionChaine

def main():
    



    # Test de la classe Calculs
    tableau = [10, 20, 30, 40, 50]
    print("\nSomme:", Calculs.calculerSomme(tableau))
    print("Moyenne:", Calculs.calculerMoyenne(tableau))

    chaine = "Bonjour, monde!"

    chaine_majuscule = GestionChaine.convertir_en_majuscule(chaine)
    print("Chaîne en majuscule :", chaine_majuscule)

    longueur_chaine = GestionChaine.calculer_longueur_chaine(chaine)
    print("Longueur de la chaîne :", longueur_chaine)



if __name__ == "__main__":
    main()
