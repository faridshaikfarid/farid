
#Eg:3
def profile(name, age, place):
    txt ="My name is {}.iam {} years old.Iam from{}."
    print(txt.format(name, age, place))
profile("bharath", 20, "kadapa")

#Eg:4
# ? Function with return statement

# return
#1.) A varable decleared inside the function can be accessed outside the function
#using return
#2.) return does not print anything
#3.) we cannot write any code below return statement
def f1():
    z = 8
f1()
print() #  error ---> cannot use outside the function

def f1(a, b):
    c = a*b
    return c
print(f1(6, 8))
obj = f1(6,8)
obj1  =f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)


# 123
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n , "Palindrome")
    else:
        print("Not palindrome")
a = int(input("Enter the value:"))
palindrome(a)


#Based on the decleration of parameter and args
# Functions are divided into 5 catagories

# Positional args
# keyword args
# defalut args
# variable length args
# keywords variable length args

#* Positional args
# The position of parameter have to same as positional os arguments
# Eg:1

def profile(name,phone,mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name,phone, mark))
profile(8956246324,"Bharath", 89)

# keyword args
# ! Eg:1
#To overcome the disadvantage of position args, we use keyword args
# It is the process of intialising the parameter with the args while calling the function
def profile(name,phone,mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name,phone, mark))

profile(name = "Bharath",mark=96, phone=1234567890)

# todo Exeception of keyword args function
def profile(name,phone,mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name,phone, mark))

#profile(name = "sid",1234567890,mark=96)
#profile( 1234567890, name="sid",mark=96)
profile("Bharath", mark=98, phone=1234567890)

# Defalut args
# ! Eg:1
def profile(name,phone,place="Kadapa"):
    txt = "My name is {}. My phone number is {}. I am from {}."
    print(txt.format(name,phone, place))

profile("Bharath", 9874937390)



#Eg:2
def profile(name,phone,place="Kadapa"):
    txt = "My name is {}. My phone number is {}. I am from {}."
    print(txt.format(name,phone, place))

profile("Bharath", 9874937390,"Guntur")





# Eg:3
def profile(name,phone,place="KADAPA"):
    if place =="kadapa" or place =="KADAPA" or place =="kadapa":
        txt = "My name is {}. My phone number is {}. I am from {}."
        print(txt.format(name,phone, place))
    else:
        print("You are not eligible to Signup")

profile("Bharath", 9874937390)

# Exception
def profile(name,phone,place="KADAPA"): # error ---> coz defalut args should not follow
    # positional param
    if place =="kadapa" or place =="KADAPA" or place =="kadapa":
        txt = "My name is {}. My phone number is {}. I am from {}."
        print(txt.format(name,phone, place))
    else:
        print("You are not eligible to Signup")

profile("Bharath", 9874937390)

# variable length param
# ! Eg:1
# To pass more than 1arg to parameter means we use variable length args
# To convert normal to variable length param,add * to their prefix of param
# name ="sid", 'name2', 'name3'
def profile(*name):
    for val in name:
        print("My name is",val)
profile("sid", 'name2','name3')

# !Eg:2

def profile(*name,age):
    for val in name:
        print("My name is",val,"my age is", age)
#profile("sid", 'name2', 'name3',28)


def profile(age, *name):
    for val in name:
        print("My name is",val,"my age is",age)
profile(28,"sid", 'name2','name3')


# keyword variable length args
# kwargs ----> which is used to provide the args in the form
# ! Eg:1
def price(price_list):
    print(price_list)
#print(shirt=1000, iphone=80000)
n = 5
{1:1, 2:4, 3:9,4:16,5:25}

n = int(input("Enter the number:"))
d1 = {}
for val in range(1, n+1):
        d1[val] = val**2
print(d1)
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict1(5)


# ! ----> object oriented programming
# The paradigms of objects orinted programming are

# class
# objects
# inheritannce
# polymorphism
# abstraction
# encanpsulation

# ! class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# Eg:1
class c1:
    name1 = "sidhu"
    print(name1)

# ? Eg:2
class person:
    name = "sidhu"

c  = person()# c is object
# The process of creation of an object is clled as Instantiation
print(c.name)

# Method without parameter
# creation of a method
#When the function is created with a class is called as method
class person:
    def display(person):
        print("Hello Welcome to classes")

p = person()
p.display()


#? Eg:4
# ! Method with parameter
class person:
    def display(person,name,age):
        print(name, age)

p = person()
p.display("farid",21)


# ? Eg : 5
class person1:
    fname = "farid" #attribute of static variable
    lname = "T"

def first_name(self):
    print(person.fname)

def full_name(self):
    print(person.fname+" "+person.lname)
p = person1( )

# ?  Eg : 6
# constructors ----> ___init___( )
# This is a special method which has the ability to excute itself without
# calling if manullay through the process of instantiation

class profile:
    def __init___(self ): # constructor method
        print("hey")

p = profile( ) #execution of constructor throught this process














   


#d1 = {"a":100, "b":200, "c":300}
#d1 = dict(a=100, b=200, c=300)
#print(d1)












n =12















#Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’.
#The length of the string is variable. The task is to find the minimum number of ‘*’
#or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’
#and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
#Note : The output will be a positive or negative integer based on number of ‘*’
#and ‘#’ in the input string.

#(*>#): positive integer
#(#>*): negative integer
#(#=*): 0
#Example 1:
#Input 1:

###***   -> Value of S
#Output :

#0   → number of * and # are equal



   

