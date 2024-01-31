import random
import string
import numpy as np
import logging


def generate_question() -> str:
    # generate string
    letters = string.ascii_lowercase
    result_str = ' '.join(random.choice(letters) for i in range(50))

    # split string and scamble
    split_str = result_str.split(" ")
    scramble_order = np.arange(len(split_str))
    np.random.shuffle(scramble_order)

    # reorder
    question = ""
    for i in range(len(split_str)):
        question += f"{scramble_order[i]}-{split_str[scramble_order[i]]} "
    return question.strip()


def solve_question(question: str) -> str:
    split_str = question.strip().split(" ")

    # create dictionary
    _dict = {}
    for _str in split_str:
        if "-" in _str:
            index, string = _str.split("-")
            _dict[int(index)] = string

    # unscramble
    unscramble = ""
    for i in range(len(split_str) - 1):
        unscramble += _dict[i]

    return unscramble.strip()

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        user_question = ' '.join(sys.argv[1:])
        print(solve_question(user_question))
    else:
        sample_question = generate_question()
        print(sample_question)
