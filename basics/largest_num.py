num=[]
s=int(input("Enter the size of the list:"))
for i in range(s):
    a=int(input("Enter the element to the list:"))
    num.append(a)
largest=num[0]
for i in num:
    if i>largest:
        largest=i
print("Largest num is:",largest)
