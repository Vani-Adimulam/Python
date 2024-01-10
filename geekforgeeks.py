# To calculate the area of circle
# def area(r):
#     PI = 3.14
#     print("The area of circle is:", (PI *(r ** 2)))
# area(3)
# area(5)


#To calculate prime numbers between the range
# lower = 45
# upper = 100
# print("Prime numbers between", lower, "and", upper, "are:")
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# a = 4
# b = 34
# c = abs(a-b)
# print(c)

#Sample prime number check code
# n = [1, 2, 3, 10, 5, 8]
# for i in n:
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break 
#         else:
#             print(i)

# TO calculate the given number is a prime number:
# num = int(input("Enter a number:"))
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(num ,"is not a prime number")
#             break
#     else:
#         print(num, "given number is a prime number")
# else:
#     print(num, "is not a prime number")


#To calculate fibonacci number
# def fibonacci(n):
#     if n <= 0:
#         print("Incorrect number")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(12))

    

#To calculate sum of array
# def _sum(arr):
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    # sum = 0
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    # for i in arr:
    #     sum = sum + i
    # return(sum)
# driver function
# arr = []
# input values to list
#arr = [12, 3, 4, 15]
# calculating length of array
#n = len(arr)
#ans = _sum(arr)
# display sum
#print('Sum of the array is ', ans)


#TO CALCULATE THE SUM OF ARRAY
# import math
# arr =[]
# arr =[1,3,5,6,6,7,8,7,9]
# ans = sum(arr)
# print("The sum of given array is", ans)


#TO CALCULATE THE LARGEST NUMBER IN THE ARRAY
# def largest_num(arr, n):
#     max = arr[0]
#     for i in range(1, n):
#         if arr[i] > max:
#             max = arr[i]
#     return max
# arr = []
# arr = [1, 4, 5, 6, 7, 7]
# n = len(arr)
# ans = largest_num(arr, n)
# print("the largest number is:", ans)


#TO CALCULATE THE MAX IN ARRRAY
# def large(arr, n):
#     ans = max(arr)
#     return ans
# arr = [1, 3, 5, 6 ,7, 123]
# n = len(arr)
# put = large(arr, n)
# print("the largest num is:", put)


#LISTS
#TO SWAP FIRST AND LAST ITEMS IN LIST
# def swaplist(newlist):
#     n = len(newlist)
#     temp = newlist[0]
#     newlist[0] = newlist[n-1]
#     newlist[n-1] = temp
#     return newlist
# newlist = [1, 4, 5, 6, 7, 3, 5, 3]
# print(swaplist(newlist))


#TO SWAP THE LIST
# def swaplist(llist):
#     llist[0], llist[-1] = llist[-1], llist[0]
#     return llist
# llist = [1, 5, 6, 3, 2, 6, 7, 8, 9]
# print(swaplist(llist))


#TO CONVERT THE NESTED LIST INTO LIST
# import itertools
# a = [[1, 2], [3, 4], [5, 6]]
# b = list(itertools.chain.from_iterable(a))
# print(b)



# Program to add two matrices
# using list comprehension
# x = [[1,2,3],
#      [3,4,5],
#      [2,4,5]]
# y = [[4,5,6],
#      [4,6,8],
#      [6,7,8]]
# result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
# for r in result:
#     print(r)


# Multiplication of two matrics using numpy
# import numpy
# A = [[1, 3, 4],
#      [3, 5, 6],
#      [4, 5, 6]]
# B = [[2, 4, 5],
#      [5, 6, 7],
#      [4, 6, 9]]
# result = numpy.dot(A,B)
# for r in result:
#     print(r)

#Addition of two matrices
# import numpy
# A = [[1, 3, 4],
#      [3, 5, 6],
#      [4, 5, 6]]
# B = [[2, 4, 5],
#      [5, 6, 7],
#      [4, 6, 9]]
# ans = numpy.add(A,B)
# for r in ans:
#     print(r)


# To count the length of list
# my_list = [3, 4, 5, 6, 7, 8]
# my_list2n = len(my_list)
# print(my_list2n)


#PROGRAM TO FIND SUM OF TWO NUMBERS
# def sumoftwonumbers(n1, n2):
#     sum = n1 + n2
#     print("sum of two numbers is:", sum)
# sumoftwonumbers(2, 3)

