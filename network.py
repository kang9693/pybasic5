#import lib.lib
from lib.lib import *  #from 패키지명.모듈명 import 함수명, * 일경우 모든 값들
from lib.time import *
from lib.cisco import *
from conf.conf import *

#########
###  
### pip install ciscoconfparse """
###"""
### 자산명 작성규칙
###  잘못된예)
###   1. 신채널(삼성, 하나카드) 죽전 UTM.log
###   2. 내부 팩스 UTM B.log
###  적절한 예
###   1. 내부_팩스_UTM_B.log
###  적절한 예와 같이 작성하여 제출 
#dir_list = os.listdir('Z:\\공유문서\\생명\\09.SLA\ 취약점\ 진단\\01\\05.NW')



### 추가 기능 구현요구사항 
###  1) 파일명 자동리네임(치환)
	

def read_file():
	#data=open('D:\\util\\진단\\network\\network\\UTM\DMZ 팩스 UTM A.log')
	data=codecs.open('D:\\util\\진단\\network\\network\\L2 스위치\\ESM L2 스위치.log','r','utf-8')
	#data=data.decode('utf-8')
	#print( type(data.read()) )
	print( data.read(),end='')
	
def file_list():   #folder_list( path )
	i=0
	network_config_dir="D:\\util\\진단\\network\\network\\"
	title_02='구분'
	NW1_03_result='진단결과'
	dir_list = os.listdir('D:\\util\\진단\\network\\network\\')
	for row in dir_list:
		#print( row )
		
		dir_name=row
		dir_list = os.listdir('D:\\util\\진단\\network\\network\\'+row)
		#print( dir_list)
		for row in dir_list:
			i= i + 1
			#print(++i)
			
			title = row
			print(row)
	'''network_config_dir="D:\\util\\진단\\network\\network\\"
	dir_list = os.listdir('D:\\util\\진단\\network\\network\\')
	cmd = "cat D:\\util\\진단\\network\\network\\UTM\DMZ\ 팩스\ UTM\ A.log"
	std_out, std_err = c_execute(cmd)
	for line in std_out.readlines():
		#	line #= line.decode('euc-kr')
		#	rec = re.findall('\S+',line)
		print("line:",line)
	'''
	'''
	for row in dir_list:
		dir_name=row
		#cmd = "type " + network_config_dir+dir_name +"\\" + row
		cmd = "type D:\\util\\진단\\network\\network\\UTM\DMZ\ 팩스\ UTM\ A.log"
		print("cmd:",cmd.encode('utf-8'))			
		print(cmd)			
		std_out, std_err = c_execute(cmd)
		#print std_out
		print(std_out,std_err)
		for line in std_out.readlines():
		#	line #= line.decode('euc-kr')
		#	rec = re.findall('\S+',line)
			print("line:",line)
	'''
	
