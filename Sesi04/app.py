path = "text.txt"
try:
    with open(path, 'r', encoding='utf-8') as f:
        print(f.readline())
except FileNotFoundError as error:
    print(error)
else:
    print('Success')
finally:
    print('Finally')

x = 2
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

assert (x < 3), "Value x must < 2"
