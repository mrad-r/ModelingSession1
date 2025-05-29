from color_point import ColorPoint

class AdvancedPoint(ColorPoint): # This means we are inheriting from ColorPoint
    # pass This is used to say we don't want any code
    # Inheriting means that AdvancedPoint takes all the features of ColorPoint automatically.

    """
        AdvancedPoint extends ColorPoint by adding color validation and management features.

        Attributes:
            COLORS (list): Class-level list of valid color names.
        """
    COLORS = ["red", "green", "blue", "black", "white"]
    def __init__(self, x, y, color):
        """
        Initialize an AdvancedPoint instance with coordinates and a color.
        :param x: Numeric value representing the x-coordinate.
        :param y: Numeric value representing the y-coordinate.
        :param color: Color of the point which must be in COLORS list.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        if not color in self.COLORS:
            raise ValueError(f"Color must be one of: {self.COLORS}")
        # super().__init__(x, y, "red") # Call the init method of the parent
        self._x = x
        self._y = y
        self._color = color

    @property # Here we use property to make the access to data safer and cleaner.
    # We turn a method into a property so it can be accessed like a variable making it more readable.
    def x(self):
        """
        Get the x-coordinate of the point

        :return: The x-coordinate value
        """
        return self._x

    @property
    def y(self):
        """
        Get the y-coordinate of the point

        :return: The y-coordinate value
        """
        return self._y

    @property
    def color(self):
        """
        Get the color of the point

        :return: The color name as a string
        """
        return self._color

    @color.setter # We use setter to be able to change the value of the property safely like a variable.

    def color(self, new_color):
        """
        Set a new color for the point after validating it

        :param new_color: New color name to assign.
        :return: str
        """
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"Color must be one of: {AdvancedPoint.COLORS}")
        self._color = new_color

    @classmethod # Here we use @classmethod since we access the class and not the object.
    def add_color(cls, new_color):
        """
        Add a new color to the class-level COLORS list.

        :param new_color: Color to add to valid options.
        :return: str
        """
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculate Euclidean distance between two points

        :param p1: First point object with x and y properties
        :param p2: Second point object with x and y properties
        :return: Euclidean distance between p1 and p2
        """
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

    @staticmethod
    def from_dictionary(dict):
        """
        Create an AdvancedPoint instance from a dictionary

        :param dict: Dictionary with keys 'x', 'y', and 'color'
        :return: New AdvancedPoint instance
        """
        x = dict.get("x", 10)
        y = dict.get("y", 20)
        color = dict.get("color", "black")
        return AdvancedPoint(x, y, color)

AdvancedPoint.add_color("amber")
p1 = AdvancedPoint(1, 2, "red")

print(p1)
print(p1.distance_orig())

AdvancedPoint.add_color("amber")
p2 = AdvancedPoint(1, 3, "amber")
print(p2)

print(p2.color)
print(p2.color)
print(p2)

print(p2.x)
print(p2.y)

p2.color = "blue"
print(p2)
print(AdvancedPoint.distance_2_points(p1,p2))
p4 = AdvancedPoint.from_dictionary({"x": 44})
print(p4)






