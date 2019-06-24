a = [];
n = input("enter the size of the list: ");
n = int(n)

print("enter the elements :");
for i in range(0,n):
    print("a[",i,"] :", end = " ");
    x = input("")
    x = int(x)
    a.append(x)



print(a)
