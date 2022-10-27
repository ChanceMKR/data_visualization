1 + 2
4 - 10
2 * 2
4 / 2
5 / 2
2 ** 3
5 // 2
5 % 2

"ㄱㄴㄷ"
x = 'ㄷㄹㅁ'

type(x)
int()
float()
complex()
str(100)

"박범진이 '뭐라뭐라' 말했다."
'박범진이 "뭐라뭐라" 말했다.'

'''
박범진이
"뭐라뭐라"
말했다.
'''

y = "My name is Seongchan Kim"
y + 'abc'
y * 2

sentence = "My name is %s"
name1 = "Seongchan Kim"
name2 = "YDY"

sentence %(name1)
sentence %(name2)

a = "%d is an integer"
a %(1.1)

b = "%f is a float"
b %(1.1)

b = "%1.1f is a float"
b %(1.1)

b = "%1.2f is a float"
b %(1.1)

c = "%d + %d = %d"
c %(3, 3, 3+3)

d = "My name is {0}"
d.format("Seongchan Kim")

e = "{0} + {1} + {2}"
e.format(1, 2, 1+2)

f = "{num1} + {num2} + {num3}"
f.format(num1=1, num2=2, num3=1+2)

True
False

2<3
2>3

(3-2) == 1
2 != 1
"Seonchan" != "Woobin"
"Seonchan" >= "Woobin"

True == 1
False == 0

int(True)
int(False)

not True
not False

True and True
True and False
True or True
True or False

x = 1
0 < x < 2

x = [1,2,3,4,5,6]
x

y = [1, "a", True, [3,4]]
y

z = (1,2,3)
z

a = [1, "a"]
b = [1, "b"]
a + b

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set1 | set2
set1. union(set2)

set1 & set2
set1.intersection(set2)

set2 - set1
set1 - set2
set1.difference(set2)
set2.difference(set1)




