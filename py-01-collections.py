# list is an ordered collection of elements
#   elements can be of any type
#   subscript access is available
#   duplicates can exist
#   mutation of elements is possible
#   list is not hashable
names = ['Raman', 'Rutherford', 'Bohr', 'Heisenberg']

# set is a unique collection of hashable elements
#   elements can be of any type, but they must be hashable
#   duplicates are not allowed
#   index-based or subscript-based access is not allowed as there is no order
#   mutation of elements is possible
#   set-specific operators are available
#   set itself is not hashable
branches = {'electrical', 'mechanical', 'civil'}

# tuple is an immutable, ordered collection of elements
#   elements can be of any type
#   subscript access is available
#   duplicates can exist
#   mutation of elements(reassignment/rebinding) is not possible
#   tuple is hashable
scores = (9.2, 8.7, 8.9, 8.7, 8.8, 9.3, 9.0)

# dictionary is a collection of key-value pairs
#   keys must be unique and hashable
#   values can be duplicates
#   keys may not follow any order
#   subscript access with key is available
subjects = {
    'EE0256': 'Network analysis',
    'EE0431': 'Microprocessors and interfacing',
    'EE0653': 'VLSI'
}
