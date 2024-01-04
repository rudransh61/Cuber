from itertools import product

# Define the characters
characters = '1234'
'''
1 = U
2 = D
3 = R
4 = L

'''

# Generate combinations of lengths 1 to 11
for length in range(1, 8):
    # Use product to generate all combinations with repetition
    combinations = product(characters, repeat=length)

    # Create a file to write the combinations
    filename = f'combinations_length_{length}.txt'
    with open(filename, 'w') as file:
        # Write each combination to the file
        for combo in combinations:
            file.write(''.join(combo) + '\n')

    print(f'Combinations of length {length} written to {filename}')
