# Mario

![end of first level](https://cs50.harvard.edu/x/2024/psets/1/mario/less/pyramid.png)

# Le problème à résoudre

Dans le jeu vidéo "Super Mario Bros." sorti en 1985, la fin du premier niveau consiste à monter une 
demi-pyramide de briques.

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

> [!TIP]
> Pour transformer un `str`en `int`, il suffit d'utiliser la fonction `int()`

Si l'utilisateur ne rentre pas un `int` strictement supérieur à 0, il faut redemander sans afficher de message d'erreur, comme dans l'exemple ci-dessous.

```bash
$ python mario.py
Height: -3
Height: 3
       #
      ##
     ###
```

> [!TIP]
> Pour vérifier qu'une chaîne de caractères (`str`) contient uniquement des chiffres, vous avez la fonction `isdigit()` ([Doc str](https://docs.python.org/fr/3/library/stdtypes.html#str.isdigit))

# Les tests

N'oubliez pas qu'il est important de tester son programme.
En effet, lorsque vous décidez de tester un programme cela vous amène à vous poser des questions
sur ce que fait votre programme et les cas particuliers.

Que se passe-t-il si l'utilisateur tape :
* un nombre négatif ?
* 0 ?
* un nombre positif
* des lettres ou des mots ?
* rien du tout ?

Nous avons tendance à faire confiance à la logique des utilisateurs mais, 
lorsque nous concevons un logiciel, nous devons imaginer des réponses qui 
ne correspondent à aucune logique.

> "La logique est le dernier refuge des gens sans imagination.” Oscar Wilde

# Le rendu via git
A tout moment, vous pouvez soumettre votre travail sur github visa un `push`.

```bash
git add hello.py
git commit -m "My answer"
git push
```

Des tests automatiques seront lancés dont vous pourrez voir les résultats sur github.

# La vidéo d'explication

Nous vous encourageons à essayer de résoudre le problème par vous même.
Si vous êtes bloqué et/ou que votre cerveau surchauffe, vous pouvez regarder la vidéo suivante.
Attention, il faut se connecter avec votre sésame.

Lien video à ajouter
