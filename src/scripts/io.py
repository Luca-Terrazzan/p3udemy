# basic I/O

# open file
my_file = open('test.txt')
# missing file => ERRNO 2
# my_file = open('fake_test.txt')

print(my_file.read())
# if I read it again, the cursor is at the end! basic iterator
print(my_file.read())

# reset the cursor
my_file.seek(0)
print(my_file.read())

# Get a list of lines, split on \n
my_file.seek(0)
print(my_file.readlines())

# close the io...
my_file.close()
# ...or use 'with' clause
with open('test.txt') as txtfile:
    print(txtfile.read())

# modes
# r - read
# w - write
# a - append only
# r+ - read and write
# w+ - write and read
with open('test.txt', mode = 'a') as txtfile:
    txtfile.write('\nanother line!')

with open('newfile.txt', mode = 'w') as new:
    new.write('new file!')
