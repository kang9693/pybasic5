import os
import sys
import subprocess as sub
## 프로세스 가로체기

a = sys.argv[1:]
print(a[0])
a=int(a[0])
if a==1:
	pslist=os.system("tasklist | findstr python.exe")  #pslist
	print(pslist)
elif a==2:	
	pslist=os.popen("tasklist | findstr python.exe")
	while True:
		line = pslist.readline()
		if not line:break
		print(line.strip("\n"))
	#print(pslist)
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