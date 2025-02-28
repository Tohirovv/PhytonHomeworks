class Vector:

    def __init__(self, *numbers):
        self.numbers = numbers

    def __str__(self):
        return f"Vector{self.numbers}"

    def __len__(self):
        return len(self.numbers)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions to be added.")
        return Vector(*(a + b for a, b in zip(self.numbers, other.numbers)))

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions to be added.")
        return Vector(*(a - b for a, b in zip(self.numbers, other.numbers)))

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions to be added.")
        return sum((a * b for a, b in zip(self.numbers, other.numbers)))

    def __rmul__(self, num):
        return Vector(*(a * num for a in self.numbers))

    def magnitude(self):
        return ((sum(a ** 2 for a in self.numbers)) ** 0.5)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a vector with zero magnitude.")
        return Vector(*(a / mag for a in self.numbers))


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * v2
v6 = 3 * v1
print(v1)
print(v3)
print(v4)
print(v5)
print(v6)
print(v1.magnitude())
print(v1.normalize())