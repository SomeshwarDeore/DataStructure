Queue=[]
max_size=5

while True:
    choice=int(input("Enter your choice\n1.Insert 2.Delete 3.Display 4.Exit\n"))
    
    if choice==1:
        if len(Queue)<max_size:
            value=int(input("Enter Element\n"))
            Queue.append(value)
            
        else:
            print("Queue is OVERFLOW") 
            
    elif choice==2:
        if len(Queue)<=1:
            value=int(input("Delete Element\n"))
            Queue.pop(value)
            
        else:
            print("Queue is UNDERFLOW")
            
    elif choice==3:
        for i in range(0,len(Queue)):
            print(Queue[i])
            
    elif choice==4:
        print("Program is End...!")   
        
    else:
        print("invalid choice")         
                         