def folder_list():   #folder_list( path )
	i=0
	network_config_dir="D:\\util\\진단\\network\\network\\"
	title_02='구분'
	NW1_03_result='진단결과'
	dir_list = os.listdir('D:\\util\\진단\\network\\network\\')
	for row in dir_list:
		#print( row )
		
		dir_name=row
		dir_list = os.listdir('D:\\util\\진단\\network\\network\\'+row)
		print( dir_list)
		for row in dir_list:
			i= i + 1
			#print(++i)
			
			title = row
			print( title )
			#cmd = "cat " + network_config_dir+dir_name +"\\" + row
			cmd = network_config_dir+dir_name +"\\" + row
			#cmd 디렉토리 + 파일 
			#(dname)
			#dname=network_config_dir+dir_name +"\\" + row
			#print(dname)
			#parse = CiscoConfParse(dname)
			
			try:
				### 한글파일 읽기 
				#parse = CiscoConfParse(dname)
				print ('---------start----------')
				#print (dname)
				print ('-------------------')
				print ('Global Config Audit')
				print ('-------------------')
				
				log_time=today(5)				


				#data=codecs.open(cmd,'r','utf-8')				
				#data.read()
				
				
				#dname_ture_log ="network_ture_dname" + ".log"
				#f = open(dname_ture_log,"a")
				#f.write( log_time +", "+ cmd + ":" + vtp_mode+"\n" )
				#f.close 
				
				
				'''
				#1.NW1-01,H,패스워드 설정
				pattern = re.compile("service password-encryption")
				for i, line in enumerate(codecs.open(cmd,'r','utf-8')):
					for match in re.finditer(pattern,line):
						#print("pattern:",pattern,"match.group():",match.group())
						#print('Found on line %s', match.group())
						if( match.group() == 'service password-encryption' ):
							print( '조건분기')
							print('Found on line %s', match.group())
				#2.NW1-02,H,패스워드 복잡성 설정
				#3.NW1-03,H,암호화된 패스워드 사용
				pattern = re.compile("service password-encryption")
				for i, line in enumerate(codecs.open(cmd,'r','utf-8')):
					for match in re.finditer(pattern,line):
						#print("pattern:",pattern,"match.group():",match.group())
						#print('Found on line %s', match.group())
						if( match.group() == 'service password-encryption' ):
							print( '조건분기')
							NW1_03_result ='Y'
							print('Found on line %s', match.group())
				#4.NW2-01,H,VTY 접근(ACL) 설정
				#5.NW2-02,H,Session Timeout 설정
				#6.NW3-01,H,최신 보안 패치 및 벤더 권고사항 적용
				#7.NW3-02,H,SNMP 서비스 확인
				#8.NW3-03,H,SNMP community string 복잡성 설정
				#9.NW3-04,H,SNMP ACL 설정
				#10.NW3-05,H,SNMP 커뮤니티 권한 설정
				#11.NW3-06,H,TFTP 서비스 차단
				#12.NW3-07,H,Spoofing 방지 필터링 적용
				#13.NW3-08,H,DDoS 공격 방어 설정
				#14.NW3-09,H,사용하지 않는 인터페이스의 shutdown 설정
				#15.match("service password-encryption")
				'''
				
			except ValueError:
				#error 발생시 로그 기록
				error_log_time=today(5)
				print( "error!!!" )
				#filename = str(filename)
				err_log= "network_error_" + ".log"
				dname_err_log ="network_error_dname" + ".log"
				f = open(err_log,"a")
				f.write( error_log_time +", "+ cmd+"\n" )
				f.close 	
				f = open(dname_err_log,"a")
				f.write( error_log_time +", "+ dname+"\n" )
				f.close
				NW1_03_result_01='수동진단'				
			#f = open (cmd,'r')
			#lines = f.read()
			#print(data.encode('utf-8')
			#for line in lines:
			#	print( line )
			#f.close()
			title_01 = title.strip('.log')
			
			#print( row )						
			#print("title:", title)
			title_02 += "," + str(title_01)
			#NW1_03_result ="," + NW1_03_result_01
			#print("title_01:",str(title_01)  )
			#print("title_02:",str(title_02)  )
			''' '''
		#dir_list = os.listdir('D:\\util\\진단\\network\\')
		#dir_list = os.listdir('D:\\util\\진단\\network\\')

	#print( row)
	csv_line_01=title_02 +"\n"
	
	
	#초기화
	#print( title_02 )
	i=0
	return title_02

