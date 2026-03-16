num=[]
s=int(input("Enter the size of the array:"))
for i in range(s):
    a=int(input("Enter the element:"))
    num.append(a)
key=int(input("Enter the element to be search:"))
for i in range(len(num)):
    if num[i]==key :
        print("Element found at the position of",i+1)
        found=True
        break
if found==False:
    print("Element not found!")