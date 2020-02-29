# Random numbers
print('\n Exercise 1 \n')
import random

for i in range(10):
    x = random.random()
    print(x)
print('\nRandom int\'s\n')
for i in range(4):
    y = random.randint(5,10)
    print(y)
print('\nTo choose an element from a sequence at random, you can use choice\n')
t = [1,2,3]
z = random.choice(t)
print(z)
z = random.choice(t)
print(z)

print('\nAdding new functions\n')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print('I sleep all night and work all day')
print_lyrics()
# Inside another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
#Call newmade function
repeat_lyrics()
print('\nDefinitions and uses\n Exercise 2 & 3\n')
#Move the last line of this program to the top, so the function call appears before the the definitions.
#Run the programs and see what error message you get. - # I'm getting the error that function is not defined.
#Move the function call back to the bottom and move the definition of print_lyrics_1 after the definition of repeat_lyrics.
#What happens when you run this program? - Nothing, because function repeat_lyrics_1 doesn't contain useable definitions.

def repeat_lyrics_1():
    print_lyrics_1()
    print_lyrics_1()
def print_lyrics_1():
    print('Never gonna give you up!')
    print('Never gonna let U down!')

repeat_lyrics_1
print('\nParameters and arguments\n')
def print_twice(bruce):
    print(bruce)
    print(bruce)
michael = 'Eric, the half a bee.'
print_twice(michael)
print('\nFruitful functions and void functions\n')
import math
radians = 0.7
x = math.cos(radians)
golden = (math.sqrt(5) +1) /2
#To return result from a function, we use the return statement in our function. F.e., we could make a very simple f-ion called addtwo that adds two numbers together and returns a result
def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3,5)
print(x)
# Exercise 4
# What is the purpose of the "def" keyword in Python?
# It indicates the start of a function and that the following indented section of code is to be stored for later. (Not sure tbh, it could also even be the answer e) None of the above, because def means definin/-ed. def just defines a new function, d'oh).
# Who TF even exercises in using Python, while drinkin'in a frickin' Avotu Eziic? Is this some sort of a joke?
#Nah, Still enjoying that. Too bad that time flies so fast. :(
print('\n Exercise 5 \n')
def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()
print('\n Exercise 6 \n')
def computepay(hours,rate):
    print('Hours: %.2f \nRate: %.2f' %(hours, rate))
    if hours <=40:
        wage = hours*rate
        print('Pay: ',wage)
#        return wage
    else:
        wage = (hours-40)*(rate*1.5)+(40*rate)
        print('Pay: ',wage)
#        return wage
    
computepay(45,10)
print('\n Exercise 7 \n')
# Rewrite the grade program from the previous chapter using a function called computegrade that takes score as its parameter and returns a grade as a string
score = 0
error_msg = "Bad input! Use numerals between 0.0 and 1.0"
warn_msg = "Bad score! Use numerals between 0.0 and 1.0"
def computegrade(score):
    try:
        if (float(score) >= 0) and (float(score) <= 1):
            if score >= 0.9:
                print('Grade: A')
            elif score >= 0.8:
                print('Grade: B')
            elif score >= 0.7:
                print('Grade: C')
            elif score >= 0.6:
                 print('Grade: D')
            elif score < 0.6:
                print('Grade: C')
        else:
            print(warn_msg)
    except:
        print(error_msg)
        
# Use function whilst askin' for user input.
input_score = input('Enter a score between 0.0 and 1.0: ')
try:
    if (float(input_score) >= 0) and (float(input_score)<= 1):
        computegrade(input_score)
    else:
        print(warn_msg)
except:
    print(error_msg)
