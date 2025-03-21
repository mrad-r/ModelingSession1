import random
from itertools import count


class Point:
    """
    Class modeling a real life 20 point
    """
    def __init__(self, x, y):
        """
        Initialise the point instance
        :param x: the x-axis coordinate value
        :param y: the y-axis coordinate value
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Magic method that defines how a point is printed
        :return:
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__()

    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        Magic method that is called when you do self > other
        :param other: the other point comparing against
        :return: True/False
        """
        return self.distance_orig() > other.distance_orig()
    def __eq__(self, other):
        return self.distance_orig() == other.distance_orig()

if __name__=="__main__":
    points = []
    for i in range(5):
        p = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )

        # Append it to the list
        points.append(p)

    for point in points:
        print(points)

    # points.sort()
    p = Point(-12,-5)
    print(p.distance_orig())

    p1 = Point(1, 2) # Create a new instance
    p2 = Point(3,4)
    p3 = Point("James", "Jane") # This is valid but probably not intended

    print(p1.x, p1.y) # Access attributes
    print(p1)

    p1 = (4,6)
    p2 = (7,7)

    print(p1.__gt__(p2))

    print("unsorted points")
    print(points)
    print("sorted points")
    points.sort()
    print(points)

    found_equal = 0
    count = 0
    while True:
        if found_equal == 10:
            break
        p1 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )

        p2 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )

        count += 1
        if p1 == p2:
            print(p1, p2)
            found_equal +=1

    print(f"probability is 1 in {count/found_equal}")

