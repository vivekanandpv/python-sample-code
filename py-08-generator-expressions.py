#   generators keep on yielding values lazily
#   generators give the value when invoked with next(gen_expr),
#   raise StopIteration error if there are no more items to return
#   generator expression looks very much like a list comprehension
#   list comprehension is eagerly evaluated, but generator is lazily
#   evaluated (hence memory efficient, but may be slow in some cases)

gen_expr = (n ** 2 for n in range(25) if n % 5 == 0)

print(type(gen_expr))

print(next(gen_expr))
print(next(gen_expr))
print(next(gen_expr))
print(next(gen_expr))
print(next(gen_expr))
# print(next(gen_expr))   # StopIteration is raised as no values are to be returned

print('~'*50)

#   generator expressions are iterables (can be used with for loop)
gen_expr_2 = ((n, n ** 2) for n in range(20) if n % 2 == 0)
for x in gen_expr_2:
    print(x)
