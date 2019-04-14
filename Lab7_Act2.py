# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Alex Villa
#       Jacob Tovar
#       Ricardo Trujillo
# Section: 514
# Assignment: Lab7_Act2
# Date: 10 March 2019
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:10:12 2019

@author: Ricardo, Alex, Jacob
"""
#This program allows the user to input the score a golfer got on his first 2 holes and their name. After this the program will find the median an output whether or not they made the cut.
First=[] #creating empty lists
Second=[]
Golf=[]
Count=1
List=[]
Dictionary={}
print("Please enter the first round score (enter a negative number when done) for Golfer #", Count)
FirstRound=int(input())
while FirstRound > 0:
    print("Please enter the second round score for Golfer #", Count)
    SecondRound=int(input())
    print("Please enter the name for Golfer #", Count)
    Golfer=input()
   
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #prints out all user inputted information
    print("First Round Score = ", FirstRound)
    print("Second Round Score = ", SecondRound)
    print("Name of golfer is: ", Golfer)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    Total=FirstRound+SecondRound
    List.append(Total) #adds total of each set of 2 rounds into 'List'
    Dictionary[Total]=Golfer #equals total strokes with user inputted names
    Count = Count + 1 #allows loop to continue onto the second golfer
    print("")
    print("Please enter the first round score (enter a negative number when done) for Golfer #", Count) #repeats until given a - number
    FirstRound=int(input())
    
List.sort() #sorts out all numbers
number=len(List)    #gives total length of List
if len(List)%2 == 0 : #checking if List is even
    median1 = List[number//2]
    median2 = List[number//2-1]
    median = (median1 + median2)/2
    print("")
    print("The median is: ", median)
else: #if List is odd it goes through here
    median = List[number//2]
    print("")
    print("The median is", median)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in Dictionary: #checks each total to see if its less than the median
    if i < median:
        print(Dictionary.get(i), " made the cut")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in Dictionary: #checks each total to see if its greater than or equal to the median
    if i >= median:
        print(Dictionary.get(i), "did NOT make the cut")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
