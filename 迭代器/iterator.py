# 例子1

l = [1, 3, 5, 7, 9]

list_iterator = l.__iter__()

while True:
	try:
		val = list_iterator.__next__()
		# val = next(list_iterator)
	except StopIteration as e:
		print(e)
		break
	print(val)

# 例子2

dit = {
	'name': 'gmbjzg',
	'age': 18
}

dict_keyiterator = dit.__iter__()

while True:
	try:
		k = dict_keyiterator.__next__()
		val = dit[k]
	except:
		break
	print(k, val)
