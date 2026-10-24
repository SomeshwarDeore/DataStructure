list=[1,2,3,4,5,6,7,8]
dict={}
for i in list:
    if i in dict:
        dict[i]+=1
        
    else:
        dict[i]=1
        
print(dict)        