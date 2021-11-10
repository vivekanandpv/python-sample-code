inventors = {
    'C': 'Dennis Ritchie',
    'C++': 'Bjarne Stroustrup',
    'Java': 'James Gosling',
    'Python': 'Guido van Rossum'
}

#   key-based accessing
print(inventors['Python'])

#   adding
inventors['JavaScript'] = 'Brandon Eich'
print(inventors['JavaScript'])

#   deleting
del inventors['Java']
# print(inventors['Java'])    # key error, as the key doesn't exist
print(inventors.get('Java'))    # None

#   get all keys (view-only list)
print(inventors.keys())

#   get all values (view-only list)
print(inventors.values())

#   check key membership
print('Python' in inventors)

#   remove last item and get it as a tuple
inv_tuple = inventors.popitem()
print(inv_tuple)
print(inventors)

#   update existing dictionary with another
inventors.update({'JavaScript': 'Brandon Eich', 'Fortran': 'John Backus'})
print(inventors)

#   normal iteration is over keys
for key in inventors:
    print(f'{key} is created by {inventors[key]}')

#   k-v pair iteration over items
for lang, creator in inventors.items():
    print(f'{lang} is created by {creator}')
