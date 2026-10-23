list=[1,2,3,4,5,6,1,1,1,7,8,9,10]

dict={}

for i in range(0,len(list)):
    dict[list[i]]=dict.get(list[i],0)+1
print(dict)    