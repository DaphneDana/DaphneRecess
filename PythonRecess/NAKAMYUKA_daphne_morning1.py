age = 60
if (age<18):
    print('You are underage')
elif(age>=65):
    print('You are an adult')
else:
    print('You are a senior citizen')
    
# """#
# oops
# for loop
# while loop

# for i in sequence:

#    """
cars = ['Tesla', 'Jeep', 'Ford', 'Toyota']
for car in cars:
    print (car)

fruits = ['apple', 'banana', 'watermelon', 'tomato','orange', 'pineapple']
for fruit in fruits:
    print(fruit)

# while loop
x = 0
while x<= 5:
    print(x)
    x += 1

fruits = ['apple', 'banana', 'watermelon', 'tomato','orange', 'pineapple']
i = 0
while i< len(fruits):
    print(fruits[i])
    i +=1
    
#break and continue
for num in range(0 ,60,4):
    if num == 3:
        continue
    print(num)

#exception handling
#try, except, finally:
try:
    x = 10/3
    print(x)
except:
    print('you cant devide a number by zero')
finally:
    print('it is done')

#Exercise 1
#write a program to a student abou their mental health
#Prompt a student to rate their mental health on a scale of 1 -5
mental_health = int(input('What is your mental health on a scale of 1 - 5'))

mood = {
    1: "need to see a doctor",
    2: 'You are not fine',
    3: 'Your are moderate',
    4: "You are doing great",
    5: "you are healthy",
}
if mental_health in mood:
    print("you are " + mood[mental_health])
else:
    print('Please enter a value between 1 and 10') 
