from itertools import product

# Define the characters
characters = 'abcdefghijkl'
'''
A = U
B = D
C = R
D = L
E = F
F = B
G = U'
H = D'
I = R'
J = L'
K = F'
L = B'

'''

# Generate combinations of lengths 1 to 11
for length in range(1, 12):
    # Use product to generate all combinations with repetition
    combinations = product(characters, repeat=length)

    # Create a file to write the combinations
    filename = f'combinations_length_{length}.txt'
    with open(filename, 'w') as file:
        # Write each combination to the file
        for combo in combinations:
            file.write(''.join(combo) + '\n')

    print(f'Combinations of length {length} written to {filename}')
