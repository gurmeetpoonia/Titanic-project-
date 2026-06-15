import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
b=np.zeros(5) 
print(b)     # [0. 0. 0. 0. 0.]
print(np.ones(5) )
      # [1. 1. 1. 1. 1.]
print(np.arange(1,10) ) # 1 to 9
print(np.linspace(1,10,5))# 5 equal values
print(a.ndim )     # Dimensions
print(a.shape)     # Shape
print(a.size )     # Total elements
print(a.dtype )    # Data type
a = np.array([10,20,30])

print(a+5)
print(a-5)
print(a*2)
print(a/2)
a = np.array([10,20,30,40])

print(a.sum() )     # 100
print(a.mean() )    # 25
print(a.max() )   # 40
print(a.min() )     # 10
print(a.std() )     # Standard deviation
a = np.array([10,20,30,40])

print(a[0])
print(a[2])
print(a[-1])
a = np.array([10,20,30,40,50])

print(a[1:4])
print(a[:3])
print(a[2:])
a = np.array([
    [1,2,3],
    [4,5,6]
])

print(a)
print(a[0,1])
print(a[1,2])
a = np.array([1,2,3,4,5,6])

b = a.reshape(2,3)

print(b)
print(np.random.rand(3))
print(np.random.randint(1,100,5))
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a+b)
print(a-b)
print(a*b)
a=np.array([56,88,46,85,34,93,2])
print(np.unique(a))
print(np.sort(a))
print(np.sqrt(a))
print(np.log(a))
print(np.exp(a))