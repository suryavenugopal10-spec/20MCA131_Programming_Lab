# Importing complete modules
import graphics.rectangle
import graphics.circle

print("Rectangle Area:",
      graphics.rectangle.area(10, 5))

print("Rectangle Perimeter:",
      graphics.rectangle.perimeter(10, 5))

print("Circle Area:",
      graphics.circle.area(7))

print("Circle Perimeter:",
      graphics.circle.perimeter(7))

# Selective import
from graphics.graphics_3d import cuboid

print("Cuboid Surface Area:",
      cuboid.area(4, 3, 2))

print("Cuboid Perimeter:",
      cuboid.perimeter(4, 3, 2))

# Selective import of functions
from graphics.graphics_3d.sphere import area, perimeter

print("Sphere Surface Area:", area(7))
print("Sphere Perimeter:", perimeter(7))