#TO FIND THE SQAREROOT
# num = int(input("enter number:"))
# sqare = (num ** 2)
# print("The sqare root of given number is:", sqare)


#TO CALCULATE THE QUADRATIC EXPERSSIONS
# import cmath
# a = 1
# b = 6
# c = 9
# d = (b**2)-(4*a*c)
# sol1 = (-b-cmath.sqrt(d))/2*a
# sol2 = (-b+cmath.sqrt(d))/2*a
# print("The roots are", sol1, "and", sol2)


#TO SWAP THE VARIABLES
# x = 5
# y = 6
# x, y = y, x
# print("The value of x after swap is", x)
# print("The value of y after swap is", y)


#TO IMPORT A RANDOM NUMBER
# import random
# x = random.randint(0, 9)
# print(x)


#TO CONVERT KILOMETERS INTO MILES
# kilo = float(input("Enter kilos:"))
# conv_fact = 0.621371
# miles = kilo * conv_fact
# print("%0.2f kilometers is equal to %0.2f miles" %(kilo, miles))


#to convert celsius into faranheat
# celsius = float(input("Enter the temparature:"))
# fahrenheit = (celsius * 1.8 ) + 32
# print("%0.1f degree celsius temparature is equal to %0.1f fahrenheit."%(celsius, fahrenheit))


#TO CALCULATE A NUMBER IS POSITIVE OR NEGATIVE OR 0
# num = int(input("Enter a number:"))
# if num > 0:
#     print("Number is positive")
# elif num < 0:
#     print("Number is negative")
# else:
#     print("Number is 0")


#TO CALCULATE A NUMBER IS EVEN OR ODD
# num = int(input("Enter a number:"))
# if (num % 2) == 0:
#     print("Number is even")
# else:
#     print("Number is odd")


#TO CALCULATE THE GIVEN YEAR IS A LEAP YEAR OR NOT
# year = int(input("ENter the year:-"))
# if (year % 400 == 0) or (year % 100 == 0):
#     print("THis is a leap year")
# elif (year % 4 == 0):
#     print("this ia leap year")
# else:
#     print("This is not a leap year")


#TO CALCULATE THE LARGEST AMONG THREE NUMBERS:
# a = int(input("enter first number:"))
# b = int(input("enter second number: "))
# c = int(input("enter third number:"))
# if (a > b) and (a > c):
#     print("The largest number is:", a)
# elif(b > a) and (b > c):
#     print("The largest number is :", b)
# else:
#     print("The largest number is :", c)


#TO CHECK NUMBER IS A PRIME OR NOT:
# num = int(input("Enter a number:"))
# if num > 1:
#     for i in range(2, num):
#         if (num % i == 0):
#             print("Number is not prime")
#             break
#     else:
#         print("Number is prime")
# else:
#     print("Number is not prime")


#TO CONVERT BYTES TO A STRING
# print(b'easy'.decode("utf-8"))


#To calculate the prime numbers between range:
# lower = int(input("Enter a number:-"))
# upper = int(input("Enter a numner:-"))
# print("The prime numbers between ", lower, "and", upper ,"are:")
# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i == 0):
#                 break
#         else:
#             print(num)


#TO CALCULATE THE NUMBERS DEVIDED BY ANOTHER NUMBER:
# my_list = [23, 24, 26, 28, 45]
# for i in my_list:
#     if i % 12 == 0:
#         print(i)
# else:
#     print("no numbers devided by 34")


#To convert decimal into binary, octal, hexadecimal:-




#TO GET THE ASCII VALUE OF A CHARACTER:-
# char = "%"
# print("The ascii conversion of is", ord(char))

#TO CALCULATE THE HCF OF TWO NUMBERS:-
# def compute_hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
# num1 = 54
# num2 = 24
# print("The hcf of given two numbers is:",compute_hcf(num1, num2))


#TO DISPLAY A MULTIPLICATION TABLE
# num = 12
# for i in range(1, 13):
#     print("12" ,'X', i, '=', num * i)


#TO CALCULATE THE LCM OF TWO NUMBERS:-
# def compute_lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while(True):
#         if ((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break 
#         greater += 1 
#     return lcm
# x = 2
# y = 12
# print("The lcm of two numbers is:", compute_lcm(x, y))


#PYTHON PROGRAM TO PRINT A CALANDER
# import calendar
# yy = 2022
# mm = 12
# print(calendar.month(yy, mm))


