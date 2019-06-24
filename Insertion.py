x =[5,2,4,1,3,7,6,9,8]
def sort(arr):
    for j in range (1,len(arr)):
        key = arr[j]
        i = j-1
        while (i>-1) and key < arr[i]:
             arr[i+1]=arr[i]
             i -= 1
        arr[i+1] = key
    return arr

    
sort(x)
print(x)

