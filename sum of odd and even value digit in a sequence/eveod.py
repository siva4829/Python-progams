even = 0
odd =0
try:
    num=int(input("Enter the number:"))
    a=int(len(str(num)))
    for i in range (0,a):
        if(i%2==0):
            even+=i
        else:
            odd+=i
except Exception as e:
    print(e) 
print("The count of even digit:",even)
print("The count of odd digit:",odd)
