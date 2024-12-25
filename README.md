# Mario

Dans le jeu vidéo "Super Mario Bros." sorti en 1985, la fin du premier niveau consiste à monter une 
demi-pyramide de briques.
![end of first level](https://cs50.harvard.edu/x/2024/psets/1/mario/less/pyramid.png)
Dans un fichier nommé `mario.py`, vous devez écrire un programme qui recrée cette pyramide avec le symbole `#` comme dans l'exemple ci-dessous (pyramide de 8).
```bash
$ python mario.py
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```
Comme vous le voyez, le programme commence par demander à l'utilisateur la hauteur (`Height`) 
de la pyramide et attend un `int` en réponse. Une fois que l'utilisateur a répondu, le programme affiche la
pyramide sur la sortie standard.

Si l'utilisateur ne rentre pas un `int` strictement supérieur à 0, il faut redemander sans afficher de message d'erreur, comme dans l'exemple ci-dessous.
```bash
$ python mario.py
Height: trois
Height: -3
Height: 3
       #
      ##
     ###
```
> [!TIP]
> * Pour vérifier qu'une chaîne de caractères (`str`) contient uniquement des chiffres, vous avez la fonction `isdigit()` ([Doc str](https://docs.python.org/fr/3/library/stdtypes.html#textseq))
> * Pour transformer un `str`en `int`, il suffit d'utiliser la fonction `int()`
