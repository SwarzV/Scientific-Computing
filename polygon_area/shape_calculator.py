class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __repr__(self):
		return f'Rectangle(width={self.width}, height={self.height})'

	def get_perimeter(self):
		perimeter = 2 * self.width + 2 * self.height
		return perimeter

	def get_area(self):
		area = self.width * self.height
		return area

	def get_diagonal(self):
		diagonal = (self.width ** 2 + self.height ** 2) ** .5
		return diagonal

	def get_picture(self):
		if self.width > 50:
			return "Too big for picture."
		if self.height > 50:
			return "Too big for picture."

		width_display = "*" * self.width
		display = [width_display for a in range(self.height)]
		picture = "\n".join(display)

		return picture + "\n"

	def get_amount_inside(self, shape):
		w = self.width // shape.width
		h = self.height // shape.height

		return w * h

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

class Square(Rectangle):

	def __init__(self, side):
		self.width = side
		self.height = side

	def __repr__(self):
		return f'Square(side={self.width})'

	def set_side(self, side):
		self.width = side
		self.height = side


rect = Rectangle(10, 5)

print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))