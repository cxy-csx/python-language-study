# 上下文对象, 实现了__enter__以及__exit__方法

class Context():

	def __enter__(self):
		print('enter')
		return self


	def __exit__(self, exe_val, exe_type, exe_tb):
		print(exe_val)  # <class 'ZeroDivisionError'>
		print(exe_type) # division by zero
		print(exe_tb)  # <traceback object at 0x000001D9AA5451C0>
		import traceback
		print(traceback.extract_tb(exe_tb))  # 定位异常信息位置 [<FrameSummary file C:\Users\gmbjzg\Github\python基础学习\上下文管理器\context.py, line 24 in <module>>]
		print('exit')
		return True  # 如果返回值为True, 则不会抛出异常信息


with Context() as f:
	print(f)  # <__main__.Context object at 0x00000232BBFC54F0> __enter__方法的返回值
	1/0

# 方式二
import contextlib

@contextlib.contextmanager
def context():

	print('enter')

	yield context()

	print('exit')

with context() as f:
	print(f)  # <contextlib._GeneratorContextManager object at 0x000001CFDB2F7550> yield的返回值
	pass

# 方法三

class Context:

	def close(self):
		print('关闭文件')

# 创建上下文对象
with contextlib.closing(Context()) as f:
	print(f)  # <__main__.Context object at 0x000002163B4475B0>


# 上下文对象嵌套
with open('1.png', 'rb') as fp_read:
	with open('2.jpg', 'wb') as fp_write:
		fp_write.write(fp_read.read())

# 简写
with open('1.png', 'rb') as fp_read, open('2.jpg', 'wb') as fp_write:
	fp_write.write(fp_read.read())










