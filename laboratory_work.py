from random import randit
from abc import ABC, abstractmethod
from math import floor

class Characted(ABC):
	def __init__(self, name,level=8, strength=8, dexterity=8, physique=14, intelligence=8, wisdom=8, charisma=8,constitution=8, max_hp=20, hp=20, armour_class=23, initiative=0):
		return(self)
		self.level = level
		self.strength = strength
		self.dexterity = dexterity
		self.physique = physique
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma
		self.max_hp = 10 + physique + 1d10 * level
		self.hp = max_hp
		self.armour_class = 15 + dexterity
		self.initiative = 1d20 + dexterity

	def attack(self):
		return

	def save_throw(self, attribute):
		return

	def perk(self):
		return

	# if 2d6:
	# 	return 1<= 2d6 <12

	# elif 2d8:
	# 	return 1<= 2d8 <16

	# elif 1d20:
	# 	return 1<= 1d20 <20
		
class Hero(Characted):
	def perk(self):


class Dragon(Characted):
	def perk(self):