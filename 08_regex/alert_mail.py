#-*- coding: utf-8 -*-
import os
import time
import subprocess
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate

from datetime import date 
from email import encoders

#msg['Subject']='The contents of %s' % textfile 
#msg['from']= me
#msg['To']= you



def sendMail():
	HOST=''
	
	sender = "email 주소"			#보내는 메일주소
	toAddrList = ["email 주소"]	#받는 사람 메일주소
	cc_users = ["email 주소"]		#참조 메일주소 
	
	me = 'm'
	you = '1'
	contents = '[이벤트] 보고서'    #메일 본문 내용
	
	msg = MIMEMultipart()
	
	msg = MIMEText(contents, _charset='euc-kr')	#메일 포멧
	msg['Subject']='[ALERT]보고서'					#메일 제목
	msg['From'] = me
	msg['Date'] = formatdate(localtime = True)
	msg['To'] = you
	#msg['Cc']= ",",join(cc_users) 
	
	#test = 'test'
	
	
	msg.attach(MIMEText(contents))
	
	
	for f in files:
		part = MIMEBase('application','octet-stream')
		part.set_payload(open(attach,'rb').read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
		msg.attach(part)
		
	#smtp = smtplib.SMTP(server, port)

def send_mail( send_from, send_to, subject, text, files=[], server="", port=25, username='', password='', isTls=True):
    
	msg = MIMEMultipart()
    
	msg['From'] = send_from
	msg['To'] = COMMASPACE.join(send_to)
	msg['Date'] = formatdate(localtime = True)
	msg['Subject'] = subject

	msg.attach( MIMEText(text) )

	for f in files:
		part = MIMEBase('application', "octet-stream")
		part.set_payload( open(f,"rb").read() )
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
		msg.attach(part)

	smtp = smtplib.SMTP(server, port)
   
	#if isTls: smtp.starttls()
	#smtp.login(username,password)
	smtp.sendmail(send_from, send_to, msg.as_string())
	smtp.quit()


   
	
	
	

	
if __name__ == "__main__":
	#sendMail()
	#send_mail( send_from, send_to, subject, text, files=[], server="", port=25, username='m', password='m', isTls=True):
	send_from =''			#
	send_to =''				#
	subject=''				#메일제목
	text='''<br>  
	         %s 입니다. '''  % '2017.03.29'
	files=['demo.docx']
	send_mail(send_from,send_to,subject,text,files)
	#ip = IP('')
	#ip_type= ip.iptype()	
	#print( ip.iptype())
	#print( ip_type )
	