x = 0
y = 5

# If Statement
if x < y:
    print('x < y')

if x > y:
    print('x > y')

if x:
    print(x, 'x')

if y:
    print(y, 'y')

if x in {0, 1, 2, 3}:
    print('X in')

# Group Statements
weather = 'nice'
if weather == 'nice':
    print('Weather Nice')
    print('Paling Nice')
    print('Ter-Nice')

# else and elif Clauses
isGanteng = 'tidak ganteng'
isKaya = 'kaya'

if isGanteng == 'ganteng':
    print('Aku Ganteng')
elif isKaya == 'kaya':
    print('Aku tidak ganteng tapi aku kaya')
else:
    print('Aku Rapopo')

# One-Line if Statements
conditional = 'true'
conditional == 'true' if print('benar') else print('salah')

# While
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print('else while')

# Nested while loops

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))

    b = ['baz', 'qux']

    while len(b):
        print('>', b.pop(0))

# Python for loop
a = ['a', 'b', 'c']
for i in a:
    print(i)

# range() function
x = range(5)
for n in x:
    print(n)

# Altering for loop behavior
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'az' in i:
        break
    print(i)
