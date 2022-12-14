import string
import pandas as pd
import re


strings = ["My", "name", "is", "Chance"]

# 연결하기
"".join(strings)
" ".join(strings)
",".join(strings)

LETTERS = list(string.ascii_uppercase) # -> 대문자모음
letters = list(string.ascii_lowercase) # -> 소문자모음

list(zip(LETTERS, letters))
["-".join([i,j]) for i, j in zip(LETTERS, letters)]

# (문자열).count(세고싶은거, 시작, 끝)
("a"*3 + "b"*2).count("b")
("a"*3 + "b"*2).count("a", 1, 5)

("chance").count("c")
("chance").count("c", 1, 5)


"chance".replace("c", "s")
"chance".find("a") # 처음으로 나타내는 위치
"chance".find("b") # 없으면 -1 반환

"chance".index("a") # find랑 비슷하게 동작
"chance".index("b") # -> 없으면 에러 발생

try:
    "Beomjin".index("a")
except:
    "Beomjin".index("e")
    
["a", "b", "c"].find("a") # list는 find없음
["a", "b", "c"].index("a")

"Beomjine".rfind("e") # rfind는 뒤에서부터 숫자를 센다.
"Beomjine".rindex("e")

"My name is Chance".split(" ")
"  a  ".strip()
"a b a b a".strip("a") # 앞과 뒤에만 지워준다.


z = re.search("e", "beeeomjin eee") # 첫번째가 e가 나오는 위치 -> re.Match 반환
if z:
    print("the pattern in string")

re.search(r"(e\w+)", "beeeomjin eee")
re.search(r"e\w+", "beeeomjin eee")
re.search(r"e\w+\s", "beeeomjin eee")
re.search(r"(e\w+)\s", "beeeomjin eee")
re.search(r"(e\w+)\s(e\w+)", "beeeomjin e")
re.search(r"(e\w+)\s(e\w+)", "beeeomjin eee")
# \w : 영어 대소문자와 _ 매칭 
# + : 1번이상
# \s : 띄어쓰기

re.match("e", "Beomjin")
re.match("b\w+\se\w+", "beeeomjin eee")
# match는 무조건 e가 첫번째로 나와야한다.

re.fullmatch("aaa", "aaa")
re.fullmatch("aaa", "aa")

string = "my name is Beomjin Park"
z = re.search(r"(\w+)\s(\w+)", string)
z
z.group(0)
z.group(1)
z.group(2)
# match라는 객체는  () 가 있으면 group화 해준다.
re.search(r"e\w+\s", "beeeomjin eee").group(0) # -> 에러발생


string = 'My name is Beomjin Park'
re.search(r'(\w+)', string)
z = re.search(r'(\w+)\s(\w+)', string)
z.start() # 문자열에서 처음으로 match 된 단어가 몇번째에 나오냐
z.end() # 문자열에서 처음으로 match 된 단어의 마지막
z.start(1) # 1그룹은 My이므로 0, 2 나옴
z.end(1)
z.start(2)
z.end(2)
string[z.start(2):z.end(2)]

re.findall(r'(\w+)\s(\w+)', string) # matching 되는 것들 다 찾음
z = re.finditer(r'(\w+)\s(\w+)', string)
# z.__next__() ## iter니까 처음 찾은 문자열 나옴 iter가 없으면 안ㄴ나옴
# list(z)
string = ''' Beomjin is in his 30's,
but he still have the same looks
from his teens to his 30's'
'''
z = re.finditer('his', string)
for m in z:
    print('The word "his" is matched at {}, {}'.format(m.start(), m.end()))

string = 'abcdefg'
re.sub('ab', 'AB', string)

string = 'My name is Beomjin Park'
re.sub(r'(\w+)\s(\w+)', 'merong', string, count=3)

re.split('j', string)
re.split("i", string)

c = re.compile(r"e")
c.search(string)

c = re.compile(r"(\w+)\s(\w+)")
c.sub("merong", string)

re.findall("[n|s]", "My name is Beomjin")

"\w+" # 하나이상 매칭
"\w?" # 딱 하나 나오는거
"\w*" # 안나와도 괜찮음
"\w{3}" # {}안의 숫자만큼 매칭
# 학습자료 참고!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

string = "beeeomjiiiin"
re.sub("e+|i", "e", string)
re.sub("e", "e", string)
re.sub("i", "e", string)
re.sub("e+|i{2,}", "e", string)
re.sub("e+|i{5,}", "e", string)
re.sub("e+|i{2}", "e", string)
re.sub("be*|ji*", "e", string)

string = "His shirt is grey"
re.sub("grey|gray", "red", string)
re.sub("gr(e|a)y", "red", string)


string = "beeeomjiiiin"
re.sub("[be]", "a", string) #[be] b, e중 하나
re.sub("b.e.", "a", string)
re.sub(".", "a", string)
re.sub("[.]", "a", string)
re.sub("^[be]", "a", string)
re.sub("[^be]", "a", string)
re.sub("[a-z]")
re.sub("[A-Z]")
re.sub("[0-9]")
re.sub("[a-zA-z]")
re.sub("[가-힣]")
re.sub("[\w]")
re.sub("[\W]")
re.sub("[\d]")


strings = '''
Beomjin Park : 010-1234-5678
SangjunMoon : 010-2345-6789
Sion Park:010-4321-1234
Younghee Ki : 01056561243
'''


"([A-Z][a-z]+\s*[A-z][a-z]+)s*:\s*([0-9]+-\*[0-9]+)"

'''
([A-Z][a-z]+\s*[A-z][a-z]+)
s*:\s*
([0-9]+-\*[0-9]+)

'''
z = re.compile(
    '''
    ([A-Z][a-z]+\s*[A-z][a-z]+)
    s*:\s*
    ([0-9]+-\*[0-9]+)

    ''', re.VERBOSE  # \n 제거
)
z.findall(strings)
pd.DataFrame(a, columns = ["name", "phone number"]) #시험문제 내시겠다


# 예제2 번 1, 3, 4

z =  re.compile(r'''
                ^[\w-](\.[\w-]+)*@[a-z0-9-]+(\/[a-z0-9-]+)*$
                ''', re.VERBOSE)

strings = ["bj-.__.park@gmail.kr.com",
           "bj,park@gmail.com", 
           "bj.par@gmail.com",
           "bj._abcd_.park@gmail.com"]

pos_vec = []
for i, string in enumerate(strings): # enumerate strings에 인덱스를 붙여준다.
    res = z.match(string)
    if res:
        pos_vec.append(i)
        

 


