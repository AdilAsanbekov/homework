from stack2 import *

my_stack = ()
print(my_stack)
print(is_empty(my_stack))

push(my_stack, 1)
print(my_stack)
print(is_empty(my_stack))

push(my_stack, 2)
print(my_stack)

push(my_stack, 3)
print(my_stack)

remove(my_stack)
print(my_stack)

remove(my_stack)
print(my_stack)

calced_stack = calc(my_stack)
print(calced_stack)
for i in calced_stack:
	print(i)