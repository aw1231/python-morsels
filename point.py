class Point:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self) -> str:
        return "Point(x=" + str(self.x) + ", y=" + str(self.y) + ", z=" + str(self.z) + ")"
    def __eq__(self, __o: object) -> bool:
        if self.x == __o.x and self.y == __o.y and self.z == __o.z:
            return True
        else:
            return False
    def __add__(self, __o):
        return Point(self.x + __o.x, self.y + __o.y, self.z + __o.z)
    def __sub__(self, __o):
        return Point(self.x - __o.x, self.y - __o.y, self.z - __o.z)
    def __mul__(self, num):
        return Point(self.x* num, self.y * num, self.z * num)

    __rmul__ = __mul__