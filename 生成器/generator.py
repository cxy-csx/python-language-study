
# 例1
def MyGenarator():
	for i in range(100):
		yield i


generator = MyGenarator()

while True:
	try:
		val = generator.__next__()
	except StopIteration:
		break
	print(val)

# 例2
for item in enumerate([1, 3, 5, 7, 9]):
	print(type(item))  # <class 'tuple'>

def MyEnumerate(l):

	i = 0
	while i <= len(l) -1:
		yield i, l[i]
		i += 1

generator = MyEnumerate([1, 3, 5, 7, 9])

print(generator)

# 例子3
for item in zip([1, 3, 5, 7, 9], [0, 1, 2, 3, 4]):
	print(item)


def MyZip(l1, l2):
	i = 0
	while i<= len(l1) - 1:
		yield l1[i], l2[i]
		i += 1


for item in MyZip([1, 3, 5, 7, 9], [0, 1, 2, 3, 4]):
	print(item)


		




