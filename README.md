# Mario

![end of first level](https://cs50.harvard.edu/x/2024/psets/1/mario/less/pyramid.png)

# What to Do

In the “Super Mario Bros.” video game, released in 1985, towards the end of the first level Mario must ascend right-aligned pyramid of bricks.
In a file named `mario.py`, you need to write a program that recreates this pyramid using `#` as bricks, as in the below.

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

First prompt the user for an `int` for the pyramid’s actual height, so that the program can also output shorter pyramids like the below:

```bash
$ python mario.py
Height: 5
    #
   ##
  ###
 ####
#####
```

> [!TIP]
> To transform `str` into `int`, simply use `int()`.


Re-prompt the user, again and again as needed, if their input is not greater than 0 or not an int altogether.

```bash
$ python mario.py
Height: 0
Height: 3
  #
 ##
###
```

> [!TIP]
> To check that a string (`str`) contains only digits, you may use `isdigit()`. ([Doc str](https://docs.python.org/fr/3/library/stdtypes.html#str.isdigit))

# When to Do it

By Sunday, january 12, 2025 at 11:59 PM

# How to Test

- Test your script with command `./check [-v] mario.py`
- `-v` option gives the difference between what is expected and what your script prints

Don't forget it's important to test your program.
In fact, when you decide to test a program, you'll have to ask yourself questions about what your program does and what the special cases are.

What happens if the user input is :
* a negative number?
* 0 ?
* a positive number
* letters or words?
* nothing at all?

We tend to trust users' logic, but, when we write code, we have to imagine answers that don't follow any logic.

> "When you have eliminated the impossible, whatever remains, however improbable, must be the truth."
> Sherlock Holmes

# How to Submit

Once you're done with all tasks, submit your python files on Moodle
