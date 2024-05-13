import random


def primes(n):
    primes_list = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes_list.append(num)
    return primes_list


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_coprime(num, primes):
    for prime in primes:
        if gcd(num, prime) == 1:
            return prime
    return None


def find_d(fi, exp, primes):
    for el in primes:
        if (el * exp) % fi == 1:
            return el


def get_keys():
    d = None
    exp = 0
    mod = 0
    while d is None:
        print()
        print("################################")
        print()
        n = 10000
        primes_arr = primes(n)

        p = primes_arr[random.randint(0, len(primes_arr) - 1)]
        q = primes_arr[random.randint(0, len(primes_arr) - 1)]

        while p == q:
            q = primes_arr[random.randint(0, len(primes_arr) - 1)]

        print(f"p: {p}, q: {q}")

        mod = p * q

        print(f"mod = {mod}")

        fi = (p - 1) * (q - 1)

        print(f"fi = {fi}")

        exp = 0

        ferm_numbers = [3, 5, 17, 65537]

        for i in ferm_numbers:
            if i < mod and find_coprime(i, primes_arr):
                exp = i

        print(f"exp = {exp}")

        print("Public key: ")
        print(f"(e, mod) = {exp, mod}")

        d = find_d(fi, exp, primes_arr)

        print(f"d = {d}")

        print("Private key:")
        print(f"(d, mod) = {d, mod}")

    return exp, mod, d


def letter_position(letter):
    english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']
    return ord(letter)


def letter_by_position(position, lang='en'):
    english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']

    return chr(position)


def encode_letter(exp, mod, letter):
    return (letter ** exp) % mod


def decode_letter(d, mod, letter):
    return (letter ** d) % mod


exp, mod, d = get_keys()

word = input("Enter the word: ")
word_arr = []

for i in word:
    word_arr.append(letter_position(i))

print(f"Start word: {word_arr}")

encode_word = []
for el in word_arr:
    encode_word.append(encode_letter(exp, mod, el))

print(f"Encode word: {encode_word}")

decode_word = []

for el in encode_word:
    decode_word.append(decode_letter(d, mod, el))

print(f"Decode word: {decode_word}")

final_word = ""

for el in decode_word:
    final_word += letter_by_position(el)

print(f"Final word: {final_word}")
