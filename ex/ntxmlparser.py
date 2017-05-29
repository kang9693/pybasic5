import xml.etree.ElementTree as ET

import csv
from lib.lib import *  #from 패키지명.모듈명 import 함수명, * 일경우 모든 값들
from lib.time import *
from lib.cisco import *
from conf.conf import *
from lxml import etree
from xml.etree.ElementTree import Element, dump


def file_list():   #folder_list( path )
	i=0
	dir_file=[]
	network_config_dir="D:\\util\\진단\\network\\03.NT\\"
	title_02='구분'
	NW1_03_result='진단결과'
	dir_list = os.listdir(network_config_dir)
	for dir_row in dir_list:
		#print('dir_list:',row )		
		dir_name=dir_row	
		dir_list = os.listdir(network_config_dir + dir_row)		
		#print("dir_list:",dir_list)
		for filename in dir_list:
			i= i + 1
			#print(++i)			
			
			#print(network_config_dir + dir_name +"\\"+ filename )
			dir_file = network_config_dir + dir_name +"\\"+ filename
			print( dir_file )
			try:
				test(dir_file,filename,dir_name)
				
			except ValueError:
				error_log_time=today(5)
				print( "error!!!" )
				#filename = str(filename)
				err_log= "nt_error_" + ".log"
				dname_err_log ="nt_error_dname" + ".log"
				f = open(err_log,"a")
				f.write( error_log_time +", "+ dir_file +"\n" )
				f.close 	
				#f = open(dname_err_log,"a")
				#f.write( error_log_time +", "+ dir_file+"\n" )
				#f.close
				#NW1_03_result_01='수동진단'	
	
	return





	
def test(dir_list,filename,dir_name):	

	data=codecs.open(dir_list,'r') #,'r','utf-8')
	targetxml=data.read()	

	
	root = ET.fromstring(targetxml)

	'''
	print( "ET.fromstring(targetxml):",ET.fromstring(targetxml ))
	print( "root", root )
	'''
	# 파일을 라이팅 하는 부분
	path='result\\'+dir_name +'\\'
	if not os.path.exists(path):
		os.makedirs(path)
	print(path)
	filename=path+filename+".csv"
	print(filename)
	Resident_data=open(filename,'w')		
	csvwriter = csv.writer(Resident_data)
	resident_head = []

	count = 0
	

	for member in root.iter('Item'):
		#print ("member:",member)
		resident = []
		address_list = []
		if count == 0:
			iCode = member.find('iCode').tag			
			resident_head.append(iCode)
			
			iTitle = member.find('iTitle').tag						
			resident_head.append(iTitle)
			
			InspectionCode = member.find('InspectionCode').tag			
			resident_head.append(InspectionCode)
			
			
			Result = member.find('Result').tag	
			resident_head.append(Result)
			
			
			Evidence = member.find('Evidence').tag
			resident_head.append(Evidence)
			'''
			Address = member[3].tag
			resident_head.append(Address)
			'''
			csvwriter.writerow(resident_head)
			count = count + 1

		iCode = member.find('iCode').text
		#print( 'name.text:',name)
		resident.append(iCode)
		iTitle = member.find('iTitle').text.strip('\n')
		resident.append(iTitle)
		InspectionCode = member.find('InspectionCode').text
		resident.append(InspectionCode)		
		Result = member.find('Result').text
		if ( Result=='양호'):
			Result ='Y'
		if ( Result=='미흡'):
			Result = 'N'
		if ( Result=='취약'):
			Result = 'N'
		#elif ( Result==')
		#Result=Result.strip().split(',')
		
		resident.append(Result)
		Result = member.find('Result').text
		
		
		Evidence = member.find('Evidence').text
		Evidence=Evidence.strip(',')
		resident.append(Evidence)
		

		csvwriter.writerow(resident)
	
				
				#data = reader.read()
				#fields = 
			
	''' '''
	#f.write(  )
	#with open(filename,'r') as reader:
	#		for line in reader:
	#			fields=line.strip().split(',')
	Resident_data.close()
	#with open(filename,'r') as reader:
	#		for line in reader:
	#			fields=line.strip().split(',')
				

	''' '''	
	''' '''
	