#PYTHON PROGRAM FOR RECURSION
# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
# tri_recursion(9)


#TO ADD DUPLICATE ITEMS IN SEPARATE LIST:
# reglist = []
# duplilist = []
# l1 = [2,2,3,4,5,3,5,6,7,8,9,1]
# for i in l1:
#     if i not in reglist:
#         reglist.append(i)
#     elif i not in duplilist:
#             duplilist.append(i)
# print(duplilist)


# OOPS in python:-
# -- Python is a object-orienteed programming language that uses objects and classes in programming.
# It aims to implement Inheritence, Polymorphism, Encapsulation..., in Programming.
# Main concepts of object-oriented programming are Classes, Objects, Polymorphism, Encapsulation, Inheritence, Data Abstraction.

# CLASS:-
# -- A class is a collection of objects. A class contains blueprints from where the objects are being created.
# Class Dog:
#    pass

# OBJECT:- 
# -- Object is an entity that has behaviour and state associated with it. It may be like Mouse, Pen, string, interger.
# obj = Dog()

# KEY WORDS IN OOPS:-
# SELF:- 
# -- The self parameter is a reference to the current instance  of the class, which is used to access variables the belongs to the class.

# "__init__":- 
# -- It is a reserved method in python class. It is called as a constructor in object oreiented programming. This method called when an obkect is created from the class and it allows the class to initialize the attributes of a class.
# class Dog():
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("My dog name is:".format(self.name))
# Rodger = Dog("Rodger")
# Rodger.speak()

# Inheritance:-
# -- Inheritance is a capability of one class to derive its properties from another class.The class thar derives properties are called derived class or child classes from which properties are being derived are called parent class.
# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#     def details(self):
#         print("My name is: {}".format(self.name))
#         print("My idnumber is: {}".format(self.idnumber))
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#         Person.__init__(self, name, idnumber)
#     def details(self):
#         print("Salary is: {}".format(self.salary))
#         print("The post is: {}".format(self.post))
# a1 = Employee('vani', 3456, 3456667, "Developer")
# a1.display()
# a1.details()

# POLYMORPHISM:-
# -- Polymorphism simply means having many forms. Simply we can define the ability of a message to display in different forms.For example, the person can have different characters at the sametime.
# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#     def flight(self):
#         print("Some birds can fly some birds can't fly.")
# class Sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly")
# class Ostrich(Bird):
#     def flight(self):
#         print("Ostrich can't fly")
# bb = Bird()
# bb1 = Sparrow()
# bb2 = Ostrich()
# bb.intro()
# bb.flight()
# bb1.flight()
# bb2.flight()

# ENCAPSULATION:-
# --Encapusulation is a fundamental topic in oops. It describes the idea of wrapping data and methods that work on data within the one unit.
# *-- A class is an example of encapsulation as it encapusltes the functions and variables.
#  Advantages of encapsulation:- Security, Datahiding, Simplicity.

#Examples of OOPs:

# class Flashcard: 
#     def __init__(self, word, meaning):
#         self.word = word 
#         self.meaning = meaning 
#     def __str__(self):
#         return self.word+' ( '+self.meaning+')'
# flash = []
# print("Welcome to flash card application")
# while(True):
#     word = input("Enter the word you want to enter: ")
#     meaning = input("Enter the meaning you want to enter: ")

#     flash.append(Flashcard(word, meaning))
#     opinion = int(input("Enter 0 if you want to continue or 1 if you want to  exit: "))

#     if opinion == 0:
#         continue
#     else:
#         break
# print("/nYour flashcards: ")
# for i in flash:
#     print("* ", i)

# ex-2:-
# import random
# class flashcard:
#     def __init__(self):
#         self.fruits={'apple':'red',
#                      'banana':'yellow',
#                      'watermelon':'green',
#                      'orange':'orange',
#                      'mango':'green'}
#     def quiz(self):
#         while (True):
#             fruit, color = random.choice(list(self.fruits.items()))

#             print("What is the color of {} ".format(fruit))
#             user_answer = input()

#             if (user_answer.lower == color):
#                 print("Correct answer")

#             else:
#                 print("Wrong answer")

#             option = int(input("Enter 0 if you want to continue enter 1 if you want to quit: "))
#             if (option == 0):
#                 break
# print("The fruit quiz is: ")
# fc=flashcard()
# fc.quiz()


