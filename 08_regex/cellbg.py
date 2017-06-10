# -*- coding: utf-8 -*-
from docxtpl import DocxTemplate, RichText
from struct import unpack
from socket import AF_INET, inet_pton
import wx
#import wx
import pygeoip
import sqlite3
import time
import msvcrt
import datetime
import cx_Oracle
import ipcheck
from datetime import date 



tpl=DocxTemplate('sample/event_report.docx')

def geoipcounty(county_code):
	conn = sqlite3.connect("county.db") 
	# Connection 으로부터 Cursor 생성
	cur = conn.cursor() 
	sql = "select c_name from county where c_code='" + county_code +"'"
	cur.execute(sql) 
	# 데이타 Fetch
	rows = cur.fetchall()
	for row in rows:
		county = row
	##rows = c.fetchall()
	##print( rows )
	##for row in rows:
	##	print(row)
 
	## Connection 닫기
	conn.close()	
	#print(county)
	
	#return county

def today_type(type):	
	#e = datetime.datetime.now()
	# 함수설명 넣는곳  
	#
	now = time.localtime()
	#now = time.localtime(	)
	#s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
	#s = "%04d/%02d/%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday,now.tm_hour)  # Ԣ࠹OރУ 
	if(type==1): 		
		s = "%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday)   # Ԣ/࠹/O
	if(type==2):
		s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday) 
	if(type==3):
		s = "%04d%02d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday,now.tm_sec) 
	if(type==4):
		s = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday) 
	if(type==5):
		s = "%02d" % (now.tm_hour)
	##print ( s )
	return s
	#print ( e )
	#s


def geoip(ip):
	#if len(sys.argv) is 1:
	#	print ("옵션을 주지 않고 이 스크립트를 실행하셨군요")
	
	#print ("옵션 개수: %d" % (len(sys.argv) - 1))
	#print ( "\n< 옵션 목록 >")

	#for i in range(len(sys.argv)):
	#	print ("sys.argv[%d] = '%s'" % (i, sys.argv[i]))
	print( ip )
		
	gi = pygeoip.GeoIP('GeoIP.dat')
	
	#print ( gi.country_code_by_name('sys.argv[1]'))
	# 'US' 출력
	#print ( sys.argv[1] )
	#county = 
	county_code=gi.country_code_by_addr( ip )
	#print (county_code.rstrip('\n'))
	conn = sqlite3.connect("county.db") 
	# Connection 으로부터 Cursor 생성
	cur = conn.cursor() 
	sql = "select c_name from county where c_code='" + county_code +"'"
	cur.execute(sql) 
	# 데이타 Fetch
	rows = cur.fetchall()
	#print ( "rows:rows )
	for row in rows:
		county = row[0].rstrip('\n')
		#print('국가코드')
		#print( county)
	#if( ip == '172.18.96.193'):county='내부'
	#if( ip == '172.18.59.112'):county='내부'
	#if( ip == '172.18.134.90'):county='내부'
	#county=geoipcounty(county)
	#ounty=county[1]
	#print (county.split('\n'))
	#return row
	
	return county
	# 'US' 출력
	#print ( gi.country_name_by_name('google.com'))
	# 'United States' 출력
	#print (gi.country_name_by_addr('64.233.161.99'))

	# 'United States' 출력

	#def main

def lookup(ip):
	f = unpack('!I',inet_pton(AF_INET,ip))[0]
	private = (
		[ 2130706432, 4278190080 ], # 127.0.0.0,   255.0.0.0   http://tools.ietf.org/html/rfc3330
		[ 3232235520, 4294901760 ], # 192.168.0.0, 255.255.0.0 http://tools.ietf.org/html/rfc1918
		[ 2886729728, 4293918720 ], # 172.16.0.0,  255.240.0.0 http://tools.ietf.org/html/rfc1918
		[ 167772160,  4278190080 ], # 10.0.0.0,    255.0.0.0   http://tools.ietf.org/html/rfc1918
	) 
	for net in private:
		if (f & net[1]) == net[0]:
			return True
	return False	

conn = sqlite3.connect('esm_event.db')
conn.text_factory = str
c = conn.cursor()
#curr = conn.cursor()
#sql = "select * from esm_event;"
c.execute('''PRAGMA encoding = "UTF-8";''')
#sql =".schema salespeople"
#c.execute('''create table esm_event (id INTEGER PRIMARY KEY AUTOINCREMENT, mgr_time TEXT,title TEXT, slocation TEXT, ext1 TEXT,src_info TEXT,src_port TEXT,to_attack_info TEXT,to_attack_port TEXT,alt_level TEXT,org_alert_level TEXT,info_status TEXT)''')
#print ( sql )

for row in c.execute('SELECT * FROM esm_event where src_info=\'50.63.197.204\''):
	print ("row[0]/id:",row[0])
	print ("row[1]/mgr_time:",row[1])  #mgr_time   탐지 시간 
	print ("row[2]/title:",row[2])  # title     인스던트명 
	print ("row[3]/slocation:",row[3])  # slocation  탐지장비
	print ("row[4]/ext1:",row[4])   # ext1
	print ("row[5]/src_info:",row[5])   # src_info
	print ("row[6]/src_port:",row[6])   # src_port 
	print ("row[7]/to_attack_info:",row[7])   # to_attack_info
	print ("row[8]/to_attack_port:",row[8])   # to_attack_port 
	print ("row[9]/alt_level:",row[9])   # alt_level
	print ("row[10]/org_alert_level:",row[10]) # org_alert_level
	print ("row[11]/info_status :",row[11]) # info_status 
	print ("row[12]/agent_name:",row[12]) # agent_name 
	#print ("row[12]:",row[12])
	#print ("row[13]:",row[13])
	#print ("row[14]:",row[14])
	#print ("row[2]
	#print ("row[2]
	#row[5] src_ip
	#row[6] src_port 
	date = today_type(2)  # today_type{} 함수 type 값 설명 :  1 2016/08/16,  2 2016-08-16 
	#print ( date )
	#print( lookup(str(row[5])))
	if ( True == lookup(str(row[5]))):
		county='내부'
	if ( False == lookup(str(row[5]))):
		county=geoip(str(row[5]))
	
	print( county )
	#print(county)
	payload = {  
		'company_name' : 'KoreaIT', 
		'date' : date, 
		'event_name' : row[2],
		'detect_unit' : row[12],
		'Detection_type': '차단',
		'detect_time' : row[1],     #탐지시간
		'src_ip':  row[5],
		'dst_ip': row[7],
		'event_detect_list':'공격상세내역',
		'whois' : county,  
		'target_port' : row[0],  
		'customer_Recommendations':'권고사항',  
		'event_Explanation':'이벤트 설명'
		#'monthly_avg_count' : 2225000
	}
	print ( payload )
	tpl.render(payload)
	
	filename="report/이벤트_탐지_보고서" + today_type(4)+ "_" + today_type(5)+".docx"
	print ( filename )
	tpl.save(filename) #''' ''''''
	
conn.commit()

#county=geoip('201.101.176.31')
#print (county.rstrip("\n"))
#conn.close()



