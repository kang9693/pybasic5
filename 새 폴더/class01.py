class Service:
    secret = "영구는 배꼽이 두 개다."
    def sum(self, a, b):                # 더하기 서비스
        result = a + b
        print("%s + %s = %s입니다." % (a, b, result))
		
pey=Service()

pey.sum(1,1)
#pey.sum(pey,1,1)
pey.sum(pey, 1, 1)