# # To have a count of instances
# class geeks:
#     conuter = 0
#     def __init__(self):
#         geeks.conuter += 1
# g1 = geeks()
# g2 = geeks()
# g3 = geeks()
# print(geeks.conuter)


# To calculate area of circle, rectangle
# class Circle:
#     pi = 3.17

#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculate_area(self):
#         print("The area of circle is", self.pi * self.radius * self.radius)

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def calculate_area(self):
#         print("The area of rectangle is: ", self.length * self.width)
# def area(shape):
#     shape.calculate_area()
# cir = Circle(5)
# rect = Rectangle(10, 5)

# area(cir)
# area(rect)


# Example on inheritence
# class Vehicle:
#     def __init__(self, name , color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#     def details(self):
#         print(self.name, self.color, self.price)
# class Car(Vehicle):
#     def change_gear(self, no):
#         print("The car name is ", self.name, "change gear to: ", no)
# car = Car("Roolsroyce", "white" , 2345678)
# car.details()
# car.change_gear(5)


# Short hand if statement
# print(True) if 10 > 12 else print(False)

# a1 = input("Enter value: ")
# a = int(a1)
# row = (a * "* ")
# counter = 0
# while counter < a:
#     print(row)
#     counter = counter + 1
# print("End")


# While loop:-
# counter = 0
# while counter < 3:
#     counter += 1
#     print(counter)

# count = 0
# while count < 4:
#     count += 1
#     print("Haii Vani")

# l = [1, 2, 3, 4, 5]
# while l:
#     print(l[1])


# While loop to miss some letters in a string
# i = 0
# a = "Geeks for geeks"
# while i < len(a):
#     if a[i] == "k":
#         i += 1
#         print("letter is : ", a[i-1])
#         continue 
#     print("Current letter is: ", a[i])
#     i += 1


# i = 0
# a = "My name is Vani"
# while i < len(a):
#     if a[i] == "s" or a[i] == "i":
#         i += 1
#         break
#     print("Current letter is: ", a[i])
#     i += 1


# To use a pass statement
# a = "my name is vani"
# i = 0
# while i < len(a):
#     i += 1 
#     pass
# print("The no.of letters are: ", i)


# to use else in while loop
# i = 0
# while i < 3:
#     i += 1
#     print(i)
# else:
#     print("No Break")
# i = 0
# while i < 2:
#     i += 1
#     print(i)
#     break
# else:
#     print("Has a Break")

#Sentinel controlled statements
# a = int(input("Enter a number from -1 to quit: "))
# while a != -1:
#     print("The entered number is: ", a)


# Recursion function:
# def recursion(n):
#     if n<=1:
#         return n 
#     else:
#         return ((n-1)+(n-2))
# n = int(input())
# if n<=0:
#     print("Invalid inpput")
# else:
#     print("Given fibonacii number is", n)
# i = 0
# for i in range(n):
#     print(recursion(i))
#     i = i+1

# def recursive_factorial(n):
#   if n == 1:
#       return n
#   else:
#       return n * recursive_factorial(n-1)
 
# # user input
# num = 6

 
# check if the input is valid or not
# if num < 0:
#   print("Invalid input ! Please enter a positive number.")
# elif num == 0:
#   print("Factorial of number 0 is 1")
# else:
#   print("Factorial of number", num, "=", recursive_factorial(num))

#matplotlib 
# import matplotlib.pyplot as plt 
# import numpy as np 
# x = np.array([10, 30, 50, 10])
# mylabels = ["banana", "Apple", "MNango", "Strawberry"]
# plt.pie(x, labels = mylabels)
# plt.legend()
# plt.show()



# How to product the list with out duplicates
# l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7]
# s = []
# for i in l:
#   if i not in s:
#     s.append(i)
# print(s)
# pro = 1
# for j in s:
#   pro = pro * j 
# print(pro)


# To get numbers with frequency greater than k
# l = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# s = []
# m = []
# for i in l:
#   if i not in s:
#     s.append(i)
# for k in s:
#   count = 0 
#   for j in l:
#     if k == j:
#       count = count + 1 
#   if count > 2:
#     m.append(k)
# print(m)


# a = "vani"
# b = "madhu"
# c = "swetha"
# d = "This is me {} , This is my brother {}, This is my bff {}"
# print(d.format(a, b, c))

# l = ["fsfs", "fdsfsf", "dvff", "yhyjhju"]
# n = [x for x in l if "f" in x]
# print(n)

