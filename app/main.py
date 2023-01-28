import math
from typing import Tuple
from KeyDict import KEYBOARD
import pandas as pd


def find_distance(first: str, second: str) -> float:
    a: Tuple[float, float] = KEYBOARD[first]
    b: Tuple(float, float) = KEYBOARD[second]

    return math.dist(a, b)


def check_word(word) -> float:
    return sum(find_distance(letter, word[i + 1]) for i, letter in enumerate(word[:-1]))


def main():
    # read in wordlist
    filename: str = "app/static/wordlist.txt"
    wordlist: list[str] = open(filename, "r").read().split("\n")

    # Remove short and long words (), and capitalize
    wordlist = [
        word.upper() for word in wordlist if len(word) > 2 and len(word) < 8
    ]
    words = {"Word": [], "Length": [], "Distance": []}
    for word in wordlist:
        words["Word"].append(word)
        words["Length"].append(len(word))
        words["Distance"].append(check_word(word))

    pd.DataFrame.from_dict(words).to_csv("out.csv")


if __name__ == "__main__":
    main()
