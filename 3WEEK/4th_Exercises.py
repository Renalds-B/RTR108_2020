inp = input('Enter Fahrenheit Temperature: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0)*5.0/9.0
    print(cel)
except:
    print('Please enter a number!')
    
print('\n Exercise 1 \n')
hours = int(input('Enter Hours: '))
rate = int(input('Enter Rate: '))
if hours <= 40:
    print('Pay: ', hours*rate)
else:
    print('Pay: ', (hours-40)*(rate*1.5)+(40*rate))

print('\n Exercise 2 \n')
try:
    hours = int(input('Enter Hours: '))
    rate = int(input('Enter Rate: '))
    if hours <= 40:
        print('Pay :', hours*rate)
    else:
        print('Pay :', (hours-40)*(rate*1.5)+(40*rate))
except:
    print('Error! Please enter a numeric input!')

print('\n Exercise 3 \n')
score = float(input('Enter score: '))
if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print('Grade: A')
    elif score >= 0.8:
        print('Grade: B')
    elif score >= 0.7:
        print('Grade: C')
    elif score >= 0.6:
        print('Grade: D')
    elif score < 0.6:
        print('Grade: F')
else:
    print('Bad score!')
