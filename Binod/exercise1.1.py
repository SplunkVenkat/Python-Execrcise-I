#!/usr/bin/python
import re
print('Enter string to be checked:')
x = raw_input()
temp='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' # punctuation marks
y = re.compile('[%s]' % re.escape(temp))
print('String is '+y.sub('',x))