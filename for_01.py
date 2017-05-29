list = [1,2,3,4,5,6,7,8,9,10]

### 초기값을 설정한다. 
result=0
for i in range(0,10):
	
	result = result + list[i]  ##=> result+=list[i]
	print("list index: %d, range value: %d, 누적합계: %d" % (list[i],i,result))

