print("\n Traversal through a string with a loop\n")
fruit = 'raspberry'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index+1
print('\n Exercise 1 \n Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards\n')
index = 0
while index < len(fruit) and index != -len(fruit):
    letter = fruit[index]
    print(letter)
    index = index-1
print('\nFunction found on the net:\n')
word = 'python' 
def backwards(word):
    index = len(word) - 1  # adjust for 0th index
    while index >= 0:
        print(word[index])
        index -= 1

backwards(word)

print('\n Another way to write a traversal is with a "for" loop:\n')
for char in fruit:
    print(char)
#Each time through the loop, the next character in the string is assigned to the variable "char". The loop continues until no characters are left.

print('\n Exercise 2\nGiven that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.\n')
print(fruit[:])
print('\nLooping and counting\n')
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count+1
print(count)
print('\n Exercise 3 \n Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments \n')
def count(string, letter):
    counter = 0
    for inrow in string:
        if inrow == letter:
            counter = counter+1
    print('We counted %d letters'%counter)
count('am I a joke to you? Nintendo vs SEGA!','e')

print('\n>String comparison \n')
word = input('Enter a word/string for comparidon with bananas!!! :')
if word == 'banana':
    print('All right, bananas.')
elif word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

print('\n>String methods \n')
help(str.upper)
word = 'banana'
new_word = word.upper()
print(new_word)

print('\n For example, there is a string method named _find_ that searches for the position of one string within another: ')
word = 'banana'
index = word.find('a')
print(index)
print('\nThe find method can find substrings as well as characters:\n')
index = word.find('na')
print(index)
index = word.find('na',3) # Kas sheit notiek?!
print(index)
print('\n One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: ')
line = '   Here we go  '
print(line,'\n',line.strip())

print('\nSome methods such as "startswith" return boolean values\n')
line = 'Have a nice day'
print(line)
A=line.startswith('Have')
print('Line starts with Have?',A)
B=line.startswith('h')
print('Line starts with h?',B)
# Startswith requires case to match, so sometimes we take line and map it all to lowercase before we do any checking using the "lower" method.
C=line = 'Have a nice day'
D=line.startswith('h')
E=line.lower()
print('If using "lower" methond on line: ', E)
F=line.lower().startswith('h')
print('Line starts with h if it\'s mapped as lowercase?',F)

print('\n Exercise 4 \n There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"')
def howmanyinbanana():
    import re
    import sys
    print('\n\nWelcome to a program which counts how many user specified letters are in a word "banana"!\nIt\'s absolutely useful so I hope you\'l have fun with it!')
    lettery = str(input('\nInputt\'o a letter\'o! For bananaS.S.S. Squad! : '))
    stringy = 'banana'
    county = stringy.count(lettery)
    if not re.match("^[a-z]*$", lettery):
        print('Error\'Ah! Only letterz a to z allAwd!')
        sys.exit()
    elif len(lettery) > 1:
        print('ERROR!!!! Can U type just one letter?! Geez..')
        sys.exit()
    print(county)
howmanyinbanana()


print('\nParsing strings\n')
data = 'From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008'
atpos = data.find('@')
print(data, "Symbol @ is at: ", atpos)
sppos = data.find(' ',atpos)
print("Where's the next space after @ symbol? :",sppos)
host = data[atpos+1:sppos]
print(host)

print('\nFormat operators\n')
camels = 42
print('I have spotted %d camels' % camels)
print('In %d years I have spotted %g %s' %(3, 0.1, 'camels'))

print('\n Exercise 5 \n')
str = 'X-DSPAM-Confidence: 0.8475 '
start = str.find(':')
itog = str[start+2:-1]
print('We extracted this:',itog)
konvert=float(itog)
print(type(itog))
print('We got a floating number point:',konvert)
print(type(konvert))
