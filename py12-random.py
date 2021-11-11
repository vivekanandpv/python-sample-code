#   random values
import random

#   random int so that a <= rand <= b
random_int_value = random.randint(1, 10)

#   equivalents
#   both produce a single value not a range!
val_1 = random.randrange(1, 11, 1)  # start, end, step
val_2 = random.randrange(11)    # end

#   random bytes
byte_value = random.randbytes(16)

#   choose a random value from an iterable
num_list = [12, 3, 4, 5, 31, 90, 97, 65]
choice_value = random.choice(num_list)

#   shuffling a list in place; must support mutation
#   can't do with range(), you must use a list
range_to_be_shuffled = [n for n in range(20, 40)]
random.shuffle(range_to_be_shuffled)
