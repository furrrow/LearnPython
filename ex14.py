# example of input/outputs in Python

#taken from 'learnpythonthehardway.org'
#starting from Exercise 14

from sys import argv

script, user_name = argv
prompt = '>'

print("Hi %s, I am the %s script." % (user_name, script))
print("I'd like to ask you  a few questions.")
print("Do you like me %s?" % (user_name))
likes = input(prompt)

print("where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r acomputer. Nice
""" % (likes, lives, computer)
)
# so apparently next line in printing statements do become next line in print_ed statements
