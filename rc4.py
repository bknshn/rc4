import os
import numpy as np
import matplotlib.pyplot as plt

COLOR_TABLE = ['b', 'g', 'r', 'c', 'm', 'y']

# key-scheduling algorithm
# initialize the permutation in the array S of 256 bits
def init_S(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

# pseudo-random generation algorithm
# output a number of 1 byte in each iteration
def random_generator(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

# encode or decode
def rc4(data, key):
    S = init_S(key)
    gen = random_generator(S)
    result = bytearray([c ^ n for c, n in zip(data, gen)])
    return result

def count_random_numbers(random_key_times, key_length, gen_times):
    # count[nth byte of gen][number (0 - 255)]
    count = np.zeros((gen_times, 256))
    for _ in range(random_key_times):
        key = os.urandom(key_length)
        S = init_S(key)
        gen = random_generator(S)

        for i in range(gen_times):
            count[i][gen.__next__()] += 1
    for i in range(gen_times):
        plt.plot(count[i], COLOR_TABLE[i])
    plt.show()
    return count

def test():
    message = bytearray('hello, world', 'utf-8')
    key = bytes('hoge', 'utf-8')
    encoded = rc4(message, key)
    print('message: ', message)
    print('encoded: ', encoded)
    print('decoded: ', rc4(encoded, key))

if __name__ == '__main__':
    print(count_random_numbers(100000, 5, 5))
