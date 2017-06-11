import os
import sys

a = sys.argv[1:]
#print(a[0])
a=int(a[0])
if a==1:
	pslist=os.system("tasklist | findstr 현금인출기.exe")  #pslist
	#print(pslist)
elif a==2:	
	#pslist=os.popen("tasklist | findstr 현금인출기.exe")  
	pslist=os.popen("dir test01.docx")  
	print(pslist)
	while True:
		line = pslist.readline()
		if not line:break
		f=open("popen_test.log",'a')
		print(line.strip("\n"))
		### 여기에서 
		f.write(line.strip("\n"))
		f.close
	#filepath="dir" 
	#3pslist=os.popen("dir c:\test*.docx")  