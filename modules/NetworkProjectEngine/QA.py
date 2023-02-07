import random

def generate_question() -> str:
    pass
    rand1 = random.randint(1, 26)
    ALPHABETS = [chr(val) for val in range(65, 91)]
    encrypted_message = "".join(random.choices(ALPHABETS, 50))

    rand1 = random.randint(1, 1000)
    rand2 = random.randint(1, 1000)
    operator = random.choice(('+', '-', '*', '/'))

    question = str(rand1) + " " + encrypted_message
    return question


def solve_question(question: str) -> str:
    pass
    parsed = question.split()
    rand1 = int(parsed[0])
    encrypted_message = parsed[1]
    alpha_offset = (rand1) % 26
    # print("{} {} alpha offset: {}".format(self.rand1, self.rand2, alpha_offset))
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(((ord(char) - 65 + alpha_offset) % 26) + 65)
    return decrypted_message
