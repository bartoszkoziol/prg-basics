class C:
    def __init__(self, coordinates):
        self.coordinates=coordinates

    def m(self, n):
        first_quadrant_count=sum(1 for x,y in self.coordinates if x>0 and y>0)

        return first_quadrant_count>=n

points = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

print(points.m(2))
print(points.m(3))