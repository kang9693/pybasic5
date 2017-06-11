import threading
 
def example(argv_0):
    print (argv_0)
 
 
th = threading.Thread(target=example, args=('hi',))
th.start()
th.join()


#출처: http://bbolmin.tistory.com/164 [bbolmin]