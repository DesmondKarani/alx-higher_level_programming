#!/usr/bin/python3
"""Module for Square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The id of the object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes."""
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, args):
                if attr == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                elif hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.width,  # width and height are the same for a square
            'x': self.x,
            'y': self.y
        }
