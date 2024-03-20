s1 = "hello how are you"
s2 = "hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
n1 = 0
n2 = 1
ans = 0+1

n1 = 1
n2 = 2
ans = 1+2

n1 = 2
n2 = 3
ans = 2+3

# ! Find the 8th fibanochi number
num = 8
n1 = 0
n2 = 1
for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 =ans
print(ans)


# ! Constructors

# Eg:2
# unparameterised constructor
class profile:
    def __init__(self):
        print("hello world")


obj = profile()
obj.__init__()

# ? Eg:3
# Parameterised Constructor
class profile:
    def __init__(self, id ,name ,age):
        print(id,name, age)
       
obj = profile(1,"farid", 21)

# ? Eg:4
class c1:
    email = "sid@gmail.com"

    def m1(self):
        name = "sid"
        place = "cbe"
        print(name, place)
        print(self.email)
object = c1()
object.m1()

# ? Eg:5
class c1:
    email = "farid@gmail.com"
    def m1(self):
        name = "farid"
        age = 20
        return name, age
    def display(self):
       # ! print(name, age)
       # ! print(self.name, self,age)
       print(self.m1())
object = c1()
object.display()


# Eg:6
# To use the variable inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "farid"
        self.email = "farid@gmail.com"
        # return name, email # error ---> cnnot use return with constructor
       
    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()

# -----> Inheritance
# The process of utilising the methods and attributes of parent class
# Throught the object of child class it is called as inheritance

# ? 5 types of Inheritance
# Single Inheriatance
# Multiple Iheritance
# Hybrid Inheritance
# Heirrichal Inheritance

# Single Inheritance
# It has only one parent class and only one child class
# Eg:1
class parent:
    def m1 (self):
        print("Iam parent class")

       
class child(parent):
    def m2(self):
        print("Iam child class")

p = parent()
p.m1()

obj1  = parent()
obj1.m1()

# ! Eg : 2
class c1:
    def  __init__(self):
        print("I am constructor from parent class") 

class child1(c1):
    pass


obj = child()



# ! Eg : 3
class parent:
    name = "farid"

class child(parent):
    name = "farid1"

    def display(self):
        print(self.name)

d = child()
d.display()                   
        

# ! Multilevel inheritance

# ? Eg : 1
class voice:
    def sound(self):
        print("All the animals have their own voice")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice
all.cat_voice()
all .sound
all.parrot_voice

# ! Multiple Inheritance
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(4,2)

# ! Heirarical inheritance
# The one parent class will be act as parent for all the child classes
class catagory:
    def cat_name(self, weight):
        print("Vegetables")

class Tomato(catagory):
    def tomato_specs(self):
        colour="black"
        taste = "neutral taste"

class carrot(catagory):
    def carrot_specs(self):
        colour="orange"
        taste = "sweet"

c = carrot(catagory)
c.carrot_specs()
c.weight("30gms")

t = Tomato()
t.tomato_specs()
t.weight("20"gms)

# ! Hybrid inhertance
# ? The combination of above 4 inheritance is called hybrid inheritance
class c1:
    def m1 (self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")

class c3:
    def m3(self):
        print("class3")

class c4:
    def m4 (self):
        print("class4")

class c5 :
    def m5(self):
        print("class5")
class c6(c5, c4, c2, c1):
    def m6(self):
        print("class6"


obj = c6()
obj.m3()

# ! ------> polymorphism
# ? poly - many, morph ---> form
# A function which has the ability to perform more than 1 functionality
# then it is considered to be as polymorphism

# * polymorphism in builtin functions
len() --> which is used to find the length of list, tuple, dict etc..
index()
max()
min()
count()
pop()
and more...

# * polymorphism in operator
# +
print (8+8)
print("k"+'1')
print([1, 2, 3] +[4, 5, 6])

# *
print(6*7)
l1 = {12, 3, 4, 5, 6}
print(*l1)
def f1(*args)
l1 = [1,2,3,4]
print(l1*10)

# Polymorphism in classes
we can achieve polymorphism in 2 ways
1.) Method overloading ---> it is not possible
2.)Method overriding

#) Tasks
#Write the code for the belwo tasks using function
#!)>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'
#2.) Find then 67, is strong number or not
#3.) 11 [1,2,3,4,5,6]
#n=2> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]

