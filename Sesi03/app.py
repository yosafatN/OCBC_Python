import person

print("\n# Calling a Function")


def printMe(str):
    print(str)
    return


printMe("I'm first call to user defined function!")
printMe("Again second call to the same function")


print("\n# Keyword Arguments")
printMe(str="Hacktiv8")


print("\n# Default Arguments")


def printInfo(name, age=26):
    print("Name : ", name)
    print("Age  : ", age)
    return


printInfo(name="Hacktiv8", age=50)
printInfo(name="hacktiv")


print("\n# Variable-length arguments")


def fucntionVariableLength(name, *hobby):
    print("Name : ", name)
    print("Hobby: ", hobby)
    return


fucntionVariableLength(
    "Hacktiv8", "Reading Webtoon", "Play Video Game", "Coding")


print("\n# The Anonymous Functions")
def sum(arg1, arg2): return arg1 + arg2


print("Value of total: ", sum(10, 20))
print("Value of total: ", sum(20, 20))


print("\n# The return Statement")


def sum(arg1, arg2):
    total = arg1 + arg2
    total2 = total + arg1
    print("Inside the function : ", total)
    return total2


total = sum(10, 20)
print("Outside the function: ", total)


print("\n# Import Person")
person.printPerson()
