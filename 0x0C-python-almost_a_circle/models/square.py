#!/usr/bin/python3
""" """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ """
    def __init__(self, size, x=0, y=0, id=None):
        """ """
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """ """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ """
        return self.width

    @size.setter
    def size(self, value):
        """ """
        if not isinstance(value, int):
                raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ """
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
        """ """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
