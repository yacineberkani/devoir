
from collections import Counter

def generer_permutation_depuis_nom(nom):
    nom = nom.upper()
    caracteres_uniques = []
    for char in nom:
        if char not in caracteres_uniques and 'A' <= char <= 'Z':
            caracteres_uniques.append(char)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in caracteres_uniques:
            caracteres_uniques.append(char)
    tableau = [caracteres_uniques[i:i+9] for i in range(0, len(caracteres_uniques), 9)]
    print("tableau 3x9 :", tableau, "\n")
    permutation = []
    for col in range(9):
        for row in range(3):
            if col < len(tableau[row]):
                permutation.append(tableau[row][col])

    return permutation


def creer_dictionnaire_substitution(permutation):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return {alphabet[i]: permutation[i] for i in range(len(alphabet))}

def chiffrer_texte(texte_entree, dictionnaire_substitution):
    # 
    texte_chiffre = ""
    for char in texte_entree.upper():
        if char in dictionnaire_substitution:
            texte_chiffre += dictionnaire_substitution[char]
        else:
            texte_chiffre += char  
    return texte_chiffre


with open("CSIA.txt", "r") as fichier:
    texte_original = fichier.read()


dictionnaire_substitution = creer_dictionnaire_substitution(permutation)
texte_chiffre = chiffrer_texte(texte_original, dictionnaire_substitution)







def analyse_frequence(texte):
    compteur = Counter([char for char in texte.upper() if 'A' <= char <= 'Z'])
    total = sum(compteur.values())


    frequence = {char: count / total * 100 for char, count in compteur.items()}

    frequence_trie = dict(sorted(frequence.items(), key=lambda item: item[1], reverse=True))

    return frequence_trie


frequence_lettres = analyse_frequence(texte_chiffre)





def dechiffrer_texte(texte_chiffre, dictionnaire_substitution_inverse):
    texte_dechiffre = ""
    for char in texte_chiffre.upper():
        if char in dictionnaire_substitution_inverse:
            texte_dechiffre += dictionnaire_substitution_inverse[char]
        else:
            texte_dechiffre += char 
    return texte_dechiffre


dictionnaire_substitution_inverse = {v: k for k, v in dictionnaire_substitution.items()}

texte_dechiffre = dechiffrer_texte(texte_chiffre, dictionnaire_substitution_inverse)



nom = "BERKANI Yacine"
permutation = generer_permutation_depuis_nom(nom)
print("Permutation de l'alphabet:", permutation)




permutation_final = ''.join(permutation)
print("BERKNAI Yacine permutation de l'alphabet avec la règle du tableau 3x9  ",  permutation_final)


print("Texte chiffré:", texte_chiffre)

with open("CSIA_chiffre.txt", "w") as fichier:
    fichier.write(texte_chiffre)

print("Fréquence des lettres:", frequence_lettres)

print("Texte déchiffré:", texte_dechiffre)
with open("CSIA_dechiffre.txt", "w") as fichier:
    fichier.write(texte_dechiffre)