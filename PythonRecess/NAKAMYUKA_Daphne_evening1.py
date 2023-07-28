#dictionaries
#they are changeable bt dont allow duplicates
#one dictionary can have different data items with differnt datatypes


mydict = {
    'phone' : 'iphone',
    'iphoneModel' : 'iphone 14',
    'year' : 2023
}
print (mydict)
print (len(mydict))
print (type(mydict))

#Access dictionary items
print (type((mydict['phone']))) 

year = mydict['year']
print(year)

iphoneModel = mydict.get('iphoneModel', 'no model here')
print(iphoneModel)

m = mydict.keys()
print(m)


#Exercise 1; use values method to retrieve to return the list of all values in the dictionary


clas = {
    1 : 'Senior one',
    2 : 'Senior two',
    3 : 'Senior three',
    4 : 'Senior four'
}

print (clas.values())


#Exercise 2: to check if a key exists in the dictionary

clas = {
    1 : 'Senior one',
    2 : 'Senior two',
    3 : 'Senior three',
    4 : 'Senior four'
}

if 1 in clas:
    print('key exists in dictionary')



#exercise 3; Give an example on how to change dictionary items, update the dictionary
clas = {
    1 : 'Senior one',
    2 : 'Senior two',
    3 : 'Senior three',
    4 : 'Senior four'
}

clas[1] =  "form one"
print(clas[1])



#Exercise 4; An example on how to add dictionary items, how to remove dictionary items

clas = {
    1 : 'Senior one',
    2 : 'Senior two',
    3 : 'Senior three',
    4 : 'Senior four'
}
clas[5] = 'Senior 5'
clas[6] = 'senior 6'
print(clas.values())



#removing dictionary items
clas.pop(1)
clas.pop(2)
print(clas.values())



#exercise 5; An example on how to loop through a dictionary and how to nest dictionaries
clas = {
    1 : 'Senior one',
    2 : 'Senior two',
    3 : 'Senior three',
    4 : 'Senior four'
}
for x in clas:
    print (clas[x])

#########################################################################
    # numbers
#integers, floats complex

# m = 10
# n = 12.43
# p = 4j
# print(type(m))
# print(type(n))
# print(type(p))

#integers
x = 1232113
y = 2
z = -23422

print(type(x))
print(type(y))
print(type(z))

x = 1232113.234
y = 2.4
z = -23422.432

print(type(x))
print(type(y))
print(type(z))

#complex
w = 6 +10j
t = -4j
h = 2j
print(type(w))
print(type(t))
print(type(h))


p = 30
z = complex(p)
print(type(z))

#conver from int to float
#convert float to complex

weight = 300
mass = float(weight)
print(type(mass))

w = 6.4
y= complex(w)
print(type(y))


#####################################################################
#CASTING
#Used to specify vsrisble types
##Example
h = int(20) #means h is an integer
a = int("201") #a is an integer

print(h)

print(a)

#######################################################################
#Strings
#They arre either in double quotes or single quotes
print('Afternoon')
print("Afternoon")


#assign a string to a variable
w = "Afternoon"

print(w)

#multiline strings
q = '''i am in BSSE year 3
Currrently doing recess in python,
Data science,
Django
'''
print (q)

# strings as arrays
a= 'Afternoon'
print (a[1])


#Exercise 1: Use the len function to determine the length your string
name = 'Daphne'
print (len(name))

#Exercise 2: use a for loop on in a string
x = 'martha'
for l in x:
    print (l)

#Exercixe 3:Give an example of slicing in strings

course =  'Software engineering'
print(course[2:9])

#How to modify strings using differnt methods in python

a = 'Afternoon'
print(a.lower())
print(a.upper())

b = '   Afternoon      '
print(b.split())

#concatenation of strings

c = 'Afternoon'
d = 'Class '
w = c + d
print(w)
z = c + " " +d
print(z) 

##############################################################33
#format stringd
#is used when one is combining a string to a number

age = 21
name = 'My name is Dana, I am '
print(f"{name} {age}")

#############################################################################################
# Booleans
# have true and false

print(20<10)
print (30==40)
print (30>10)

print (bool(15))

r = 'DAphne'
z = 22

print (bool(r))
print (bool(z))


# Exercise Use conditional statement to show how to use boolean
x = 0
while (x<=10):
    print ('x')
    x += 1