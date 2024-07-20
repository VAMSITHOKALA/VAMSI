num=int(input("Enter the number:"))
sum=0
temp=num
while temp>0:
    r=temp%10
    sum=sum*10+r
    temp=temp//10
if(sum==num):
    print("the given number is palindrome")
else:
    print("the given number is not palindrome")
