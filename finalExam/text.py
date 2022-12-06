import string
import re


strings = ["My", "name", "is", "Seongchan", "Kim"]

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


"Beomjine".replace("e", "a")
"Beomjine".find("e") # 처음으로 나타내는 위치
"Beomjine".find("a") # 없으면 -1 반환

"Beomjin".index("e") # find랑 비슷하게 동작
"Beomjin".index("a") # -> 없으면 에러 발생

try:
    "Beomjin".index("a")
except:
    "Beomjin".index("e")
    
["a", "b", "c"].find("a") # list는 find없음
["a", "b", "c"].index("a")

"Beomjine".rfind("e") # rfind는 뒤에서부터 숫자를 센다.
"Beomjine".rindex("e")

"Beomjine, Dayeong, Sihyeon".split(", ")
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














