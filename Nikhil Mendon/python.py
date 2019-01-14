string = input("Enter a string: ")   # Accept the string entered by the user
words = string.split()               # Split the string using split function
words.sort()                         # Sort the words in ascending order
for output in words:
   print(output)                     # Display the words in ascending order
