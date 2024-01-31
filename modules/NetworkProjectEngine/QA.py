import random


def generate_question() -> str:
    import random
    rand1 = random.randint(1, 1000)
    rand2 = random.randint(1, 1000)
    operator = random.choice(('+', '-', '*', '/'))

    question = str(rand1) + " " + operator + " " + str(rand2)
    return question


def solve_question(question: str) -> str:
    interp = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)
    }
    if not question:
        print("no question provided")
        return ""
    parsed = question.split()
    ans = str(interp[parsed[1]](int(parsed[0]), int(parsed[2])))
    return ans


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        user_question = ' '.join(sys.argv[1:])
        print(solve_question(user_question))
    else:
        sample_question = generate_question()
        print(sample_question)
