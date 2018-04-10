# Some tests with strings interpolations

some_var = 'my string'
some_var2 = 'my other string'
some_var3 = 'my pet'

# 2.7 + 3.6 style interpolation
print('My string was {}'.format(some_var))
print('My string was {}, {}'.format(some_var, some_var2))
print('My string was {1}, {0}'.format(some_var, some_var2))
print('My string was {pet}, {string}'.format(pet=some_var3, string=some_var2))

my_num = 100 / 13

print('My string was {num:1.6f}'.format(num=my_num))
print('My string was {num:9.4f}'.format(num=my_num))

name = "Test"

# 3.6 only interpolation
print(f'Hello {name}')
