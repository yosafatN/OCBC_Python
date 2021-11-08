x = 0
y = 5

# If Statement
print('\n# IF Statetment')
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
print('\n# Groyp Statements')
weather = 'nice'
if weather == 'nice':
    print('Weather Nice')
    print('Paling Nice')
    print('Ter-Nice')

# else and elif Clauses
print('\n# Else and Elif Clauses')
isGanteng = 'tidak ganteng'
isKaya = 'kaya'

if isGanteng == 'ganteng':
    print('Aku Ganteng')
elif isKaya == 'kaya':
    print('Aku tidak ganteng tapi aku kaya')
else:
    print('Aku Rapopo')

# One-Line if Statements
print('\n# One-Line if Statement')
conditional = 'true'
print('benar') if conditional == 'true' else print('salah')

# While
print('\n# While')
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print('else while')

# Nested while loops
print('\n# Nested while loops')
a = ['foo', 'bar']
while len(a):
    print(a.pop(0))

    b = ['baz', 'qux']

    while len(b):
        print('>', b.pop(0))

# Python for loop
print('\n# Python for loop')
a = ['a', 'b', 'c']
for i in a:
    print(i)

# range() function
print('\n# Range Function')
x = range(2, 8)
result = ''
for n in x:
    result = result + str(n) + ', '
print(result)

# Altering for loop behavior
print('\n# Altering for loop behavior')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'az' in i:
        break
    print(i)

d = {'foo': 1, 'bar': 2, 'baz': 3, 'qux': 4}
for k in d.values():
    print(k)
