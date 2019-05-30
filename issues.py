#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Project...: Learning Python with Issues
# File Name.: issues.py
# Author....: dLight - Heleno A. Luz                            Date: 28/05/2019
#-------------------------------------------------------------------------------

import os


# ========================================================= General Informations
''' Issues references:
    - https://pynative.com/python-basic-exercise-for-beginners/
'''


# ======================================================== Global configurations
max_issue = 7


# ============================================================= Support Fuctions
def instructions(issue_number):
    if issue_number == 0:
        print("\n ######## Studying python 3 through issues. ######## ")
        print("\n Instructions:")
        print("\n ----> Max issue number = ", max_issue)
        print(" ----> Enter '0' (zero) to exit.")
        print(" ----> Enter 'cls' to clear the screen.")

    elif issue_number == 1:
        print("\n\t Issue 1: [ Multiply or Add ] Accept two int values from user and return their product. If the product is greater than 1.000, then return their sum.\n")

    elif issue_number == 2:
        print("\n\t Issue 2: [ Fibonacci number ] \n\t Receive a number indicating the term to be found in the Fibonacci Sequence.\n")

    elif issue_number == 3:
        print("\n\t Issue 3: Accept string from the user and display only those characters which are present at an even index.")

    elif issue_number == 4:
        print("\n\t Issue 4: Given a string and an int n, remove characters from string starting from zero upto n and return a new string.")

    elif issue_number == 5:
        print("\n\t Issue 5: Given a list of ints, return True if first and last number of a list is same.")
        print("\n\t Instructions:")
        print("\n\t ----> Press 'Enter' to next number")
        print("\t ----> Enter 'exit' to finish \n")

    elif issue_number == 6:
        print("\n\t Issue 6: Calculate the square root of an informed number.\n")
        print("\n\t Instructions:")
        print("\n\t ----> Press 'Enter' to next number")
        print("\t ----> Enter 'exit' to finish \n")

    elif issue_number == 7:
        print("\n\t Issue 7: Calculate the cubic root of an informed number.\n")
        print("\n\t Instructions:")
        print("\n\t ----> Press 'Enter' to next number")
        print("\t ----> Enter 'exit' to finish \n")


# ========================================================= Issues and Solutions


# ---------------------------------------------------------------------- Issue 1
def issue_1():
    instructions(1)

    def multiplyOrAdd(num1, num2):
        if( (num1 * num2) < 1000):
            print("\n\t ----> Product of the numbers.")
            return num1 * num2
        else:
            print("\n\t ----> Sum of numbers.")
            return num1 + num2

    while True:
        try:
            num1 = float(input("\t Enter the first number: "))
            break
        except:
            print("\n\t ---> The entered character is not valid.\n")

    while True:
        try:
            num2 = float(input("\t Enter the second number: "))
            result = multiplyOrAdd(num1, num2)
            print("\t The result is: ", result)
            break
        except:
            print("\n\t ---> The entered character is not valid.\n")


# ---------------------------------------------------------------------- Issue 2
def issue_2():
    instructions(2)

    def fibonacci(number):
        last = 1
        penult = 1

        if (number == 1) or (number == 2):
            print("1")
        else:
            count=3
            while count <= number:
                tern = last + penult
                penult = last
                last = tern
                count += 1
            print(tern)

    level = input("\t Enter the level Fibonacci term to search: ")
    print("\t Fibonacci number, level ", level, " = ", fibonacci(int(level)))


# ---------------------------------------------------------------------- Issue 3
def issue_3():
    instructions(3)

    def printEveIndexChar(str):
        for i in range(0, len(str)-1, 2):
            print("\t index[",i,"]", str[i] )
    inputStr = input("\t Enter String: ")
    print("\t Orginal String is ", inputStr)
    print("\t Printing only even index chars")
    printEveIndexChar(inputStr)


# ---------------------------------------------------------------------- Issue 4
def issue_4():
    instructions(4)

    def removeChars(str, n):
        return str[n:]

    print("\n\t Removing n number of chars.")
    texto = input("\t Enter a string: ")
    qtd = input("\t Enter a quantity to delete on string: ")
    print("\n\t Return: ", removeChars(texto, int(qtd)))


# ---------------------------------------------------------------------- Issue 5
def issue_5():
    instructions(5)

    def isFirstAndLastSame(numberList):
        firstElement = numberList[0]
        lastElement =  numberList[-1]
        if(firstElement == lastElement):
            return True
        else:
            return False
    numList = []


    while True:
        int_number = input("\t Enter a int number: ")

        if int_number == "exit": break
        try:
            int_number = int(int_number)
            numList.append(int_number)
        except:
            print("\n\t ---> The entered character is not valid.\n")


    print("\n\t The first and last number of a list is same.")
    print("\t Result is: ", isFirstAndLastSame(numList))
    print("\t The numbers is: ", numList[0], " and ", numList[-1])


# ---------------------------------------------------------------------- Isue 6
def issue_6():
    instructions(6)

    def squareRoot(number):
        # return math.sqrt(number)   ---------   (necessary import math)
        return number ** (1/2)

    while True:
        try:
            number = int(input("\t Enter the number: "))
            break
        except:
            print("\n\t ---> The entered character is not valid.\n")

    print("\n\t The Square Root is: ", squareRoot(int(number)))


# ---------------------------------------------------------------------- Isue 7
def issue_7():
    instructions(7)

    def cubiRoot(number):
        return number ** (1/3)

    while True:
        try:
            number = int(input("\t Enter the number: "))
            break
        except:
            print("\n\t ---> The entered character is not valid.\n")

    print("\n\t The Cubic Root is: ", cubicRoot(int(number)))


# =========================================================== Index of questions
def questions():

    study_question = True

    while study_question:
        instructions(0)

        issue_number = input("\n Enter the number of issue: ")

        if issue_number == "cls": os.system("clear")
        elif int(issue_number) == 0: study_question = False
        elif int(issue_number) == 1: issue_1()
        elif int(issue_number) == 2: issue_2()
        elif int(issue_number) == 3: issue_3()
        elif int(issue_number) == 4: issue_4()
        elif int(issue_number) == 5: issue_5()
        elif int(issue_number) == 6: issue_6()
        elif int(issue_number) == 7: issue_7()
        else: print("\n\t Issue not found!\n\t Max issue number = ", max_issue)

    print("\n\t ----> Studies of the issues concluded.\n")


# ------------------------------------------------------------------------- main
if __name__ == "__main__":
    questions()
