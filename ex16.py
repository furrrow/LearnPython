"""
example of input/outputs in Python

taken from 'learnpythonthehardway.org'
starting from Exercise 16
more READ FILE exercises

NOTE: type (some file) is a quick way to let powershell print something

"""
from sys import argv
script, filename = argv
print(
    "We are going to erase %r." % filename,
    "If you don't wnat that, hit CTRL_C(^C).",
    "If you do want that, hit RETURN"
)

input("?")
print("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print("How I am going to ask you for three lines.")

line1 =  input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")
print ("i am goin to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
