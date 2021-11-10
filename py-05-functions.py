#   defining a function
def drive(car):
    print(f'driving {car}...')


#   calling a function
drive('BMW X5')

#   returning a value from a function


def square(num):
    return num ** 2


print(square(7))

#   default parameters


def calculate_area_of_circle(r=1):
    return 3.1415926535 * (r ** 2)


print(calculate_area_of_circle())   # default will kick in
print(calculate_area_of_circle(2.8))

# named parameters (can be passed in any order)


def calculate_perimeter(length, breadth):
    return 2*(length + breadth)


print(calculate_perimeter(breadth=23, length=45))

#   *args for variadic functions (any number of arguments)
#   *args must come after the positional parameters if any


def calculate_sum(*args):
    total = 0

    for num in args:
        total += num

    return total


print(calculate_sum(12, 24, 36))

#   global variables and local variables

global_var = 101


def foo():
    local_var_1 = 23
    local_var_2 = 'hi'

    print('local variables', vars())    # only local_var_1 and local_var_2

    # all the variables in the current module
    print('global variables', globals())


foo()

#   lambda expressions or lambda functions
#   short, one-line, anonymous functions that have implicit return
#   x and y are parameters and x*y is implicitly returned
#   lambda_expr = lambda x, y: x*y
#   print(lambda_expr(12,3))    #36