# while True:
#     a = input("Enter a value: ")
#     print(a)
#     if a == "-1":
#         break

# def rec(n):
#     if n == 0:
#         result = 0
#     else:
#         result = (n) + rec(n-1)
#     return result 
# print(rec(4))

# def gen_2_comb(words):
#     words = sorted(words)
#     items = list(range(len(words)))
#     combinations_1 = []
#     for item in items:
#         combinations_1.append([item])
#     combinations_2 = []
#     for combination in combinations_1:
#         for item in items:
#             if item > combination[-1]:
#                 combinations_2.append(combination + [item])
#     word_combinations = []
#     for combination in combinations_2:
#         word_combination = []
#         for index in combination:
#             word_combination.append(words[index])
#         word_combinations.append(tuple(word_combination))
#     return sorted(set(word_combinations))
# words = input("Enter: ").split()
# all_combinations = gen_2_comb(words)
# for combination in all_combinations:
#     print(' '.join(combination))



# from collections import Counter
# l = [1, 2, 3, 4, 4, 5, 6, 2, 3, 4, 5, 2]
# n = (Counter(l).values())
# print(n)


# import math 
# def product(list):
#     s = set(list)
#     return (math.prod(s))
# l = [1, 2, 4, 5, 2, 7]
# print(product(l))


# l = [1, 2, 3]
# for i in l:
#     for j in l:
#         for k in l:
#             if i != j and j != k and k != i:
#                 print(str(i) + " " + str(j) + " " + str(k))


# from itertools import permutations
# c = permutations(["Sasi", "Vani", "ramani"], 2)
# for i in c:
#     print(i)


# from itertools import combinations
# l = ["vani", [2, 3], "ssai", 0]
# s = combinations(l, 2)
# for i in list(s):
#     print(i)

# from itertools import combinations_with_replacement
# l = [1, 2, 'vani', 5, [4, 5]]
# s = combinations_with_replacement(l, 3)
# for i in s:
#     print(i)


# import itertools 
# l = [1, 2, 3]
# for i in itertools.count(5, 5):
#     if i == 35:
#         break 
#     else:
#         print(i, end=" ")


# import itertools 
# count = 0 
# for i in itertools.cycle('AB'):
#     if count > 7:
#         break
#     else:
#         print(i, end=" ")
#         count += 1


# import itertools 
# print(list(itertools.repeat(25, 4)))


# def vishaka():
#     v = {1:"Suri", 2.0:"vani", 2:"swe"}
#     return v[2.0]
# print(vishaka())

# from itertools import combinations_with_replacement
# b = [2, 3, 4, 5]
# s = combinations_with_replacement(b, 4)
# for i in s:
#     print(i)


#python itertools:- Types
# Infinite iterators
# Combinatoric iterators
# Terminating iterators
# * Infinite iterators:- Iterator in Python is any Python type that can be used with a ‘for in loop’. Python lists, tuples, dictionaries, and sets are all examples of inbuilt iterators. But it is not necessary that an iterator object has to exhaust, sometimes it can be infinite. Such types of iterators are known as Infinite iterators.
# eg:- count(start, step)
# import itertools
# for i in itertools.count(5, 5):
#     if i == 35:
#         break 
#     else:
#         print(i, end=" ")
# cycle(iterable):- This iterator prints all values in order from the passed container. It restarts printing from the beginning again when all elements are printed in a cyclic manner.
# eg:- 
# import itertools
# c = 0 
# for i in itertools.cycle('AB'):
#     if c > 7:
#         break 
#     else:
#         print(i, end = " ")
#     c += 1
# repeat(val, num):- This iterator repeatedly prints the passed value an infinite number of times. If the optional keyword num is mentioned, then it repeatedly prints num number of times.
# import itertools 
# print(list(itertools.repeat(30, 6)))
# combinatoric iterators:-The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, and Cartesian products are called combinatoric iterators.
# types:-
# Product():-This tool computes the cartesian product of input iterables. To compute the product of an iterable with itself, we use the optional repeat keyword argument to specify the number of repetitions. The output of this function is tuples in sorted order.
#eg:- 
# from itertools import product 
# print(list(product([1, 2], repeat = 3)))
# from itertools import product 
# print(list(product(['vani', 'swetha', 'ram'], '2')))

