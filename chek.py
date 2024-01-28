import os
def chek(x):
                for count, ch in enumerate(x, 1):
                        for i in x[count:4]:
                                #print(ch,i)
                                if (ch == i):
                                       return True 
try:
    f = open("t1.txt", "r")
    for x in f:
           #print(x,end='')
           if chek(x) == True:
                   pass
           else:
                   with open("output.txt", "a") as f:
                       f.write(x)
                   print(x)
    f.close()
except Exception as e:
     print(str(e))


     
     
     











  

