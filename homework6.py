from math import pi

from abc import ABC, abstractmethod

class Figure():
	def draw(self):
		print("Квадрат нарисован. ")

@abstractmethod
class Square(Figure):
	def move(S, a):
		super().move() = S = a^2

@abstractmethod
class Round(Figure):
	def move(S, a):
		super().move() = S = pi*a^2
		print("Круг нарисован. ")

