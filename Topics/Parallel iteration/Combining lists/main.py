# please do not modify the following code
numbers, word = input().split()
numbers = list(numbers)

# your code here
zipped = zip(numbers, word)
print(list(zipped))
