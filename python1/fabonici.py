first = 0
second = 1
next = first + second
for i in range(0, 10):
	next = first + second
	print(next, end=" ")
 
	first = second
	second = next
