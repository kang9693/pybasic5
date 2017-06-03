import time
from datetime import datetime

def log_time(option):
	
	if(option==1):
		logtime="{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
	if(option==2):
		logtime=("{:%Y/%m/%d %H:%M:%S}".format(datetime.now()))
	
	result=logtime
	return result