"""Acceptance tests for the Mario exercise.

Each test runs your program as a whole, exactly as a user would: it types
some answers to the "Height: " question, then checks what your program
prints and tries to explain what is wrong.

Run the tests from the exercise folder with:

    python test_mario.py
"""

import os
import subprocess
import sys
from pathlib import Path

EXERCISE_DIR = Path(__file__).resolve().parent
SCRIPT = "mario.py"
PROMPT = "Height: "
TIMEOUT = 5  # seconds

# Each test case: (what is checked, answers typed by the user).
# Convention: only the LAST answer is a valid height, all the others
# must be rejected by the program (which then asks again).
CASES = [
    ("height 8 (example of the instructions)", ["8"]),
    ("height 5", ["5"]),
    ("height 1 (smallest pyramid)", ["1"]),
    ("height 10 (more than 8 rows)", ["10"]),
    ("0 is rejected", ["0", "3"]),
    ("a word and a negative number are rejected", ["trois", "-2", "4"]),
    ("an empty answer is rejected", ["", "2"]),
    ("a decimal number is rejected", ["2.5", "3"]),
]


# ---------------------------------------------------------------------------
# Running the student's program
# ---------------------------------------------------------------------------

def run_program(answers):
    """Run the program, typing the answers one per line.

    Return (stdout, stderr, return code), or None if the program
    did not stop in time.
    """
    try:
        # sys.executable is the Python running the tests,
        # so "python" vs "python3" does not matter.
        result = subprocess.run(
            [sys.executable, SCRIPT],
            input="\n".join(answers) + "\n",
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=EXERCISE_DIR,
            env=dict(os.environ, PYTHONIOENCODING="utf-8"),
            timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return None
    stdout = result.stdout.replace("\r\n", "\n")
    return stdout, result.stderr.strip(), result.returncode


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def show(lines):
    """Indent lines and make spaces visible (shown as '·')."""
    if not lines:
        return "    (nothing)"
    return "\n".join("    " + line.replace(" ", "·") for line in lines)


def plural(number, word):
    """Return e.g. '1 space' or '3 spaces'."""
    return f"{number} {word}" if number == 1 else f"{number} {word}s"


def last_lines(text, nb_lines=4):
    """Return the last lines of a text, indented."""
    lines = text.split("\n")[-nb_lines:]
    return "\n".join("    " + line for line in lines)


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def expected_pyramid(height):
    """Return the rows of the expected pyramid."""
    return [" " * (height - row) + "#" * row for row in range(1, height + 1)]


def count_prompts(stdout):
    """Count the "Height: " questions at the start of the output.

    Return (number of questions, rest of the output).
    """
    nb_prompts = 0
    while stdout.startswith(PROMPT):
        stdout = stdout[len(PROMPT):]
        nb_prompts += 1
    return nb_prompts, stdout


def check_questions(stdout, stderr, return_code, answers):
    """Check that the program asks the question the right number of times.

    Return (error message or None, rest of the output after the questions).
    """
    nb_prompts, rest = count_prompts(stdout)
    printed = "Your program printed:\n" + show(stdout.splitlines())

    if stdout.startswith((PROMPT + "\n", PROMPT.strip() + "\n")):
        return (f"The answer must be typed on the same line as the question: "
                f"use input({PROMPT!r}) instead of print().\n{printed}"), rest
    if nb_prompts == 0:
        if stdout.startswith(PROMPT.strip()):
            message = (f"The question must be exactly {PROMPT!r}, "
                       f"with a space after the colon.")
        else:
            message = f"Your program should start by asking {PROMPT!r}."
        return f"{message}\n{printed}", rest

    if "EOFError" in stderr:
        return (f"Your program asked again after {answers[-1]!r}, "
                f"but {answers[-1]} is a valid height."), rest
    if return_code != 0:
        answer = answers[min(nb_prompts, len(answers)) - 1]
        message = (f"Your program crashed after reading {answer!r}:\n"
                   f"{last_lines(stderr)}")
        if "ValueError" in stderr:
            message += ("\nint() fails when the text is not a whole number: "
                        "check the text first (e.g. with str.isdigit()) "
                        "before converting it.")
        return message, rest

    if PROMPT in rest:
        extra = rest[:rest.index(PROMPT)]
        return (f"Your program printed {extra!r} before asking again. "
                f"When an answer is invalid, it should only ask again.\n"
                f"{printed}"), rest
    if nb_prompts < len(answers):
        accepted = answers[nb_prompts - 1]
        return (f"Your program accepted {accepted!r} as a height, but it "
                f"should ask again: a height must be a whole number "
                f"greater than 0.\n{printed}"), rest
    return None, rest


def describe_row_error(number, row, height):
    """Explain what is wrong in one row of the pyramid."""
    nb_hashes = row.count("#")
    nb_spaces = height - number
    nb_leading = len(row) - len(row.lstrip(" "))
    others = set(row) - {" ", "#"}

    if others:
        return (f"Row {number} contains characters other than spaces "
                f"and '#': {sorted(others)}.")
    if nb_hashes != number:
        message = (f"Row {number} should contain {number} '#' "
                   f"but contains {nb_hashes}.")
        if abs(nb_hashes - number) == 1:
            message += (" Off by one: check the bounds of your range() "
                        "(range(a, b) starts at a and stops before b).")
        return message
    if nb_leading != nb_spaces:
        return (f"Row {number} should start with {plural(nb_spaces, 'space')}"
                f" but starts with {plural(nb_leading, 'space')}.")
    if row != row.rstrip():
        return (f"Row {number} ends with spaces: nothing should be printed "
                f"after the last '#'.")
    return f"In row {number}, the '#' should be next to each other."


def check_pyramid(rows, height):
    """Check the rows of the pyramid. Return an error message or None."""
    expected = expected_pyramid(height)
    if rows == expected:
        return None

    if not rows:
        message = "Your program printed no pyramid."
    elif rows == ["#" * row for row in range(1, height + 1)]:
        message = ("Your pyramid is left-aligned: it should be "
                   "right-aligned, with spaces before the '#'.")
    elif rows == expected[::-1]:
        message = (f"Your pyramid is upside down: the first row should have "
                   f"1 '#' and the last row {height}.")
    elif any(" " in row.strip(" ") for row in rows):
        message = ("The '#' of a row should be next to each other, "
                   "with no space between them.")
    elif len(rows) != height:
        message = (f"Your pyramid has {len(rows)} rows, but it should have "
                   f"{height} (the height typed by the user).")
        if abs(len(rows) - height) == 1:
            message += (" Off by one: check the bounds of your range() "
                        "(range(a, b) stops before b).")
    else:
        number = 1
        while rows[number - 1] == expected[number - 1]:
            number += 1
        message = describe_row_error(number, rows[number - 1], height)

    return (f"{message}\n"
            f"Expected pyramid:\n{show(expected)}\n"
            f"Your pyramid:\n{show(rows)}")


def check_case(answers):
    """Run one test case. Return None if it passes, else an error message."""
    result = run_program(answers)
    if result is None:
        return ("Your program did not stop (infinite loop?). Check that "
                "input() is called inside your loop.")
    stdout, stderr, return_code = result

    message, rest = check_questions(stdout, stderr, return_code, answers)
    if message is not None:
        return message

    rows = rest.splitlines()
    expected = expected_pyramid(int(answers[-1]))
    # "Height:" + "       #" looks like "Height: " + "      #"
    if len(rows) > 1 and rows == [expected[0][1:]] + expected[1:]:
        return (f"The question must be exactly {PROMPT!r}, "
                f"with a space after the colon.")
    return check_pyramid(rows, int(answers[-1]))


# ---------------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------------

def main():
    sys.stdout.reconfigure(errors="replace")
    use_colors = sys.stdout.isatty() and (
        os.name != "nt" or "WT_SESSION" in os.environ)
    green = "\033[32m" if use_colors else ""
    red = "\033[31m" if use_colors else ""
    reset = "\033[0m" if use_colors else ""

    if not (EXERCISE_DIR / SCRIPT).is_file():
        print(f"No {SCRIPT} found in {EXERCISE_DIR}")
        return 1

    nb_ok = 0
    for description, answers in CASES:
        typed = ", ".join(repr(answer) for answer in answers)
        message = check_case(answers)
        if message is None:
            nb_ok += 1
            print(f"{green}\u2714{reset} {description}")
        else:
            print(f"{red}\u2717{reset} {description}")
            print(f"    Answers typed: {typed}")
            print("    " + message.replace("\n", "\n    ") + "\n")

    color = green if nb_ok == len(CASES) else red
    print(f"Validated: {color}{nb_ok}/{len(CASES)}{reset}")
    return 0 if nb_ok == len(CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
