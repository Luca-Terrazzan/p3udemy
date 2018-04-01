# List examples

my_list = [1, 2, 3, 'string!']
print(len(my_list))
print(my_list[::2])

# concatenation

my_list2 = ['a', 'b', 'c']
print(my_list + my_list2)

# lists are not immutable!

my_list[0] = 'asdasdas'
print(my_list)

# append() is similar to concatenation, but:
# * it works in place
# * it adds as a single element
my_list.append(my_list2)
print(my_list)

# pop() works in place and returns the item popped
last_item = my_list2.pop()
print(my_list2)
print(last_item)
some_item = my_list.pop(0)
print(some_item)

# sort and reverse
# sort() works in place and return 'None'
# reverse() works in place and return 'None'
ul_chars = ['z', 'h', 'd', 'f', 'a', 'r']
ul_nums = [4, 8, 1, 2, 22]
print(ul_nums)
ul_nums.sort()
print(ul_nums)
ul
