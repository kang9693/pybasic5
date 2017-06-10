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
#m1 = p.match("3 python")  ### match 문장이 일치 할때 출력 
#print(m1.group())         ### 듀풀 형태로 출력 됨

#목포수 >  
#기획, 설계 개발(coding,) 테스트 , 배포 유포수   
#애자일 
#공인인증서 :    본인 확인 
## 소프트웨어 누가 개발했는지 확인줘 코인사인즈 배포 인증 
