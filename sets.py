# Sets

my_set = set()
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)

# No errors, but it does nothing
my_set.add(1)
print(my_set)

redundant_list = [1, 1, 1, 1, 2, 2, 2, 5, 1, 4, 4, 2]
another_set = set(redundant_list)
print(another_set)
