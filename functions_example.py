name="Fedrik"
age=45

a = 2
b = 4

def printdetails():
    print('my name is %s and age is %d' % (name,age) )

printdetails()

print("...........................................................................................")


print("Functions with arguments")

def sum(a, b):
    return a+b;

def maximum(a, b):
    return max(a,b);

print(sum(a, b))
print(maximum(a, b))



print("Default Arguments")

def printColor(color="green"):
    print("The color that is adored by me is: "+ color)

printColor("Yellow")
printColor("blue")
printColor()

print("------------------------------------------------------------------------------------")


print("Keyword Arguments")

def printyourDetails(name,age):
    print(f'my name is {name} and age is {age}')

printyourDetails(name="George",age=45)

printyourDetails(age=45,name="Sam")


print("------------------------------------------------------------------------------------")


print("Arbitary Arguments")

def welcomeMembers(*membernames):
       for teammember in membernames:
        print("Welcome "+ teammember + " to the team")

welcomeMembers("Alice","Bob","Charlie","Daniel")



print("------------------------------------------------------------------------------------")



