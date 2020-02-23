n = 5
while n > 0:
    print(n)
    n = n-1
print('Blastoff!')

#Infinite loop
#n = 10
#while True:
#    print(n, end=' ')
#    n = n-1
#print('Done!')

print("\nFunctiona infinite loop\n It echoes everything you type, unless it's 'done'\n")
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

print("\nHere's an example of a loop that copies its input until the user types 'done', but treats lines that start wit the has character as lines not to be printed (kind of like Python comments).\n")
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
# Definite loops using 'for'
FRIENDS = ['Joseph', 'Glenn', 'Sally']
for friend in FRIENDS:
    print('Happy New Year:', friend)
print('Done!')
# Loop patterns
# Counting and summing loops
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    print('Count: ', count)
    
print("\nIf itervar makes you confused, check this (var 'itervar' changed to var. 'count'):\n")

count = 0
for count in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    print('Count: ', count)

print("\n Another similar loop \n")

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
#Functions len() and sum() do these tasks, so making loops like this are an unecessary task.


#MAXimum and MINimum loops
#To find the largest value in a list or sequence, we construct the following loop:
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest, '\n')

# To compute the smallest number, the code is very similar with one small change
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest, '\n')
#Functions max() and min() do these tasks, so making loops like this are an unecessary task.
###
print('\n Exercise 1\n')
#Write a program which repeatedly reads numbers until the user enters done. Once done is entered print out the total, count, and average of the numbers.
#If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number

total=0
count=0
while True:
    num = input('Enter a number: ')
    if num == 'done':
        print(total, count, (total/count))
        break
    else:
        try:
            total = total + float(num)
            count = count + 1
        except:
            print('Invalid input!')
            continue
print('Making script into a function: Use calculator()')

def calculator():
    total = 0
    count = 0
    while True:
        num = input("Enter a number: ")
        if num == 'done':
            print(total, count, (total / count))
            break
        else:
            try:
                total = total + float(num)
            except:
                print("Invalid input")
                continue
        count = count + 1
calculator()

print('\n Exercise 2 \n')
# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers, instead of the average
#Not my program, sadly.
total = 0
count = 0
average = 0
error_msg = 'Error, please enter a valid number.'
largest = None
smallest = None
print('Before largest: ', largest, '\nBefore smallest: ', smallest)
while True:
    line = input('Enter number: ')
    if line == 'done':
        break
    try:
        if float(line):
            print('Input is valid, thanks!')
            total = total + float(line)
            count = count + 1
            itervar = float(line)
            if largest is None or itervar > largest:
                largest = itervar
            print('Loop_largest: ', itervar, largest)
            if smallest is None or itervar < smallest:
                smallest = itervar
            print('Loop_smallest: ', itervar, smallest)
    except:
        print(error_msg)
if count !=0:
    average = total/count
    print('##DONE!')
    print('##Total: ', total)
    print('##Count: ', count)
    print('##Average: ', average)
    print('##Largest: ', largest)
    print('##Smallest: ', smallest)
else:
    print('You did not enter any values!')
