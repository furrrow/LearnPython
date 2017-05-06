# example of input/outputs in Python

#taken from 'learnpythonthehardway.org'
#starting from Exercise 13

from sys import argv

script, first, second, third = argv

#NOTE: proper way to call this script:
#python ex13.py first second third

print(
    "The script is called:", script,
    "\nYour first variable is:", first,
    "\nYour second variable is:", second,
    "\nYour third variable is:", third
    )
