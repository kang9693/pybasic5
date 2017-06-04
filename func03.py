def dic_param2(**kwargs): ### 딕셔너리 타입 일때  
    print ("kwargs:",kwargs)
    print ("key:",kwargs.keys())
    print ("value:",kwargs.values())
 
    for name, value in kwargs.items():
        print ("%s : %s" % (name, value))
 
dic_param2(first = 'a', second = 'b', third = 'c', fourth = 'd')