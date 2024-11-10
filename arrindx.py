from array import *
arr = array('i', [1, 2, 3, 4, 5])

# Print index of element 1
print(arr.index(1))

# Print the first element
print(arr[0])

# Store and print the length of arr
length = len(arr)
print("length of arr:", length)

# Insert 60 at index 1
arr.insert(1, 60)
print(arr)

# Store and print the new length of arr
new_length = len(arr)
print("length of arr:", new_length)
