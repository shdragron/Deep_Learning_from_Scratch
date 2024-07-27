import numpy as np
# numpy를 np라는 이름으로가져와!

x = np.array([1,2,3]) # 넘파이 배열
y = np.array([4,5,6])
print(x)
print(y)
print(type(x)) # numpy.ndarray

print(x + y) # 원소의 덧셈
print(x * y) # 원소의 곱셈
print(x / y) # 원소별 나눗셈
print((x+y)/2) # 원소별 나눗셈

# 주의점: 배열 원소의 개수가 같아야된다.
print()
# 2 x 2 배열
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)
print(A.dtype)