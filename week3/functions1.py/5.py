from itertools import permutations

def print_permutations():
    word = input()
    permuted_strings = [''.join(p) for p in permutations(word)]
    print()
    for permuted_string in permuted_strings:
        print(permuted_string)
print_permutations()

