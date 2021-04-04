class SomeClass(object):
	attr1 = 42
	attr2 = "Hello"

	def method(self, x):
		return x * 2

obj = SomeClass()
print(obj.attr2)
print(obj.method1(6))

class Point(object):
	def __init__(self, x, y, z):
		self.coord = {"X": x, "Y": y, "Z": z}

point = Point(0, 80, 60)
print(point.coords)
	
	
def push(stack, element):
	stack.append(element)
	return stack

def is_empty(SomeCkass):
	if not stack:
		return True
	else:
		return False

def remove(stack):
	if not stack.is_empty():
		stack.pop()
	return stack

def calc(SomeCkass):
	i = 0
	while i < len(stack) -1:
		yield stack[i] * stack[i + 1]
		i += 1