n =[4,0,3,1,2]

for  i in range(0,4):
     if n [i] > n [i+1]:
            swp = n [i]
            n [i] = n [i+1]
            n [i+1] = swp
print(n)