num=int(input("Enter any number:"))
original=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

if reverse==original:
        print(f"Palindrom number {reverse}")
else:
    print("Not palindrom")        