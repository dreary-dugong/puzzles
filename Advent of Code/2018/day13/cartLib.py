
class Cart(object):
    SYMBOLS = ("<", ">", "^", "v")
    _INTERSECTION_ORDER_ = ("left", "straight", "right")
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        
        if self.symbol == "<":
            self.direction = "left"
        elif self.symbol == ">":
            self.direction = "right"
        elif self.symbol == "v":
            self.direction = "down"
        else:
            self.direction = "up"

        self.intersectionCounter = 0


class Track(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Horizontal(Track):
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.symbol = "-"
    @staticmethod
    def move(cart):
        if cart.direction == "right":
            cart.x += 1
        else:
            cart.x -= 1
        

class Vertical(Track):
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.symbol = "|"
    @staticmethod
    def move(cart):
        if cart.direction == "up":
            self.y -= 1
        else:
            self.y += 1
        

class Intersection(Track):
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.symbol = "+"
    @staticmethod
    def move(cart):
        intersectionMove = cart.INTERSECTION_ORDER[cart.intersectionCounter]
        if intersectionMove == "left":
            cart.direction = "left"
            Horizontal.move(cart)
        elif intersectionMove == "right":
            cart.direction = "right"
            Horizontal.move(cart)
        else:
            Vertical.move(cart)
        cart.intersectionCounter += 1
        if cart.intersectionCounter > 2:
            cart.intersectionCounter = 0

class Corner(Track):
    def __init__(self, x, y):
        super().__init__(self, x, y)

class LeftDown(Corner):
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.symbol = "\\"
    @staticmethod
    def move(cart):
        if cart.direction == "right":
            cart.direction = "down"
            cart.y += 1
        else:
            cart.direction = "left"
            cart.x -= 1

class RightUp(Corner):
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.symbol = "\\"
    @staticmethod
    def move(cart):
        if cart.direction == "left":
            cart.direction = "up"
            cart.y -= 1
        else:
            cart.direction = "right"
            cart.x += 1

class LeftUp(Corner):
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.symbol = "/"
    @staticmethod
    def move(cart):
        if cart.direction == "right":
            cart.direction = "up"
            cart.y -= 1
        else:
            cart.direction = "left"
            cart.x -= 1

class RightDown(Corner):
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.symbol = "/"
    @staticmethod
    def move(cart):
        if cart.direction == "left":
            cart.direction = "down"
            cart.y += 1
        else:
            cart.direction = "right"
            cart.x += 1

        
        
