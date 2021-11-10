# list iteration
for scientist in ['Raman', 'Rutherford', 'Bohr', 'Heisenberg']:
    print(f'List: {scientist}')

print('~'*50)  # ~ will be repeated 50 times

# tuple iteration
for scientist in ('Raman', 'Rutherford', 'Bohr', 'Heisenberg'):
    print(f'Tuple: {scientist}')

print('~'*50)

# set iteration
for scientist in {'Raman', 'Rutherford', 'Bohr', 'Heisenberg'}:
    print(f'Set: {scientist}')

print('~'*50)

# dictionary iteration
inventors = {
    'C': 'Dennis Ritchie',
    'C++': 'Bjarne Stroustrup',
    'Java': 'James Gosling',
    'Python': 'Guido van Rossum'
}

for lang, inventor in inventors.items():
    print(f'Dictionary: {lang} -> {inventor}')
