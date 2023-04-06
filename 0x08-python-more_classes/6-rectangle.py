#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """define variables and methods"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if isinstance(value, int) and value >= 0:
            self.__height = value
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """define area method, evaluate rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """define perimeter method, evaluate rectangle perimeter"""
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        define special __str__ method for printing a rectangle
        when print(self) is called
        """
        pattern = ''
        if self.__width is 0 or self.__height is 0:
            return pattern
        else:
            for j in range(self.__height):
                for i in range(self.__width):
                    pattern += '#'
                if j is not (self.__height - 1):
                    pattern += '\n'
            return pattern

    def __repr__(self):
        """
        define special __repr__ method for printing a rectangle
        when eval(self) is called
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        define __del__ method for printing a delete message prior to delete
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
