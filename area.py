# -*- coding: utf-8 -*-
"""
This module calculates areas of different shapes such as square, circles, triangle
trapezium

@author: JOSEPH
"""
import math


def square(a):
    """ This calculates area of the the square"""
    return a*a

def circle(r):
    """ This calculates the area of a circle"""
    return math.pi*r*r

def triangle(b,h):
    """ this calculates the area of a triangle"""
    return 1/2*b*h

def  trapezium(a,b,h):
    """this function calculates the area """
    return 1/2*(a+b)*h

def rectangle(l,w):
    """ This calculates the area of a a rectangle"""
    return l*w