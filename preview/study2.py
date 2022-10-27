import numpy as np

np.zeros([2,2])
np.ones([2,3])

np.arange(10)
np.arange(10).reshape(2,5)
np.linspace(1, 10, 6) # 1부터 10 까지 6개요소를 등간격으로 만든다

np.array([[1,2,3], [3,4,5]])
np.array([[[1,2,3], 
           [1,1,1],
           [3,4,5]],

          [[6,7,8],
           [1,1,1],
           [9,10,11]]])

# R : 3 * 3 * 2
# py : 2 * 3 * 3

np.random.rand(2,3,3,5)

x = np.array([3,2,1])
x[0]
x[-1] #마지막꺼
x[:2]
x[1:]
x[1:3]

x[x>2]

X = np.arange(6).reshape(3,2)
X
X[0, 0]
X[1, 0]
X[:2, 0]
X[:2, :]

X[X > 2]
X[-1, 0]

Z = np.array([[[1,2,3], 
               [1,1,1],
               [3,4,5]],

              [[6,7,8],
               [1,1,1],
               [9,10,11]]])
Z[0, :, :]
Z[1, :, :]

Z[:, :, 0]

x = np.arange(0, 4)
y = np.random.choice(x, size = 10) # 복원추출
np.random.choice(x, size = 4, replace = False) # 비복원추출

np.sort(y)[::-1] # numpy는 내림차순이 없다. 따라서 이러한 방식을 사용해야한다.
np.argsort(y) # 정렬해주는 인덱스를 구해준다.
y[np.argsort(y)] 

X = np.array([[4,5,6],
              [1,2,3]])
X[:, 0]
X[np.argsort(X[:, 0]), :]

x = np.arange(0, 5)
y = np.arange(5, 10)
np.concatenate([x, y])

X
Y = np.array([[1],
              [2]])
np.concatenate([X, Y], axis=1)

Z = np.array([[1,2,3]])
X
np.concatenate([X, Z], axis=0)

x
y
# np.concatenate([x,y], axis=1) 일차원끼리는 이어붙일수 없다

x[:, np.newaxis]
x[np.newaxis, :]

np.concatenate([x[:, np.newaxis], y[:, np.newaxis]], axis =1)
np.concatenate([x[np.newaxis, :], y[np.newaxis, :]], axis = 0)

np.max(x)
np.min(x)
np.argmax(x)
np.argmin(x)
np.argmax(y)
np.argmin(y)
np.sum(x)
np.repeat(x, 3)
np.tile(x, 2)

x + 1 #브로드캐스팅
x/2
x**2

X - 1

y = np.array([1, 2, 3])
z = np.array([[1],
              [2]])
X + y
X + z

X = np.array([[1,2],
              [3,4],
              [5,6]])

y = np.array([2,3])
X + y
