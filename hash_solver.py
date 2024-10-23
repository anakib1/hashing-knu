import time

PRIME = 37
MOD = 1_000_000_000 + 9


def hash_string(s):
    ret = 0
    pwr = 1
    for i in range(len(s)):
        ret += ord(s[i]) * pwr
        ret %= MOD

        pwr *= PRIME
        pwr %= MOD
    return ret


if __name__ == '__main__':
    hash_set = set()

    start = time.time()
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as w:
            for line in f.readlines():
                operation, operand = line.split()
                operand_hash = hash_string(operand)
                if operation == '+':
                    hash_set.add(operand_hash)
                elif operation == '-':
                    if operand_hash in hash_set:
                        hash_set.remove(operand_hash)
                else:
                    w.write(('yes' if operand_hash in hash_set else 'no') + '\n')
    end = time.time()

    print('Elapsed {:.03f} seconds'.format(end - start))
