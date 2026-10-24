list1=[1,2,3,4,5,6,7,8,9,10]
list2=[3,4,2,67,89,6,5,3]

hash=[0]*11

for i in list1:
    hash[i]+=1
    
for i in list2:
    if i<0 or i>10:
        print(0)
        
    else:
        print(hash[i])        