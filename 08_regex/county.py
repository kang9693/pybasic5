# -*- coding: utf-8 -*-
import shlex, subprocess
import os
import re
import sys
import time 
#import chardet  ## 케릭터 체크
#import pymysql
import sqlite3
from subprocess import Popen, PIPE

def sslvpnlog(log):
	#log = log.decode('ascii')
	
	
	f = open(log, 'r')	
	#encoding = chardet.detect(f)
	lines = f.readlines().encode('latin-1')
	print( lines )

 
def c_execute(cmd) :
    fd = subprocess.Popen(cmd, shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    return fd.stdout, fd.stderr
 
def a_execute(cmd) :
	std_in, std_out, std_err = os.popen3(cmd)
	return std_out, std_err
	
def d_execute(cmd,log):
	process = Popen([cmd, log], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
#cmd = "ls -l"
#std_out, std_err = execute(cmd)
#for line in std_out.readlines() :
#    print line,
def csv_file(log):
	f = open(log, 'r')
	#csvReader = csv.reader(f)
	#with open(log, 'rb') as csvfile:
	#	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	#	for row in spamreader:
	#		print (', '.join(row))

#import sqlite3
def sql_lite():
	# SQLite DB 연결
	conn = sqlite3.connect("county.db")
 
	# Connection 으로부터 Cursor 생성
	cur = conn.cursor()
 
	# SQL 쿼리 실행
	cur.execute("select * from county")
 
	# 데이타 Fetch
	rows = cur.fetchall()
	for row in rows:
		print(row)
 
	# Connection 닫기
	conn.close()	

def sqlite_main(argv):
	print(argv[0])

	cmd = "type " + argv[0]
	
	# type 로그파일.txt or 로그파일.log
	std_out, std_err = c_execute(cmd)
	
	for line in std_out.readlines():
	#	line #= line.decode('euc-kr')
	#	rec = re.findall('\S+',line)
		print(line)
		county=line.split() 
		c_code = county[0].decode('utf-8')
		c_name = county[1].decode('utf-8')
		c_code = str(c_code)
		c_name = str(c_name)
		print( county[0].decode('utf-8'),county[1].decode('utf-8'))
		print( c_code,c_name )
		conn = sqlite3.connect('county.db')
		c = conn.cursor()  
		c.execute('create table if not exists county (c_code, c_name)')
		#select
		row = (c_code,c_name)
		#print  (bar.open)
		sql = 'insert into county values (?, ?)'
		c.execute(sql, row)
		conn.commit()
		conn.close()		
	
	
if __name__ == "__main__":
	
	sqlite_main(sys.argv[1:])
	#csv_file(sys.argv[1:])
	#sql_lite()