#!/usr/bin/python3
""" module to import"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
        - size (int): The size of the square.
        - x (int): The x-coordinate of the square's position.
        - y (int): The y-coordinate of the square's position.
        - id: An optional identifier for the square.

        Attributes:
        - width (int): Width of the square (inherited from Rectangle).
        - height (int): Height of the square (inherited from Rectangle).
        - x (int): x-coordinate of the square's position.
        - y (int): y-coordinate of the square's position.
        - id: Identifier for the square.
        """
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        str: A formatted string representing the square,
        including its id, position, and size.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
        - value (int): The new size value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is not greater than 0.

        Notes:
        - Updates both width and height attributes.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square based on provided arguments.

        Args:
        - *args: Variable-length argument list (no-keyworded arguments).
            1st argument: id
            2nd argument: size
            3rd argument: x
            4th argument: y
        - **kwargs: Variable-length keyworded
        argument list (key-worded arguments).
            Each key represents an attribute to update.

        Notes:
        - If *args exists and is not empty, **kwargs is skipped.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
        dict: A dictionary containing the id,
        x, size, and y attributes of the square.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
