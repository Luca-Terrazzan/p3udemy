# shorthands to work with lists
word = 'word'

# build an array of letters from the word
letters = [letter for letter in word]
print(letters)

nums = [num ** 2 for num in range(1, 100, 3)]
print(nums)
nums = [num for num in range(1, 100, 3) if num % 2 == 0]
print(nums)
