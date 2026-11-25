from graphics import rectangle as r
from graphics import circle as c
from graphics.graphics_3d import cuboid as cb
from graphics.graphics_3d import sphere as s

print("Rectangle Area:", r.area(10, 5))
print("Rectangle Perimeter:", r.perimeter(10, 5))

print("Circle Area:", c.area(7))
print("Circle Perimeter:", c.perimeter(7))

print("Cuboid Area:", cb.area(4, 3, 2))
print("Cuboid Perimeter:", cb.perimeter(4, 3, 2))

print("Sphere Area:", s.area(7))
print("Sphere Perimeter:", s.perimeter(7))