import random

LENGTH = 15
COUNT = 1_000_000
INPUT = 'input.txt'
OUTPUT = 'reference.txt'

existing = set()
answers = []


def generate_str(length):
    number = random.randint(0, 26 ** length)
    ret = ''
    while number > 0:
        ret += chr(ord('a') + number % 26)
        number //= 26
    return ret


def generate_query():
    op_type = random.randint(1, 3)
    subtype = random.randint(1, 2)

    candidate = generate_str(LENGTH)
    existing_candidate = None if len(existing) == 0 else random.choice(list(existing))

    actual_candidate = candidate if (subtype == 1 or existing_candidate is None) else existing_candidate

    if op_type == 1:
        existing.add(actual_candidate)
        return f'+ {actual_candidate}'
    elif op_type == 2:
        if actual_candidate in existing:
            existing.remove(actual_candidate)
        return f'- {actual_candidate}'
    else:
        answers.append(('yes' if actual_candidate in existing else 'no') + '\n')
        return f'? {actual_candidate}'


def generate_input(lines_count):
    with open(INPUT, 'w') as f:
        for i in range(lines_count):
            f.write(generate_query() + '\n')
    with open(OUTPUT, 'w') as f:
        f.writelines(answers)


if __name__ == '__main__':
    generate_input(COUNT)
