import itertools
import string

# Demander à l'utilisateur les paramètres du mot de passe
longueur = int(input("Longueur du mot de passe : "))
majuscules = input("Inclure des majuscules (oui/non) : ").lower() == "oui"
chiffres = input("Inclure des chiffres (oui/non) : ").lower() == "oui"

# Créer une liste des caractères à inclure dans le mot de passe
caracteres = string.ascii_lowercase
if majuscules:
    caracteres += string.ascii_uppercase
if chiffres:
    caracteres += string.digits

# Générer toutes les combinaisons possibles de mots de passe
combinaisons = itertools.product(caracteres, repeat=longueur)

# Écrire chaque combinaison de mot de passe générée dans un fichier texte
with open("combinaisons_salama.txt", "w") as f:
    for mot_de_passe in combinaisons:
        f.write("".join(mot_de_passe) + "\n")
