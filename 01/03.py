# 숫자형 

'''
작성자: SeongHun Kang
Date : 2017. 05. 20
이프로그램은 사칙연산을 수행하는  프로그램이다. 
'''

import os
import time 

print("입력한 두수의 사친연산을 수행합니다. ")
a = input()
b = input()
a = int(a)
b = int(b)
if( len(str(a)) > 2):
	print("입력값의 길이가 2보다 크다!!! ")
	
else:
	c = a+b 
	print("%d = %d + %d " % (c,a,b) )
	c = a-b
	print("%d = %d - %d " % (c,a,b) )
	c = a * b
	print("%d = %d * %d " % (c,a,b) )
	c = a / b
	print("%d = %d / %d " % (c,a,b) )
	c= a // b 
	print("%d = %d // %d " % (c,a,b))







