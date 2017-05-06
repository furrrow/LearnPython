# this file is composed of printing examples,
# taken from 'Learning Python the Hardway'
print ()
print ("#========== section 1 ==========#")
print ()
my_name = 'icebat'
my_age = 23
my_height = 172 #cm
my_weight = 169 #lb
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print ("Let's talk about %s." % my_name)
print ("He's %d centimeters tall." % my_height)
    #once I forgot the second parantheses in this following line!
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))

print ("His teeth are usually %s depending on the coffee." % my_teeth)

print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

#==============================
print ()
print ("#========== section 2 ==========#")
print ()
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary,do_not)

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print (w+e)

print ()
print ("#========== section 3 ==========#")
print ()

print("Mary had a little lamb.")
print("Its fleece was white as %s." % "snow")
print ("And everywhere that Mary went.")
# repeats the period 10 times!~!
print ("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"

end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# I don't think the comma does anything...?
# it could be that comma represents line continuation in python2
print (end1 + end2 + end3 + end4 + end5 + end6,)
print(end7 + end8 + end9 + end10 + end11 + end12)
