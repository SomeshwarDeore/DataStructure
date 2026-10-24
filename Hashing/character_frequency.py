s = "bananaapple"
q = "aepxz"

dict={}
result={}
for i in s:
    if i in dict:
        dict[i]+=1
        
    else:
        dict[i]=1
        
for i in q:
    if i in dict:
        result[i]=dict[i]
        
print(result)                                    