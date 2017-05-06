# this file is composed of printing examples,
# taken from 'Learning Python the Hard way'
print ()
print ("#========== section 4 ==========#")
print ()
formatter = "%r %r %r %r"

# "%r" should be used for debugging purposes only.
# it will give you the raw programmer's version of variable, or "representation"

print (formatter % (1,2,3,4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
#careful not to forget the commas here
print (formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight",
))

print ()
print ("#========== section 5 ==========#")
print ()
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days: ", days)
print ("Here are the months: ", months)
print ("""
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
    """)

print ()
print ("#========== section 6 ==========#")
print ()

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
# double slash becomes one slash printed
# remember backslash does special things!
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

'''
print ()
print ("#========== and just for fun ==========#")
print ()

while True:
    for i in ["/","-","|","\\","|"]:
        print ("%s\r" % i),
'''
