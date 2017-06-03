'''
filename="test.txt"
f=open(filename,'w')  ## f 객체 를 선언 
for i in range(1,11):
    data ="%d번째 줄입니다.\n" % i
    f.write(data)
	
	#f.write(data)
f.close()
'''

f = open("test.txt",'r')
while True:
	
	line=f.readlines()		
	#if line ==" " 	
	if not line: break    #"\n" 
	print(line)

f.close()