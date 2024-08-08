arr=[]
n=int(input("Enter number of elements"))
print("Enter Elements")
for i in range(n):
    a=int(input())
    arr.append(a)
sum=0
for i in range(n):
    sum+=arr[i]
print(f"sum is {sum}")