def csv_filelist():   #folder_list( path )
	i=0
	dir_file=[]
	##xml to csv_result file path
	network_config_dir="result\\"
	
	##csv_result make
	result_path='csv_result\\'

	
	result_data=''
	dir_list = os.listdir(network_config_dir)	
	for dir_row in dir_list:
		#print(dir_row)  #dir_row: result path name 
		dir_name=network_config_dir+dir_row
		#print("dir_name: ",dir_name)
		dir_list = os.listdir(network_config_dir + dir_row)		
		for file_name in dir_list:	
			filename=file_name 
			print(dir_name)
			dir_filename = dir_name+'\\' + file_name
			#print(dir_filename)
			
			data=codecs.open(dir_filename,'r') #,'r','utf-8')			
			path=result_path + dir_row
			if not os.path.exists(path):
				os.makedirs(path)
				#os.makedirs(path)
			
			
			#store_filename=result_path + dir_row + '\\' + file_name + ".csv"
			store_filename=result_path + dir_row + '\\' + 'result' + ".csv"  #통합결과파일
			#print(filename)
			'''
			for filename in dir_list:
			print("filename: ",filename)	
			
			'''
			result_data = filename.strip('_2017-02-06.xml.csv') + "\n"
			for lines in data:
				#print('lines:',lines[0])
				if( lines[0]=='S' or lines[0]=='i'):	
					print( lines )
					if( lines[0:8]=='SW23-212' or lines[0:8]=='SW23-410' or lines[0:8]=='SW23-107'
						or lines[0:8]=='SW23-108' or lines[0:8]=='SW23-109' or lines[0:8]=='SW23-110' or lines[0:8]=='SW23-111'
						or lines[0:8]=='SW23-112' or lines[0:8]=='SW23-113' or lines[0:8]=='SW23-114'
						or lines[0:8]=='SW23-115' or lines[0:8]=='SW23-116' 
						or lines[0:8]=='SW23-117' or lines[0:8]=='SW23-118'
						or lines[0:8]=='SW23-410' or lines[0:8]=='SW23-411'
						or lines[0:8]=='SW23-412' or lines[0:8]=='SW23-413'
						or lines[0:8]=='SW23-414' or lines[0:8]=='SW23-415'
						or lines[0:8]=='SW23-416' or lines[0:8]=='SW23-417'
						or lines[0:8]=='SW23-418' or lines[0:8]=='SW23-419'
						or lines[0:8]=='SW23-420' or lines[0:8]=='SW23-421'
						or lines[0:8]=='SW23-422' or lines[0:8]=='SW23-405'
						or lines[0:8]=='SW23-306' or lines[0:8]=='SW23-307'
						or lines[0:8]=='SW23-308' or lines[0:8]=='SW23-309'
						or lines[0:8]=='SW23-303' or lines[0:8]=='SW23-213'
						or lines[0:8]=='SW23-214' or lines[0:8]=='SW23-215'
						or lines[0:8]=='SW23-216' or lines[0:8]=='SW23-217'
						or lines[0:8]=='SW23-218' or lines[0:8]=='SW23-219'
						or lines[0:8]=='SW23-220' or lines[0:8]=='SW23-221'
						or lines[0:8]=='SW23-222' or lines[0:8]=='SW23-223'
						or lines[0:8]=='SW23-224' or lines[0:8]=='SW28-107' 
						or lines[0:8]=='SW28-108' or lines[0:8]=='SW28-109' or lines[0:8]=='SW28-110' or lines[0:8]=='SW28-111'
						or lines[0:8]=='SW28-112' or lines[0:8]=='SW28-113' or lines[0:8]=='SW28-114' or lines[0:8]=='SW28-115'
						or lines[0:8]=='SW28-116' or lines[0:8]=='SW28-117' or lines[0:8]=='SW28-118' or lines[0:8]=='SW28-212'
						or lines[0:8]=='SW28-213' or lines[0:8]=='SW28-214' or lines[0:8]=='SW28-215' or lines[0:8]=='SW28-216'
						or lines[0:8]=='SW28-217' or lines[0:8]=='SW28-218' or lines[0:8]=='SW28-219' or lines[0:8]=='SW28-220'
						or lines[0:8]=='SW28-221' or lines[0:8]=='SW28-224' or lines[0:8]=='SW28-303' 
						or lines[0:8]=='SW28-306' or lines[0:8]=='SW28-307' or lines[0:8]=='SW28-308' or lines[0:8]=='SW28-309'
						or lines[0:8]=='SW28-405' or lines[0:8]=='SW28-410' or lines[0:8]=='SW28-411'
						or lines[0:8]=='SW28-412' or lines[0:8]=='SW28-413' or lines[0:8]=='SW28-414' or lines[0:8]=='SW28-415'
						or lines[0:8]=='SW28-416' or lines[0:8]=='SW28-417' or lines[0:8]=='SW28-418' or lines[0:8]=='SW28-419' 
						or lines[0:8]=='SW28-420' or lines[0:8]=='SW28-421' or lines[0:8]=='SW28-422'
						or lines[0:8]=='SW28-222' or lines[0:8]=='SW28-223'
						):


						pass
					else:
					#print('lines[0:7]:',lines[0:8])
				#if (lines != NULL):
						stripped = lines
						print ( 'stripped:',stripped )
						#stripped +=stripped
						result_data += stripped
						Resident_data=open(store_filename,'w')
						Resident_data.write( result_data )
					#Resident_data.close()
				else:
					pass
		''' '''
		Resident_data.close()
		#Resident_data()
		#csvwriter = csv.writer(Resident_data)
		
		#targetxml=data.read()
	
	#Resident_data.close()

	
	return 0



