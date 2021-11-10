#   using sorted built-in function

#   sorting a list
cities = ['Bengaluru', 'Hyderabad', 'Ajmer', 'Chandigarh']

# natural sort, creates a new list, original is intact
sorted_cities = sorted(cities)

print(sorted_cities, cities)

# reverse key for descending order sort
descending_order_sort = sorted(cities, reverse=True)
print(descending_order_sort)

#   sorting a dictionary keys
print(sorted({'k1': 'v1', 'k0': 'v0'}))

#   custom sort (sort the cities in the descending order of lengths)
cities_by_length_desc = sorted(cities, key=lambda c: len(c), reverse=True)
print(cities_by_length_desc)


#   sorting a list in place using list.sort()
#   list.sort() has the same functionality except that it sorts the list in place
scores = [90, 89, 45, 47, 85, 65, 99]
scores.sort(reverse=True)
print(scores)  # scores is sorted (desc) in place; original order is lost!
