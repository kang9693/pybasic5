
### 로그 파일 쓰기 함수##
def log_write(filename, data,option): ## 파일명, 데이터, 옵션 (w, a, r)
	#filename : 파일명 
	#data : 저장할 데이터 
	#option # 저장옵션 w, a, r 
	#시간 언제, 
	f=open(filename, option)
	f.write(data+"\n")
	f.close()

	## 이함수가 return 특별하게 있을 까요 ? 
	## 파일사용중일때, 에러 ..  
	## 파일이 쓰였는지에 대해서 알려줘야 한다.
	# return의 경우는 일단 고민 
	return "저장되었습니다."

def log_read(filename, data,option): ## 파일명, 데이터, 옵션 (w, a, r)
	#filename : 파일명 
	#data : 저장할 데이터 
	#option # 저장옵션 w, a, r 
	f=open(filename,option)  
	f.readline()
	#로그에 대해서 즉 현금인출 현황을 파일로 기록한다면 
	
	f.close()

	## 이함수가 return 특별하게 있을 까요 ? 
	## 파일사용중일때, 에러 ..  
	## 파일이 쓰였는지에 대해서 알려줘야 한다.
	# return의 경우는 일단 고민 
	return "저장되었습니다."
	