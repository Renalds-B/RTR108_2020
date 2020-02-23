print('Values and types')
print()
print(4)
print('Hello,World!')
print(type('Hello,World!'))
print(17)
print(type(17))
print(3.2)
print(type(3.2))
print('17')
print(type('17'))
print(1,000,000)
print()
print('Variables')
print()
message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931
print(n)
print(pi)
print(message)
print()
print('Variable names and keywords')
print()
print('If you give a variable an illegal name, you get a syntax error. \n For example: 76trombones is illegal because it begins with a number. more@ is illegal because it contains an illegal character, @. But what\'s wrong with class? \n It turns out that class is one of Python\'s keywords.')
print('Python reserves 35 keywords:\n and       del       from      None      True\n as        elif      global    nonlocal  try\n assert    else      if        not       while\n break     except    import    or        with\n class     False     in        pass      yield\n continue  finally   is        raise     async\n def       for       lambda    return    await')
print()
print('Statements')
print('The assignment statement produces no output')
print(1)
x = 2
print(x)
print()
print('Operators and operands')
print('Operators are special symbols that represent compulations like addition and multiplication. The values the operator is applied to are called operands')
print(20+32, 5**2, ((5+9)*(15-7)/2))
print()
print('Expressions')
print('Expression is a combination of values, variables and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions')
print(17,
x,
x + 17)
print()
print('Modulus operator')
print('The \"modulus operator\" works on integers and yields the remainder when the first operand is divided by the second. In Python, the modulus operator is a percent sign (%). The syntax is the same as for the other operators')
quotient = 7 // 3
print('7 un 3 daliijums', quotient)
remainder = 7 % 3
print('7 un 3 atlikums', remainder)
print('\nString operations\n The + operator works with strings, but is not addition in the mathematical sense. Instead it performs concentration, which means joining the strings by linkin them end to end. F.ex:')
first = 10
second = 15
print(first+second)
first = '100'
second = '150'
print(first+second)
print('The * operator also works with strings by multiplying the content of a string by and integer. F.ex:')
first = 'Test'
second = 3
print(first*second)
print('\n Asking the user for input\n')
inp = input()
print(inp)
print('I\'ts also a good idea to print promt, so the user knows what to input\n')
name = input('What is your name?\n')
print('Your name is',name)
#If you expect the user to type an integer, you can try to convert the return value to int using int() function
prompt = 'What ... is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)
int(speed)
print(speed)
# This is a comment
print('\n Chossing mnemonic variable names\n')
a = 35.0
b = 12.50
c = a*b
print(c)
# Is the same as
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)
#Is the same as
x1q3z9ahd = 35.0
x1q3z9afd = 12.0
x1q3p9afd = x1q3z9ahd * x1q3z9afd
print(x1q3p9afd)
print('\nDebugging\n')
print(1.0/2.0*pi)
print(1.0/(2.0*pi))
