#   building a list of squares of numbers between 0 and 12
squares = [n ** 2 for n in range(0, 13)]
print(squares)

#   building a list of tuples of number and its square (0-12)
squares_tuple = [(n, n**2) for n in range(0, 13)]
print(squares_tuple)

#   building a list of odd numbers between 0-200 that are divisible by 3
nums_divisible_by_3 = [n for n in range(0, 200) if n % 2 != 0 and n % 3 == 0]
print(nums_divisible_by_3)