# from itertools import combinations_with_replacement 
# l = [1, 2, 3, 4, 45]
# v = list(combinations_with_replacement(l, 2))
# print(v)

# from itertools import combinations
# l = [2, 4, [5, 6], 6, 7, 6]
# v = list(combinations(l, 3))
# print(v)

# from itertools import pairwise
# l = [1, 2, 3, 4]
# v = list(pairwise(l))
# print(v)

# from itertools import count 
# counter = count()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# To zip a list
# a = ("vami", "ajdn", "swe")
# b = ("dfa", "fvfv", "gfdv")
# x = dict(zip(a, b))
# for i in x:
#     print(i)


# from itertools import count

# counter = count()
# data = [1, 2, 3, 4]
# daily = list(zip(counter, data))
# print(list(daily))

# import itertools 
# data = [1, 2, 3, 4, 5]
# daily = list(itertools.zip_longest(range(10), data))
# print(daily)

# import itertools 
# start = itertools.starmap(pow, [(0, 2), (5, 6)])
# print(list(start))

# import itertools 
# a = [1, 2, 3, 4]
# b = ['a', 'b', 'c', 'd']
# c = ['vani', 'madhu', 'maggi', 'swetha']
# # s = itertools.combinations_with_replacement(a, 4)
# # for i in s:
# #     print(i)
# # # c = zip(a, b, c)
# # print(list(c))

# # Chain function in itertools allow us to chain together iterables
# o = list(itertools.islice(range(9), 2, 8, 2))
# print(o)

# condition = True
# x = 1 if condition else 0 
# print(x)

# v = ['vani', 'madhu', 'lallie', 'swetha']
# d = enumerate(v)
# t = []
# for index, name in d:
#     t.append(index)
# print(t)

# a, b, *c = (1, 2, 3, 5, 6)
# print(a)
# print(b)
# print(c)

# from collections import Counter
# a = 'sddfsddfgthujjcvbn'
# my = Counter(a)
# l = []
# m = []
# for key, value in my.items():
#     l.append(key)
#     m.append(value)
# print(l)
# print(m)
# print(my)
# # print(my.most_common(4)[0][0])
# print(list(my.elements()))


# a = [1, 2, 3, 4, 5]
# b = [i*i for i in a]
# print(a)
# print(b)


# import sys
# m = [1, 2, 3]
# print(sys.getsizeof(m))

# v = """ hii
#  everyone"""
# print(v)

# m = 'vabi'
# print(m.count('b'))

# from itertools import permutations
# a = [1, 2, 3, 4]
# b = permutations(a)
# print(list(b))

# from itertools import product
# a = [1, 2, 3]
# b = product(a, repeat=3)
# print(list(b))

# from itertools import combinations_with_replacement, permutations
# a = [1, 2, 4, 5, 6, 7, 3, 4]
# b = combinations_with_replacement(a, 2)
# c = permutations(a, 2)
# print(list(c))
# print(list(b))

# from itertools import accumulate
# a = [1, 2, 3, 4]
# b = accumulate(a)
# c = list(b)
# print(c)

# fib = [0, 1]
# for i in range(5):
#     fib.append(fib[-2] + fib[-1])
# print(",".join(str(e)for e in fib))

# v = "vanivanivanivani"
# print(v.count("v"))


# a = [1, 2, 3, 4, 3, 2, 1]
# a.sort(reverse=True)
# print(a)

# import numpy as np 
# l = [1, 2, 3, 4, 5]
# m = [2, 4, 5, 6]
# k = np.array([[[1, 2, 2], [3, 4, 5]], [[1, 2, 3], [5, 6, 7]]])
# e = np.concatenate((l, m))
# print(e)
# print(arr[0] + arr[3])
# print(arr)
# print(np.__version__)



# l = 20
# m = 50 
# for i in range(l, m+1):
#     if i > 1:
#         for j in range(2, i):
#             if (i%j) == 0:
#                 break 
#         else:
#             print(i)

# l = [1, 2, 2, 3, 4, 4, 5, 5]
# k = []
# m = []
# for i in l:
#     if i not in k:
#         k.append(i)
#     elif i in k:
#         m.append(i)
# print(k)
# print(m)

# l = "madaM"
# k = l.lower()
# j = k[::-1]
# if k == j:
#     print("It is a palindrome")
# else:
#     print("Not a palindrome")

