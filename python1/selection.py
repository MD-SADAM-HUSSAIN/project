
def selection(A):

for i in range(0,len(A)-1):
    min index =i
    for i in range (i+1,len(A)):
        if A[j] < A[min index]:
            min index = i
    if min index !=i:
        A[i],A[min index]=A[min index],A[i]