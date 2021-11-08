print('\n# Integer')
print(10)
print(type(10))

print('\n# Float')
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

print('\n# String')
print("Hacktiv8")
print(type("Hacktiv8"))
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')

print('\n# Boolean')
print(type(True))
print(type(False))
print(100 > 200)  # False
print(100 == 200)  # False
print(100 < 200)  # True

print('\n# Variable Assignment')
n = 300
print(n)
a = b = c = 300
print(a, b, c)

print('\n# Variable Name')
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)

print('\n# Operators and Expressions')
a = 10
b = 20
print(a + b)
print(a + b - 5)

print('\n# Arithmetic Operators')
a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

print('\n# Comparison Operators')
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

print('\n# String Manipulation')
s = 'foo'
t = 'bar'
# + and * Operators
print(s + t)
print(s * 4)
# Case Conversion
print(s.capitalize())
print(s.lower())
print(s.swapcase())

print('\n# Python Lists')
a = ['foo', 'bar', 'baz', 'qux']
print(a)

print('\n# Modifying List Value')
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-1] = 20
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)


print('\n# Python Tuples')
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])

(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
print(s1)

print('\n# Defining and Accessing Dictionary')
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
}
print(MLB_team['Minnesota'])
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)

print('\n# Building a Dictionary Incrementally')
person = {}
person['fname'] = 'Hack'
person['lname'] = '8'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['children'][1])
