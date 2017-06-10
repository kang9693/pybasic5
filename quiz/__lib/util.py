import time
from datetime import datetime

def log_time(option):
	
	if(option==1):
		logtime="{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
	if(option==2):
		logtime=("{:%Y/%m/%d %H:%M:%S}".format(datetime.now()))
	### 아래 시간 표시 의미 
	### 시스템, 
	## %Y 년
	## %m 월
	## %d  일
	## %H 시간
	## %M 분
	## %S 초 
	
	result=logtime
	return result