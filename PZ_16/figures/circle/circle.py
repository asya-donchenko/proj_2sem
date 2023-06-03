__all__ = ['circlePerimeter', 'circleArea']

from math import pi

defaultRadius = 5

def circlePerimeter(radius=defaultRadius):
    return radius*2 * pi

def circleArea(radius=defaultRadius):
    return radius**2 * pi