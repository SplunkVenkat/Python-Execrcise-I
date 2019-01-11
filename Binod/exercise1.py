#!/usr/bin/python
import string
print('Enter string to be checked:')
x = raw_input()
y = x.translate(string.maketrans("",""), string.punctuation)
print('String is '+y)
