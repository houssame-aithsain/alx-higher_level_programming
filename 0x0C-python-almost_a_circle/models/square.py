#!/usr/bin/python3
""" Square Module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Str method """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter """
        self.integer_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update method """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ To dictionary method """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
