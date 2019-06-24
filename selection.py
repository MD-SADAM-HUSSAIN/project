a =[6,9,1,5,0,2,4]

i = 0
while i<len(a)
    smallest = min(a[i:])
    index_of_smallest element = a.index(smallest)
    a[i],a[index_of_smallest] = a[index_of_smallest],a[i]
    i=i+1
print (a)
