import os
import sys
import subprocess as sub  ## subprocess <== 
## 프로세스 가로체기

a = sys.argv[1:]
#print(a[0])
a=int(a[0])
if a==1:
	pslist=os.system("tasklist | findstr 현금인출기.exe")  #pslist
	#print(pslist)
elif a==2:	
	pslist=os.popen("tasklist | findstr 현금인출기.exe")  
	#<<  ## popen 시스템 명령어 또는 다른 console 명령어를 
	# 실행결과를 변수로 받을 때 
	# 지난주에 로그를 기록해보는것을 해보았습니다.
	# tasklist 와 같은 윈도우 시스템 명령어를 실행해서 결과를 받고자 할때 
	# popen 과 같은 함수를 이용하면 변수에 담아서 기록하거나 처리가 가능합니다. 
	
	#f=open("popen_test.log",'a')
	#f.write(pslist)
	#f.close
	
	while True:
		line = pslist.readline()
		if not line:break
		f=open("popen_test.log",'a')
		print(line.strip("\n"))
		### 여기에서 
		f.write(line.strip("\n"))
		f.close
	#print(pslist)
	''' '''
elif a==3:
	#pass
	pslist=sub.Popen(["tasklist | findstr python.exe"],stdout=sub.PIPE,stderr=sub.PIPE)
	output,errors=pslist.communicate()
	print(output)
else : 
	pass
'''
import os
p = os.popen('command',"r")
while 1:
    line = p.readline()
    if not line: break
    print (line)

	'''
'''
import subprocess as sub
p = sub.Popen(['your command', 'arg1', 'arg2', ...],stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()
print output  '''