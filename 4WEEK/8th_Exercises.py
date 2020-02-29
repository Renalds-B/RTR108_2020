fhand = open('mbox.txt')

print('\nReading files\n')
# Efficient way, if you don't know if the file size doesn't exceed system limitations
count=0
for line in fhand:
    count = count+1
print('Line Count:', count)
# In the next example the entire contents of the mbox.txt are read directly into the variable inp.
#It is a good idea to store the output of read as a variable because each call to read exhausts the resource.
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20]) #First 2 characters from string variable inp 

print('\nSearching through a file\n')
#fhand = open('mbox.txt')
#count = 0
#for line in fhand:
#    line = line.rstrip() #We could use line slicing to print all but the last character, but a simpler approach is to use the rstrip method which strips whitespace from the right side of a string as follows:
#    if line.startswith('From:'):
#        print(line)
        
fhand=open('mbox_short.txt')
for line in fhand:
    line = line.rstrip()
    # Skip uninteresting lines
    if not line.startswith('From:'):
        continue
    #Process our 'interesting' line
    print(line)

print('\nSearch for lines with @uct.ac.za\n')

fhand = open('mbox_short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue #Ja -1 uzraadaas tiem string, kuriem nav mekleejamaas veertiibas, tad kaa shii programma straadaa?
    print(line)

print('\nLetting the user to choose the file name\n')
def search():
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()
    count = 0
    for line in fhand:
        if line.startswith('Subject:'):
            count = count+1
    print('There were', count, 'subject lines in', fname)

search()

print('\nWritting files\n')
fout = open('output.txt', 'w') #That 'w' changes the game of the open function. _witty face_
print(fout)
#If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful! If the file doesn't exist, a new one is created.
line1 = "This here's the wattle,\n"
fout.write(line1)
#We must make sure to manage the ends of lines as we write to the file by explicitly inserting the newline character when we want to end a line. The print statement automatically appends a newline, but the write method does not add the newline automatically.
line2 = 'the emblem of our land.\n'
fout.write(line2)
fout.close()

print('\nDebugging\n')
s = '1 2\t 3\n 4'
print(s)
print(repr(s))


print('\n Exercise 1\n Write a program to read through a file and print the contents of the file (line by line) all in upper case.\n')
def shouty():
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened: ', fname)
        exit()
    for line in fhand:
        line = line.rstrip().upper()
        print(line)
shouty()

print('\n Exercise 2 \nWrite a program to prompt for a file name, and then read through the file and look for lines of the X-DSPAM form.\n')
def spamy():
    count=0
    spamed=float(0)
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened: ', fname)
        exit()
    for line in fhand:
        line = line.rstrip()
        if line.find('X-DSPAM-Confidence:') == -1:
            continue
        start = line.find(':')
        konvert=float(line[start+2:-1])
        count=count+1
        spamed = spamed+konvert
    print('Average spam confidence:', spamed/count)
spamy()

print('\n Exetrcise 3 \n')
def searchEasterEgg():
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        if fname == 'na na boo boo':
            print('NA NA BOO BOO TO YOU - You have benn punk\'d!')
            exit()
        else:
            print('File cannot be opened:', fname)
            exit()
    count = 0
    for line in fhand:
        if line.startswith('Subject:'):
            count = count+1
    print('There were', count, 'subject lines in', fname)

searchEasterEgg()
