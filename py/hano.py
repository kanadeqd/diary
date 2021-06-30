def hano(num,f,t,m):
    if (num ==1):
        print ("move 1 from " +f + " to " + t)
    else:
        hano(num-1, f,m,t)
        print("move " + str(num) + " from " + f + " to " + t)
        hano(num-1, m,t,f)


hano(3,'左','右',"中")