def csv_riskresult():   #folder_list( path )
	i=0
	dir_file=[]
	##xml to csv_result file path
	network_config_dir="result\\"
	
	##csv_result make
	#result_path='csv_result\\'
	result_path='nt_csv_result\\'
	
	result_data=''
	
	file='D:\\util\\진단\\network\\nt_result.csv'
	
	if not os.path.exists(file):
		pass
	else:
		with open(file,'w') as csvfile:
			#i=i+1
			fieldnames=['자산구분','자산명','자산가치','Concern Code','점검항목','진단코드','진단결과','Concern Value','Concern 유형','Risk Value','Risk Grade','위험시나리오(현실태/문제점등기술)','Risk 유형','보호대책','평가결과','기술적','관리적','물리적','담당부서','담당자','우선순위','예산','조치계획','조치부서','조치담당자','조치확인','비고(조치불가사유)']
			#fieldnames = ['자산명(hostname)','iCode','iTitle','InspectionCode','Result','Evidence']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			csvfile.close()
	
	
	dir_list = os.listdir(network_config_dir)	
	for dir_row in dir_list:
		#print(dir_row)  #dir_row: result path name 
		dir_name=network_config_dir+dir_row
		#print("dir_name: ",dir_name)
		dir_list = os.listdir(network_config_dir + dir_row)		
		for file_name in dir_list:	
			filename=file_name 
			#filename=file_name 
			hostname=filename
			print(dir_name)
			dir_filename = dir_name+'\\' + file_name
			#print(dir_filename)
			
			
			
			data=codecs.open(dir_filename,'r') #,'r','utf-8')	
			csvReader = csv.DictReader(data)
			
			path=result_path + dir_row
			
			
			if not os.path.exists(path):
				os.makedirs(path)
				#os.makedirs(path)
			
			
			#store_filename=result_path + dir_row + '\\' + file_name + ".csv"
			store_filename=result_path + dir_row + '\\' + 'result' + ".csv"  #통합결과파일
			#print(filename)
			'''
			for filename in dir_list:
			print("filename: ",filename)	
			
			'''
			result_data = filename.strip('_2017-02-06.xml.csv') + "\n"
			for row in csvReader:
				print( row['iCode'])
				#printrow )
				#print(row['iCode'],row['iTitle'],row['InspectionCode'],row['Result'],row['Evidence'])
				#for (i,v) in enumerate(row):
				#	columns[i].append(v)
				#	print( columns[0])
				fields=[row['iCode']]
				asset_type=''  			#자산구분
				#asset_name = hostname  	# 자산명
				asset_value=''   		# 자산가치 
				Concern_Code=''         # Concern_Code
				check_type=''  			#체크항목
				if (row['iCode'] =='SU3-20' or
				#NT
					row['iCode']=='SW23-212' or row['iCode']=='SW23-410' or row['iCode']=='SW23-107'
					or row['iCode']=='SW23-108' or row['iCode']=='SW23-109' or row['iCode']=='SW23-110' or row['iCode']=='SW23-111'
						or row['iCode']=='SW23-112' or row['iCode']=='SW23-113' or row['iCode']=='SW23-114'
						or row['iCode']=='SW23-115' or row['iCode']=='SW23-116' 
						or row['iCode']=='SW23-117' or row['iCode']=='SW23-118'
						or row['iCode']=='SW23-410' or row['iCode']=='SW23-411'
						or row['iCode']=='SW23-412' or row['iCode']=='SW23-413'
						or row['iCode']=='SW23-414' or row['iCode']=='SW23-415'
						or row['iCode']=='SW23-416' or row['iCode']=='SW23-417'
						or row['iCode']=='SW23-418' or row['iCode']=='SW23-419'
						or row['iCode']=='SW23-420' or row['iCode']=='SW23-421'
						or row['iCode']=='SW23-422' or row['iCode']=='SW23-405'
						or row['iCode']=='SW23-306' or row['iCode']=='SW23-307'
						or row['iCode']=='SW23-308' or row['iCode']=='SW23-309'
						or row['iCode']=='SW23-303' or row['iCode']=='SW23-213'
						or row['iCode']=='SW23-214' or row['iCode']=='SW23-215'
						or row['iCode']=='SW23-216' or row['iCode']=='SW23-217'
						or row['iCode']=='SW23-218' or row['iCode']=='SW23-219'
						or row['iCode']=='SW23-220' or row['iCode']=='SW23-221'
						or row['iCode']=='SW23-222' or row['iCode']=='SW23-223'
						or row['iCode']=='SW23-224' or row['iCode']=='SW28-107' 
						or row['iCode']=='SW28-108' or row['iCode']=='SW28-109' or row['iCode']=='SW28-110' or row['iCode']=='SW28-111'
						or row['iCode']=='SW28-112' or row['iCode']=='SW28-113' or row['iCode']=='SW28-114' or row['iCode']=='SW28-115'
						or row['iCode']=='SW28-116' or row['iCode']=='SW28-117' or row['iCode']=='SW28-118' or row['iCode']=='SW28-212'
						or row['iCode']=='SW28-213' or row['iCode']=='SW28-214' or row['iCode']=='SW28-215' or row['iCode']=='SW28-216'
						or row['iCode']=='SW28-217' or row['iCode']=='SW28-218' or row['iCode']=='SW28-219' or row['iCode']=='SW28-220'
						or row['iCode']=='SW28-221' or row['iCode']=='SW28-224' or row['iCode']=='SW28-303' 
						or row['iCode']=='SW28-306' or row['iCode']=='SW28-307' or row['iCode']=='SW28-308' or row['iCode']=='SW28-309'
						or row['iCode']=='SW28-405' or row['iCode']=='SW28-410' or row['iCode']=='SW28-411'
						or row['iCode']=='SW28-412' or row['iCode']=='SW28-413' or row['iCode']=='SW28-414' or row['iCode']=='SW28-415'
						or row['iCode']=='SW28-416' or row['iCode']=='SW28-417' or row['iCode']=='SW28-418' or row['iCode']=='SW28-419' 
						or row['iCode']=='SW28-420' or row['iCode']=='SW28-421' or row['iCode']=='SW28-422'
						or row['iCode']=='SW28-222' or row['iCode']=='SW28-223' 
						##unix 
						or row['iCode']=='SU1-05'
						or row['iCode']=='SU1-06' 	or row['iCode']=='SU1-07' 	or row['iCode']=='SU1-08'
						or row['iCode']=='SU1-09' 
						or row['iCode']=='SU1-10'
						or row['iCode']=='SU1-11'
						or row['iCode']=='SU1-12'
						or row['iCode']=='SU1-13'
						or row['iCode']=='SU1-14'
						or row['iCode']=='SU1-15'
						or row['iCode']=='SU2-12'
						or row['iCode']=='SU2-15'
						or row['iCode']=='SU2-16'
						or row['iCode']=='SU2-18'
						or row['iCode']=='SU2-19'
						or row['iCode']=='SU2-20'
						or row['iCode']=='SU2-21'
						or row['iCode']=='SU3-09'
						or row['iCode']=='SU3-16'
						or row['iCode']=='SU3-17'
						or row['iCode']=='SU3-18'
						or row['iCode']=='SU3-19'
						or row['iCode']=='SU3-20'
						or row['iCode']=='SU3-21'
						or row['iCode']=='SU3-22'
						or row['iCode']=='SU3-23'
						or row['iCode']=='SU3-24'
						or row['iCode']=='SU3-25'
						or row['iCode']=='SU3-26'
						or row['iCode']=='SU3-27'
						or row['iCode']=='SU3-28'
						or row['iCode']=='SU3-29'
						or row['iCode']=='SU3-30'
						or row['iCode']=='SU3-31'
						or row['iCode']=='SU3-32'
						or row['iCode']=='SU3-33'
						or row['iCode']=='SU3-34'
						or row['iCode']=='SU3-35'
						or row['iCode']=='SU3-36'
						or row['iCode']=='SU4-03'
						or row['iCode']=='SU4-04'
				
				):
					print('NULL')
				else:
				
				#f= open('csv_result.csv','rb')
				
				
					
					with open(file,'a') as csvfile:
						#fieldnames=['자산구분','자산명','자산가치','Concern Code','점검항목','진단코드','진단결과', 
						#           'Concern Value','Concern 유형','Risk Value','Risk Grade','위험시나리오(현실태/문제점등기술)',
						#			'Risk 유형','보호대책','평가결과','기술적','관리적','물리적','담당부서','담당자','우선순위',
						#			'예산','조치계획','조치부서','조치담당자','조치확인','비고(조치불가사유)']
						#
						fields=['Windows',hostname,'자산가치',row['iCode'],row['iTitle'],row['InspectionCode'],row['Result'],'Concern Value','Concern 유형','Risk Value','Risk Grade',row['Evidence']]
						
						
						
						#] #,row['iTitle'],row['InspectionCode'],row['Result'],row['Evidence'].strip('\n')]
						#fieldnames = ['no','iCode','iTitle','InspectionCode','Result','Evidence']
						writer = csv.writer(csvfile)
						#writer.writeheader()
						writer.writerow(fields)
						#writer.writerow({'no':i,'iCode':row['iCode'],'iTitle':row['iTitle'],'InspectionCode':row['InspectionCode'],'Result':row['Result'],'Evidence':row['Evidence']})
						#writer.writerow({'first_name':'Baked','last_name':,'Beans'})
						#writer.writerow({'first_name':'Baked','last_name':,'Beans'})
		''' '''
		#Resident_data.close()
		#Resident_data()
		#csvwriter = csv.writer(Resident_data)
		
		#targetxml=data.read()
	
	#Resident_data.close()

	
	return 0	

if __name__ == "__main__":
	 
	 #file_list()
	 #csv_filelist()
	 #csv_strip('test')
	 csv_riskresult()
	 
	 #print(row)
