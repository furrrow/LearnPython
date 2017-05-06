"""
Names, Variables, Code, Functions

taken from 'learnpythonthehardway.org'
starting from Exercise 18


"""
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print ("I got nolthin'.")

print_two("alpha", "beta")
print_two_again("allison", "ben")
print_one("alpha")
print_none()
