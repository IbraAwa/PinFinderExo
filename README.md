# OPERATION EL JEFE : Mission 1 - Le coffre

*Confidentiel. Destruction après lecture.*

Agent,

Votre cellule vous a contacté personnellement. Vous êtes les meilleurs, et c'est pour ça qu'on fait appel à vous.

La mission El Jefe vise le cartel de Sinaloa et son chef. Dans cette mission, une sous-mission concerne un coffre numérique, `coffre.zip`, saisi lors d'une perquisition. Il est verrouillé par un code PIN à 4 chiffres, et personne n'a réussi à l'ouvrir. Le coffre est impossible à ouvrir à la main : c'est pour ça qu'on compte sur vous.

**Votre mission**

1. Écrivez un programme Python qui teste tous les codes possibles, de `0000` à `9999`.
2. Pour chaque code, essayez d'ouvrir le coffre. Une mauvaise combinaison ne doit pas faire planter le programme.
3. Dès que le bon code est trouvé, arrêtez la recherche et récupérez le contenu du coffre.

**Consignes techniques**

- Complétez la fonction `trouver_pin` dans `main.py`.
- La fonction `tester_pin` est déjà écrite : elle renvoie le contenu si le code est bon, sinon `None`. Appelez-la, ne la modifiez pas.
- `trouver_pin` doit renvoyer `(pin, contenu)` dès qu'il trouve le bon code, ou `None` s'il n'en trouve aucun.
- Lancez le programme depuis le dossier qui contient `coffre.zip` : `python main.py`.

**Ce que vous obtiendrez**

Le coffre contient deux choses :
- **L'adresse de l'intranet du cartel**, leur réseau interne. C'est la porte d'entrée vers l'étape 2 : une fois sur place, vous devrez trouver un moyen de vous identifier comme membre du cartel.
- **Le flag de l'étape 1**. Soumettez-le sur la plateforme pour valider la mission et débloquer l'accès à l'intranet.

Dans le réseau du cartel se trouvent le compte du chef, *El Jefe*, et un dossier classifié, « Opération finale ». Ce dossier contient ce que le cartel prépare. Vous ne l'atteindrez qu'en avançant étape après étape.

Le premier agent à atteindre ce dossier prendra la main sur toute la mission. Ne perdez pas de temps.

*Fin du message.*

---

## Vous codez plutôt en Java ?

`PinFinder.java` propose la même mission, mais en Java. L'ouverture du coffre chiffré est déjà gérée (Java ne sait pas lire un zip protégé par mot de passe nativement comme Python, donc le fichier embarque la librairie [zip4j](https://github.com/srikanth-lingala/zip4j) dans `lib/`) : il ne vous reste que l'algorithme à écrire dans `trouverPin`, les quatre boucles imbriquées.

**Compiler et lancer**, depuis ce dossier :

```bash
# Linux / Mac
javac -cp lib/zip4j-2.11.6.jar PinFinder.java
java  -cp "lib/zip4j-2.11.6.jar:." PinFinder

# Windows (cmd / PowerShell)
javac -cp lib\zip4j-2.11.6.jar PinFinder.java
java  -cp "lib\zip4j-2.11.6.jar;." PinFinder
```

Une fois votre algorithme Java qui fonctionne, vous pouvez demander à une IA de le traduire en Python (uniquement les boucles, pas la partie zip) pour compléter `trouver_pin` dans `main.py` : c'est ce fichier qui sert pour la soumission officielle de la mission.
