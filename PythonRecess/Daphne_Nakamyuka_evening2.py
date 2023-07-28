#Exercise 1 (lists)
#1
print("==================================================================================")
print('Exercise 1')
print("==================================================================================")

names = ['Jerome', 'Sheila', 'Vicor', 'Ronnie', 'James']
print (names[1])

#2
names[0] = 'George'
print (names)

#3
names.append('William')
print (names)


#4
names.insert(2, 'Bethel')
print (names)

#5
names.remove(names[2])
print (names)

#6
print(names[-1])

#7

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print (colors[2:5])

#8
countries = ['USA', 'Japan', 'Cuba', 'Uganda', 'Rwawnda', 'Sudan', 'Poland']
countries_copy = countries[:]

#9
for country in countries:
    print(country)

#10
animals = ['pig','dog', 'cat', 'goat', 'cheeetah']
animals.sort()
print (animals)

animals.sort(reverse=True)
print (animals)

#11
for animal in animals:
    if 'a' in animal:
        print (animal)

#12
fnames =['Daphne', 'Martha', 'Edigar', 'Brian']
snames =['Nakamyuka', 'Kisakye', 'Tumusiime', 'Wabweni']

names = fnames + snames
print(names)

###########################################################################################################
#Exercise 2 tuples
print("==================================================================================")
print('Exercise 2')
print("==================================================================================")

#1
x = ('sumsung', 'iphone', 'tecno', 'redmi')
print(x[0])

#2
print(x[-2])

#3
y = list (x)
y[1] = 'itel'
x = tuple(y)
print(x)

#4
y = list (x)
y.append('Huawei')
x = tuple(y)
print(x)

#5
for item in x:
    print(item)

#6
y = list (x)
y.remove('tecno')
x = tuple(y)
print(x)

#7
cities = tuple(['Kampala', 'Masaka', 'Mbale', 'FortPortal', 'Arua'])
print(cities)

#8
city1, city2, city3, city4, city5 = cities
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)
    
#9
print(cities[2:5])

#10
fnames =['Daphne', 'Martha', 'Edigar', 'Brian']
snames =['Nakamyuka', 'Kisakye', 'Tumusiime', 'Wabweni']
fullnane = fnames + snames
print(fullnane)

#11
colors = ['red', 'orange', 'yellow', 'green', 'blue']
newColors = colors * 3
print (newColors)

#12
thistuple = (1,3,7,8,7,5,4,6,8,5)
print(thistuple.count(8))

#############################################################################################
#exercise 3 Sets
print("==================================================================================")
print('Exercise 3')
print("==================================================================================")

#1
beverages = set(['coffee','Soyacup','tea']) 

#2
beverages.add('Juice')
beverages.add( 'water')
print(beverages)

#3
myset = {'oven', 'kettle', 'microwave', 'refridgelator' }

if 'microwave' in myset:
    print("microwave in  myset")
    
#4
myset.remove('kettle')
print(myset)

#5
for item in myset:
    print(item)

#6
set1 = {'chair', 'table', 'stool', 'benck'}
list1 = ['sofa', 'bed']

s = set(list1)

print (set1.union(s))

#7
names = {'Jane', 'Peter', 'Emma'}
ages = {20, 21, 22}

combination = names.union(ages)
print (combination)


#############################################################################################
#Exercise4 Strings

print("==================================================================================")
print('Exercise 4')
print("==================================================================================")

#1
name ='Jane Mary'
age = 19
print(name + ' '+str(age))

#2
txt = '       HEllo  , Uganda!    '
txt = txt.strip()
print(txt)

#3

print(txt.upper())

#4
tex = txt.replace('U', 'V')
print(tex)

#5
y = 'I am proudly ugandan'
print(y[2:5])

#6
x = 'All "Data Scientists" are cool'


#############################################################################################


#Exercise 5 (Dictionaries)

print("==================================================================================")
print('Exercise 5')
print("==================================================================================")

#1
shoes = {
    'Brand' : 'Nick',
    'color' : 'black',
    'size' : 40
}
print(shoes['size'])

#2
shoes['Brand'] = 'Adidas'
print(shoes)

#3
shoes['type'] = 'Sneakers'
print(shoes)

#4
print(shoes.keys())


#5
print(shoes.values())

#6
if 'size' in shoes:
    print("Size is in dictionary")
    
#7
for item in shoes:
    print(shoes[item])
    
#8
shoes.pop('color')
print(shoes)

#9
shoes.clear()
print(shoes)

#10
age = {
    'Jane' : 32,
    'Robert' : 40,
    'Martha' : 21,
}

age1 = age.copy()

print(age1)

#11
classData ={
    'StreamA' :{
        'girls' : 33,
        'boys' : 26
    },
    'StreamB' :{
        'girls' : 35,
        'boys' : 23
    },
    'StreamC' :{
        'girls' : 30,
        'boys' : 18
    }
}
print(classData)
