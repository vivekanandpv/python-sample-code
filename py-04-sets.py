#   only hashable values are allowed
#   to check execute hash(val)

#   strings, ints, floats, tuples are hashable
#   list, set are not
colours = {'blue', 'red'}

#   adding an element
colours.add('black')

#   duplicates are ignored
colours.add('red')

#   remove an element
colours.remove('blue')     # KeyError if element doesn't exist
colours.discard('brown')    # No action taken if the value doesn't exist

#   superset/subset/etc
print(colours.issuperset({'red'}))  # is colours superset of {'red'}?
# is colours subset of ...?
print(colours.issubset({'red', 'brown', 'purple', 'black'}))
print(colours.isdisjoint({'azure'}))  # no common elements?

#   https://en.wikipedia.org/wiki/Set_(mathematics)#Basic_operations
#   union
set_a = {1, 3, 5}
set_b = {2, 4, 6}

union_set = set_a.union(set_b)
print(union_set)

#   intersection
set_c = {2, 4, 6, 8}
set_d = {4, 6, 8, 10, 23}

intersection_set = set_c.intersection(set_d)
print(intersection_set)

#   difference
difference_set = set_c.difference(set_d)
print(difference_set)

#   symmetric difference (only unique elements from both sets)
symmetric_difference_set = set_c.symmetric_difference(set_d)
print(symmetric_difference_set)