def check_result():   #folder_list( path )
	i=0
	network_config_dir="D:\\util\\진단\\network\\network\\"
	title_02='구분'
	#NW1_03_result='진단결과'
	#NW1_03_result='\n'+'NW1_03'
	NW1_01_result='NW1_01'
	NW1_02_result='NW1_02'
	NW1_03_result='NW1_03'
	ip_http_server_result='ip_http_server'
	vtp_mode_result='vtp_mode'
	domain_lookup='domain_lookup'
	ip_source_route='ip_source_route'
	ip_http_server="ip_http_server"
	dir_list = os.listdir('D:\\util\\진단\\network\\network\\')
	
	for row in dir_list:
		#print( row )
		
		dir_name=row
		dir_list = os.listdir('D:\\util\\진단\\network\\network\\'+row)
		#debug_log("debug log:", dir_list)
		for row in dir_list:
			i= i + 1
			#print(++i)
			
			title = row
			#cmd = "cat " + network_config_dir+dir_name +"\\" + row
			cmd = network_config_dir+dir_name +"\\" + row
			dname = network_config_dir+dir_name +"\\" + row
			#cmd 디렉토리 + 파일 
			try:
				
				### 한글파일 읽기 
				parse = CiscoConfParse(dname)
				print ('---------start----------')
				print (dname)
				print ('-------------------')
				print ('Global Config Audit')
				print ('-------------------')
				
				log_time=today(5)	
				

				
				## VTP mode 
				
				if parse.find_lines('^vtp\smode\stransparent') or parse.find_lines('^vtp\smode\soff'):
					vtp_mode='PASS'
					vtp_mode_result_01='Y'
					print ('vtp mode = PASS')
				else:
					vtp_mode = 'FAIL'
					vtp_mode_result_01='N'
					print ('vtp mode = FAIL')
				
				#1.NW1-01,H,패스워드 설정
				#service password-encryption				
				if (parse.find_lines('^service\spassword-encryption') or  parse.find_lines('service password-encryption')):
					NW1_01_result_01='Y'
					print ('service password-encryption = PASS')
				else:
					print ('service password-encryption = FAIL')
					NW1_01_result_01='N'
					
					
				#ip source-route
				if parse.find_lines('^no\sip\ssource-route'):
					print ('no ip source-route = PASS')
					ip_source_route_01='Y'
				else:
					print ('no ip source-route = FAIL')
					ip_source_route_01='N'
				
				#domain lookup
				if parse.find_lines('^no\sip\sdomain-lookup') or parse.find_lines('^no\sip\sdomain\slookup'):
					print ('no ip domain lookup = PASS')
					domain_lookup_01='Y'
				else:
					print ('no ip domain lookup = FAIL')
					domain_lookup_01='N'
				#data=codecs.open(cmd,'r','utf-8')				
				#data.read()
				
				#3.NW1-03,H,암호화된 패스워드 사용
				#enable secret
				if parse.find_lines('^enable\ssecret'):
					print ('enable secret = PASS')
					NW1_03_result_01='Y'				
				else:
					print ('enable secret = FAIL')
					NW1_03_result_01='N'
				

				### 한글파일 읽기 
				#data=codecs.open(cmd,'r','utf-8')				
				#data.read()
				#1.NW1-01,H,패스워드 설정
				
				
				if parse.find_lines('^exeline\vty\0\4'):
					#vtp_mode='PASS'
					print ('vtp mode = PASS')
				else:
					vtp_mode = 'FAIL'
					print ('vtp mode = FAIL')
					
				NW1_01=parse.find_lines('^line\vty\0\4')
				print("NW1_01:",NW1_01)
				'''
				pattern = re.compile("service password-encryption")
				for i, line in enumerate(codecs.open(cmd,'r','utf-8')):
					for match in re.finditer(pattern,line):
						#print("pattern:",pattern,"match.group():",match.group())
						#print('Found on line %s', match.group())
						if( match.group() == 'service password-encryption' ):
							print( '조건분기')
							print('Found on line %s', match.group())
				'''
				#2.NW1-02,H,패스워드 복잡성 설정
				
				#3.NW1-03,H,암호화된 패스워드 사용
				#NW1_03_result_01='NW1-03'
				
				
				#5.NW2-02,H,Session Timeout 설정
				
				if parse.find_lines('^line\vty\0\4'):
					#vtp_mode='PASS'
					print ('vtp mode = PASS')
				else:
					vtp_mode = 'FAIL'
					print ('vtp mode = FAIL')
				
				#pattern = re.compile("service password-encryption")
				#data=codecs.open(cmd,'r','utf-8')				
				#data = data.read()
				#if ( ' ' != re.finditer(pattern,data)):
				#	NW1_03_result_01='Y'
				#else:
				#	NW1_03_result_01='N'
				
				#''' 				한줄씩 검사하는 로직   '''
				
				''''
				pattern = re.compile("service password-encryption")
				for i, line in enumerate(codecs.open(cmd,'r','utf-8')):
					for match in re.finditer(pattern,line):
						#print("pattern:",pattern,"match.group():",match.group())
						#print('Found on line %s', match.group())
						if( match.group() == 'service password-encryption' ):
							#print( )
							error_log_time=today(5)
							NW1_03_result_01 ='Y'
							#debug_log("cmd debug log: %s", cmd,
							debug_log= "debug_network_error" + ".log"
							f = open(debug_log,"a")
							f.write( error_log_time +", " + cmd+"," + NW1_03_result_01+"," + row + "\n" )
							f.close 	
							#print( )
							#print(row,'Found on line %s', match.group())
						else:
							NW1_03_result_01 ='N'
							debug_log= "debug_network_error" + ".log"
							f = open(debug_log,"a")
							f.write( error_log_time +", " + cmd+"," + NW1_03_result_01+"," + row + "\n" )
							f.close 	
							#print( )
				#4.NW2-01,H,VTY 접근(ACL) 설정
				#5.NW2-02,H,Session Timeout 설정
				#6.NW3-01,H,최신 보안 패치 및 벤더 권고사항 적용
				#7.NW3-02,H,SNMP 서비스 확인
				#8.NW3-03,H,SNMP community string 복잡성 설정
				#9.NW3-04,H,SNMP ACL 설정
				#10.NW3-05,H,SNMP 커뮤니티 권한 설정
				#11.NW3-06,H,TFTP 서비스 차단
				#12.NW3-07,H,Spoofing 방지 필터링 적용
				#13.NW3-08,H,DDoS 공격 방어 설정
				#14.NW3-09,H,사용하지 않는 인터페이스의 shutdown 설정
				#15.match("service password-encryption")
				'''
				
				#ip http server
				if ( parse.find_lines('^ip\shttp\sserver') or parse.find_lines('^ip\http\sserver') ):
					print ('no ip http server = FAIL')
					ip_http_server_01='Y'
				else:
					print ('no ip http server = PASS')
					ip_http_server_01='N'
				
			except ValueError:
				#error 발생시 로그 기록
				error_log_time=today(5)
				NW1_01_result_01='수동진단'
				NW1_02_result_01='수동진단'
				NW1_03_result_01='수동진단'
				NW2_01_result_01='수동진단'
				NW2_02_result_01='수동진단'
				vtp_mode_result='수동진단'
				ip_source_route_01='수동진단'
				domain_lookup_01='수동진단'
				ip_http_server_01='수동진단'
				print( "error!!!" )
				#filename = str(filename)
				#err_log= "network_error" + ".log"
				#f = open(err_log,"a")
				#f.write( error_log_time +", "+ cmd+"\n" )
				#f.close 	
			
			
			dname_ture_log ="network_ture_dname" + ".log"
			f = open(dname_ture_log,"a")
			#f.write( log_time +", "+ cmd + ":" + vtp_mode+"\n" )
			f.write( log_time +", "+ "dname:" + cmd + ":" + "NW1_03_result_01 result:" + NW1_03_result_01+"\n" )
			f.close 
			
			NW1_01_result += "," + NW1_01_result_01
			NW1_03_result += "," + NW1_03_result_01
			vtp_mode_result += "," + vtp_mode_result_01
			domain_lookup += "," + domain_lookup_01
			ip_source_route += "," + ip_source_route_01
			ip_http_server += ","  + ip_http_server_01
			
			#print("title_01:",str(title_01)  )
			#print("title_02:",str(title_02)  )
			''' '''
		#dir_list = os.listdir('D:\\util\\진단\\network\\')
		#dir_list = os.listdir('D:\\util\\진단\\network\\')

	#print( row)
	#csv_line_01=title_02 +"\n"
	#NW1_01_result ="\n" + NW1_01_result
	#NW1_02_result ="\n" + NW1_02_result
	NW1_01_result ="\n" + NW1_01_result
	NW1_03_result ="\n" + NW1_03_result
	#vtp_mode = "\n" + vtp_mode_result
	domain_lookup	=	"\n" + domain_lookup
	ip_source_route	=	"\n" + ip_source_route
	ip_http_server 	=	"\n" + ip_http_server
	
	
	## csv 파일에 데이터를 삽입하는 부분
	result = NW1_01_result + NW1_03_result + domain_lookup + ip_source_route + ip_http_server
	#초기화
	#print( title_02 )
	i=0
	return result
if __name__ == "__main__":
	#설정정보
	# 파일 및 폴더 경로 설정 필요 
	# 설정파일정의서: folder_list( path )
	#read_file()
	#'''
	cvs_title=folder_list()	
	cvs_data=check_result()
	create_file_csv('test_0210',cvs_title)
	add_data_file('test_0210',cvs_data)
	#'''
	#file_list()