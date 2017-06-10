import re
p = re.compile('[a-z]+')


#match
'''
m = p.match("python")
print(m)

#match method 
print(m.group())
print(m.start())
print(m.end())
print(m.span())
#print(m.span())
'''

### 정규식 기초 메타 문자 
# . ^ $ * + ? {{} \ | {} ()  문자
m1 = p.match("3 python")  ### match 문장이 일치 할때 출력 
print(m1.group())         ### 듀풀 형태로 출력 됨
