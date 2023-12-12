#!/usr/bin/python3
""" This module defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle, inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the rectangle's position.
        - y (int): The y-coordinate of the rectangle's position.
        - id: An optional identifier for the rectangle.

        Attributes:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): x-coordinate of the rectangle's position.
        - y (int): y-coordinate of the rectangle's position.
        - id: Identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
        - value (int): The new width value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is not greater than 0.

        Notes:
        - Private attribute __width is used.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
        - value (int): The new height value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is not greater than 0.

        Notes:
        - Private attribute __height is used.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle's position.

        Returns:
        int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle's position.

        Args:
        - value (int): The new x-coordinate value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.

        Notes:
        - Private attribute __x is used.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle's position.

        Returns:
        int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle's position.

        Args:
        - value (int): The new y-coordinate value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.

        Notes:
        - Private attribute __y is used.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle with '#' characters.

        Notes:
        - Spaces are added based on the x-coordinate.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        str: A formatted string representing the rectangle,
        including its id, position, and dimensions.
        """
        return f"[Rectangle] \
            ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle based on provided arguments.

        Args:
        - *args: Variable-length argument list (no-keyworded arguments).
            1st argument: id
            2nd argument: width
            3rd argument: height
            4th argument: x
            5th argument: y
        - **kwargs: Variable-length keyworded argument
        list (key-worded arguments).
            Each key represents an attribute to update.

        Notes:
        - If *args exists and is not empty, **kwargs is skipped.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
        dict: A dictionary containing the id, x, width, y,
        and height attributes of the rectangle.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'width': self.width, 'height': self.height}
