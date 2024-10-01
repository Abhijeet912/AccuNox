class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        return iter((self.length, self.width))

# Example usage:
rect = Rectangle(10, 5)

# Iterating over the instance
for dimension in rect:
    print(dimension)
