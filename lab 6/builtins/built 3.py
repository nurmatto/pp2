nurma = input()
slice_operation = slice(None, None, -1)

str_after_slice_operation = nurma[slice_operation]
# в квадратных скобках у нурмы, операция очень похожа на допустим эту nurma[0:0:-1], это тоже самое просто я через slice built in написал
if nurma == str_after_slice_operation:
	print('yeah, this one is pallindrome')
else:
	print('sorry, maybe next time')