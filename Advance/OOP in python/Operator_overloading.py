class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector<{}, {}>'.format(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __cmp__(self, other):
        print("My overloaded function is called")
        return self.a == other.a

    def __del__(self):
        print("Deleting object{}".format(self.a))


v1 = Vector(1, 1)
v2 = Vector(2, 2)

print(v1+v2)
print(9==7)

del v1
print("=============")
#print(v1.a)

print(hasattr(v2, 'a'))
print(hasattr(v2, 'c'))
delattr(v2, 'b')
print(dir(v2))
v2.b = 20
print(dir(v2))
print(hasattr(v2, 'b'))

print(dict(v2))
