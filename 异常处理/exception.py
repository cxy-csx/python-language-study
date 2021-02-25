# 常见异常类型

1 / 0  # ZeroDivisionError
print(age)  # NameError
1 + '2'  # TypeError

li = [1, 2, 3]
print(li[3])  # IndexError

dit = {
	'name': 'gmbjzg',
	'age': 18
}
print(dit['height'])  # KeyError

class Person:
	pass
obj = Person()
print(obj.age)  # AttributeError

li = [1, 3, 5]

list_iterator = li.__iter__()

while True:
	list_iterator.__next__()  # StopIteration

# 异常捕获
try:
	print(age)
except NameError:
	print('NameError')

try:
	print(age)
	1/0
except ZeroDivisionError:
	print('ZeroDivisionError')
except NameError:
	print('NameError')
else:
	print('代码正常执行...')
finally:
	print('无论是否抛出异常，都会执行的代码')

li = [1, 3, 5, 7, 9]

while True:
	try:
		index = int(input('请输入索引:'))  # 只要抛出异常，代码就不会往下执行
		print(li[index])
	# except ValueError:
	# 	print('值错误')
	# except IndexError:
	# 	print('索引错误')
	except (ValueError, IndexError) as error:
		print(error)

# 手动抛出异常
def get_age(age):

	if isinstance(age, int):
		raise TypeError('类型错误')
	
try:
	get_age(1)
except TypeError as e:
	print(e)

# 自定义异常

class OverError(Exception):

	def __init__(self, error):
		self.error = error

	def __str__(self):
		return self.error


def get_age(age):

	if age >= 200:
		raise OverError('值超过200')

try:
	get_age(200)
except OverError as obj:
	print(obj)
