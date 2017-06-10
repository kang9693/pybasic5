#chap03_section01

JUMSU=[70,60,55,90,85,75,80,100,95,45];
CNT=0;
i=0;


#print(JUMSU[1])
#print(JUMSU)
while(1):
	if(JUMSU[i] >=80):
		CNT=CNT+1  # c/java  에서는 C++ 로 가능
	i=i+1          # c/java  에서는 i++ 로 가능
	if(i>=10): break # 10 members
	
print("80점 이상인 사람 %d 이다." % CNT)
	