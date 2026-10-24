n=[1,2,3,4,5,6,7,8]
m=[1,2,3,4,9,6]

dict={}

for i in n:
    if i in dict:
        dict[i]+=1
        
    else:
        dict[i]=1    

for i in m:
    if i in dict:
        print(dict[i])
        
    else:
        print(0)    