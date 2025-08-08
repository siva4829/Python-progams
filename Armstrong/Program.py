print("Welcome to Armstrong")
armstrong= 0
num=int(input("Enter the number:"))
original=num
length=len(str(num))
while num>0:
    temp=num%10
    armstrong+=temp**length
    num//=10
print("It is an armstrong number")if(armstrong==original)else print("Not an armstrong number")