# a = 1 
# b = 1000 
# l = []
# for i in range(a, b+1):
#     for j in range(2, int(i/2)+1):
#         if i % j == 0:
#             break 
#     else:
#         l.append(i)
# for j in l:
#     r = str(j)
#     if r[-1] == "9":
#         print(j)

# len() :- This function returns the length of list.
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
# print(len(List)) Output: 10

# min() :- This function returns the minimum element of list.
# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
# print(min(List)) Output: 1.054

# max() :- This function returns the maximum element of list.
# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
# print(max(List)) Output: 5.33

# index(ele, beg, end) :- This function returns the index of first occurrence of element after beg and before end. 

# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
# print(List.index(2)) Output: 1

# count() :- This function counts the number of occurrences of elements in list.
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
# print(List.count(1)) Output: 4

# del[a : b] :- This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
# # using del to delete elements from pos. 2 to 5 
# # deletes 3,5,4 
# del lis[2 : 5] 

# pop() :- This method deletes the element at the position mentioned in its arguments.
# # using pop() to delete element at pos 2 
# # deletes 3 
# lis.pop(2) 

# insert(a, x) :- This function inserts an element at the position mentioned in its arguments. 
# It takes 2 arguments, position and element to be added at respective position.
# # using insert() to insert 4 at 3rd pos 
# lis.insert(3, 4) 

# remove() :- This function is used to delete the first occurrence of number mentioned in its arguments.
# # using remove() to remove first occurrence of 3 
# # removes 3 at pos 2 
# lis.remove(3) 

# sort() :- This function sorts the list in increasing order.
# # using sort() to sort the list 
# lis.sort() 

# reverse() :- This function reverses the elements of list.
# # using reverse() to reverse the list 
# lis.reverse() 

# extend(b) :- This function is used to extend the list with the elements
# present in another list. This function takes another list as its argument.
# # using extend() to add elements of lis2 in lis1 
# lis1.extend(lis2) 

# clear() :- This function is used to erase all the elements of list. After this operation, list becomes empty.
# # using clear() to delete all lis1 contents 
# lis1.clear() 


# a = [9, 2, 3, 9, 0, 6, 8]
# a.sort()
# k = ' vani 67 7 RamaniAdm '
# # for i in k:
# #     if i.isspace():
# #         print('yes')
# a.append(5)
# print(a.remove(0))
# print(a.append(0))


# user_str = input('Enter a string with words: ')
# words = user_str.split()
# words_result = []
# words_adjacent =[]
# for i in range(len(words)-1):
#     words_adjacent.append(sorted([words[i],words[i+1]]))
# for i in range(len(words)):
#     for j in range(i+2,len(words)):
#         word = sorted([words[i],words[j]])
#         if word not in words_result and word not in words_adjacent :
#             words_result.append(word)
# if words_result:
#     for item in sorted(words_result):
#         print(*item)
# else:
#     print("No Combinations")

# def bubble_sort(arr):
#     n = len(arr)

#     # Traverse through all array elements
#     for i in range(n):
#         # Last i elements are already in place, so we don't need to check them
#         for j in range(0, n-i-1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Example Usage
# my_array = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(my_array)

# print("Sorted array:", my_array)


# import numpy 
# a = numpy.full((3, 4), 3)
# print(a)

# def fibonacci(n):
#     if n <= 0:
#         print("This is not a correct number")
#     series = [0, 1]
#     for i in range(2, n+1):
#         num = series[-1] + series[-2]
#         series.append(num)
#     return series 
# print(fibonacci(6))

# import pandas as pd 
# panda = {
# 	"calories": [2, 3, 4],
#     "Duration": [3, 4, 5]
# }
# ad = pd.DataFrame(panda, index=["day1", "day2", "day3"]) 
# print(ad.loc["day2"])

# import pandas as pd 
# df = pd.read_csv('data.csv')
# print(df.to_string())


# import pandas as pd
# df = pd.read_json('data.json')
# print(df.to_string()) 


# import matplotlib.pyplot as plt 
# import numpy as np 

# x = np.array([34, 56, 78])
# y = np.array([4, 5, 6])

# plt.plot(x, y, mec="r")

# plt.title("Map")
# plt.xlabel("Numbers")
# plt.ylabel("Readings")

# plt.grid(axis="x")
# plt.show()


# class Dog:
#     sound = "bark"

# a1 = Dog()
# print(a1.sound)




k = "vani"

for i in k:
    if i =="v":
        print("yes")












































