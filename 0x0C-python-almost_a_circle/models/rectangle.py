#!/usr/bin/python3
""" Rectangle Module """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """ Integer validator method """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(name + " must be > 0")
        if (name == "x" or name == "y") and value < 0:
            raise ValueError(name + " must be >= 0")

    def area(self):
        """ Area method """
        return self.width * self.height

    def display(self):
        """ Display method """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ Str method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update method"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])
                else:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """ To dictionary method """
        return {
            'x': self.x,
            'width': self.width,
            'id': self.id,
            'height': self.height,
            'y': self.y
        }
