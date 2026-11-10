# ============================================================
# MISSION 1 : le coffre
#
# Fichier à ouvrir : coffre.zip (il doit être dans le MÊME dossier que ce main.py)
#
# Pour lancer le programme, ouvre un terminal dans ce dossier et tape :
#     python main.py
# (sous Windows, si ça ne marche pas : py main.py)
#
# À faire : écrire l'algorithme dans trouver_pin.
# Ne modifie pas tester_pin : elle vérifie seulement un PIN à la fois.
# ============================================================
import zipfile
import zlib


def tester_pin(archive, fichier, pin):
    """Renvoie le contenu du fichier si le PIN est bon, sinon None."""
    try:
        return archive.read(fichier, pwd=pin)
    except (RuntimeError, zipfile.BadZipFile, zlib.error):
        return None


def trouver_pin(chemin_zip):
    """A toi de jouer : teste les PIN de 0000 a 9999.
    Renvoie (pin, contenu) des que tester_pin reussit, ou None si aucun PIN ne marche."""
    # TODO
    return None


if __name__ == "__main__":
    resultat = trouver_pin("coffre.zip")
    if resultat is None:
        print("Aucun PIN trouve.")
    else:
        pin, contenu = resultat
        print("PIN trouve :", pin)
        print(contenu.decode())