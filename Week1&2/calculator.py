#Johana
#Calculator
#June 20,2019

import math as m

def add(x, y):
    return x+y
def mult(x, y):
    return x*y
def sub(x, y):
    return x-y
def divd(x, y):
    return x/y

def simple():
    num1= int(input("Enter a Number: "))
    num2= int(input("Enter another Number: "))
    print(num1,"_",num2)
    choosesign= input("Chose a sign +,-,/, or * ")
    if choosesign=="+":
        print(num1," + ", num2, " = ", add(num1,num2))
    if choosesign=="-":
        print(num1," - ", num2, " = ", sub(num1,num2))
    if choosesign=="*":
        print(num1," * ", num2, " = ", mult(num1,num2))
    if choosesign=="/":
        print(num1," / ", num2, " = ", divd(num1,num2))
    input()

def Trig():
    num=int(input("Enter a Number: "))
    choosetrigsign= input("Choose a trig symbol cos, sin, or tan")
    if choosetrigsign=="cos":
        print(m.cos(num))
    if choosetrigsign=="sin":
        print(m.sin(num))
    if choosetrigsign=="tan":
        print(m.tan(num))
    input()    
simpleortrig= input("Do you want to simple math or trig? ")
if simpleortrig=="simple math":
    simple()
if simpleortrig=="trig":
    Trig()


