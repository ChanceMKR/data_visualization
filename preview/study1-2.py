x = [1,2,3]
len(x)

y = "Beomjin Park"
len(y)

x.append(4)
x

y = [2,3,1,5,4]
y = sorted(x, reversed = True)

x = [2,2,2,1,1,3]
x.count(1)
x.count(2)

x = "banana"
x.count("a")

y = {"first name" : ["Beomjin", "Sion", "Sangjun"],
     "last name" :["Park", "Park", "Lee"]}

list(y.keys())
s
import numpy as np

np.array([1,2,3])
x

z = np.zeros(10)
z

u = np.ones(10)
u

z = np.random.rand(5)
z

mu = 10
sigma = 3

sigma * z + mu

r1 = np.arange(10)
r1

r2 = np.arange(3, 15, 2)
r2

r3 = np.linspace(1, 20, 7)
r3
np.diff(r3)
# 1번-0번, 2번-1번 ... 

Y = np.array([[1,2,3],
              [2,3,4]])

np.zeros([2,2])
np.ones([2,2])
np.random.randn(3,2)