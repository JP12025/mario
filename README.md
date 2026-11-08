# Mario

![end of first level](https://cs50.harvard.edu/x/2024/psets/1/mario/less/pyramid.png)

# What to Do

Towards the end of the first level of “Super Mario Bros.” released in 1985, Mario must ascend a right-aligned pyramid of bricks.
In a file named `mario.py`, implement a program that recreates this pyramid using `#` as bricks, as in the below.

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

First, prompt the user for an `int` for the pyramid’s actual height, so that the program can also output shorter pyramids like the below:

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
> To transform `str` into `int`, simply use `int()` ([Python ref](https://docs.python.org/3/library/functions.html#int)).

Re-prompt the user, again and again as needed, if their input is not greater than 0 or not an int altogether.
Don't use `try/except` structure, it's not needed here. A `while` loop is ok.

```bash
$ python mario.py
Height: 0
Height: 3
  #
 ##
###
```

> [!TIP]
> To check that a string (`str`) contains only digits, you may use `isdigit()`. ([Python ref](https://docs.python.org/3/library/stdtypes.html#str.isdigit))

# How to Test

Test your program from the exercise folder with:

```bash
python test_mario.py
```

(use `python3` instead of `python` if that is how you run Python on your computer).

The script runs your program as a user would: it types some answers to the `Height: ` question, then checks what your program prints.
When a test fails, it explains what is wrong; spaces are shown as `·` so you can count them.

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

Once you're done with all tasks, submit all your python files on Moodle

# Licence

This course is freely inspired from [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/x/2025/) Harvard. It is licensed under a [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.
