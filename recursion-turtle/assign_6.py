#millie mince 
#cs51a
#assignment 6
#october 11 2019
#extra credit: added color dots to the recursive h
#extra credit: made another recursive turtle function called target

from turtle import * 
from random import *

def concat_strings(l_strings):
    """function uses recursion to concatenate a list of strings into one string"""
    if l_strings == []:
        return ""
    else: 
        return l_strings[0] + " " + concat_strings(l_strings[1:])

def length(somelist):
    """function uses recursion to return the length of a list"""
    if somelist == []:
        return 0
    else:
        return 1 + length(somelist[1:])

def rec_count(somelist, value):
    """function uses recursion to count the number of occurences of a certain value in a list"""
    if len(somelist) == 0:
        return 0
    else:
        count = rec_count(somelist[1:], value)
        if value == somelist[0]:
            return count + 1
        else:
            return count

def remove_spaces(somestring):
    """function uses recursion to take an input string and return the string with no spaces"""
    if len(somestring) == 0:
        return ""
    else:
        if somestring[0] == " ":
            return remove_spaces(somestring[1:])
        else:
            return somestring[0] + str(remove_spaces(somestring[1:]))         

def recursive_h(x, y, l_vertical, level):
    """function draws a large h and then smaller h's off each end of the large h. It does this "level" amount of times (see input)"""
    penup()
    goto(x, y)
    pendown()
    forward(l_vertical)
    left(90)
    forward(l_vertical/2)
    right(180)
    forward(l_vertical)
    left(180)
    forward(l_vertical/2)
    left(90)
    forward(2*l_vertical)
    left(90)
    forward(l_vertical/2)
    right(180)
    forward(l_vertical)
    right(90)
    
    if level == 1:
        penup()
        goto(x, y)
        pendown()
        forward(l_vertical)
        left(90)
        forward(l_vertical/2)
        pencolor("red")
        dot()
        pencolor("black")
        right(180)
        forward(l_vertical)
        pencolor("yellow")
        dot()
        pencolor("black")
        left(180)
        forward(l_vertical/2)
        left(90)
        forward(2*l_vertical)
        left(90)
        forward(l_vertical/2)
        pencolor("blue")
        dot()
        pencolor("black")
        right(180)
        forward(l_vertical)
        pencolor("green")
        dot()
        pencolor("black")
        right(90)         
          
    else:
        recursive_h(x-l_vertical, y+l_vertical/2, l_vertical/2, level-1)
        recursive_h(x+l_vertical, y-l_vertical/2, l_vertical/2, level-1)
        recursive_h(x+l_vertical, y+l_vertical/2, l_vertical/2, level-1)
        recursive_h(x-l_vertical, y-l_vertical/2, l_vertical/2, level-1)
        
def square(l):
    """draws a square with lengths l"""
    for i in range(4):
        forward(l)
        left(90)
        
def stairs(x, y, length, blueness):
    """draws stairs by drawing squares on top of another until the length is less than 3. the function recursively draws more stairs at x, y+length and x+length, y until the length is less than 3."""
    color = (0, 0.5*blueness, blueness)
    if length>3:
        penup()
        goto(x, y)
        pendown()
        fillcolor(color)
        begin_fill()
        square(length)
        end_fill()
        stairs(x, y+length, length/2, blueness/1.25)
        stairs(x+length, y, length/2, blueness/1.25)
        
def target(x, y, radius):
    """function draws a target of circles within each other until the radius is less than 5. each circle has a random color to create a target."""
    color = (randint(0, 1), randint(0, 1), randint(0, 1))
    #generating random color
    if radius>5:
        penup()
        goto(x, y)
        pendown()
        fillcolor(color)
        begin_fill()
        circle(radius)
        end_fill()
        target(x, y+10, radius-10)
        
   
            