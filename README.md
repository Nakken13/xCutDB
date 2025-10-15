# xCutDB

xCutDB est un utilitaire simple en Python qui permet de découper un grand fichier texte (par exemple une grosse base de données exportée au format texte) en plusieurs fichiers plus petits. Le découpage se fait par nombre de lignes et produit des fichiers `.txt` dans un dossier de sortie.

## Caractéristiques

- Interface graphique (Tkinter + ttkbootstrap) pour une utilisation conviviale.
- Découpage par nombre de lignes (paramétrable).
- Encodage UTF-8 par défaut.
- Les fichiers de sortie sont nommés `ORIGINE_partNNN.txt` et placés dans un dossier `ORIGINE_parts`.

## Dépendances

- Python 3.8 ou supérieur
- ttkbootstrap (interface moderne pour Tkinter)

Remarque : `tkinter` est inclus avec la plupart des distributions Python sous Windows ; il n'est généralement pas installé via `pip`.

## Installation (Windows - cmd.exe)

1. Ouvrez un terminal `cmd.exe` et positionnez-vous dans le dossier du projet.
2. (Optionnel) Créez et activez un environnement virtuel :

	python -m venv .venv
	.venv\Scripts\activate

3. Installez les dépendances listées :

	pip install -r requirements.txt

## Utilisation

Le script principal est `xCutDB.py`. Lancez-le simplement :

```cmd
python xCutDB.py
```

La fenêtre permet de :

- Choisir un fichier texte (`.txt`) à découper.
- Spécifier le nombre de lignes par fichier (valeur par défaut dans l'interface : 100000).
- Lancer le découpage. Une barre de progression indique l'avancement.

Après exécution, un dossier nommé `<nomfichier>_parts` sera créé à côté du fichier d'origine et contiendra les fichiers découpés nommés `<nomfichier>_part000.txt`, `<nomfichier>_part001.txt`, etc.

## Exemple

Si vous avez `grosse_base.txt` et que vous entrez `100000` lignes par fichier, l'application va créer un dossier `grosse_base_parts/` contenant des fichiers `grosse_base_part000.txt`, `grosse_base_part001.txt`...

## Scripts auxiliaires

- `start.bat` : lance `xCutDB.py` (double-cliquer ou exécuter depuis `cmd`).
- `setup.bat` : installe les dépendances (corrigé pour installer `ttkbootstrap`).

## Dépannage

- Si l'interface ne démarre pas, vérifiez que Python est installé et que la version est compatible (3.8+).
- Si une erreur liée à `ttkbootstrap` apparaît, installez-le manuellement :

  pip install ttkbootstrap

- Si vous avez un problème d'encodage (caractères spéciaux), assurez-vous que vos fichiers source sont en UTF-8.

## Contribution

Contributions bienvenues : ouvrez une issue pour discuter d'une fonctionnalité ou d'un bug, puis soumettez une PR.

## Licence

Ajoutez ici la licence que vous souhaitez (par exemple MIT). Si aucune licence n'est fournie, le dépôt n'est pas explicitement ouvert.

## Contact

Pour toute question, consultez les informations du dépôt ou ouvrez une issue.

---

Souhaitez-vous que j'ajoute :

- une version en ligne de commande (CLI) pour découper sans interface ?
- des tests unitaires basiques (+ un `pytest` simple) ?
- un `start.bat` amélioré qui accepte des arguments ?

