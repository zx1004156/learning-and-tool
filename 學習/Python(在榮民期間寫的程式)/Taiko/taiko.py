from itertools import product

while(1):
    t = input()
    t = int(t)
    for i in product(range(2),repeat=t):
        for j in i:
            if(j==1):
                print ("咚",end = '')
                
            elif(j==0):
                print("鉲",end = '')
        print('')    
