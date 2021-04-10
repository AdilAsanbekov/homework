file = open('text2.txt', 'r')

print(file.read(1))
print()
print(file.read(2))
print()
print(file.read())
print()
print()

f = open('text2.txt')

for line in f:
	print(line)