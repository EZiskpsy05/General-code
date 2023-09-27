n = int(input('n:'))
if (1<= n <= 99 and n%2!=0):
    print(type(n))
    print(n)
    s = 0
    for i in range (1,n + 1):
        if i %2!=0:
            s = float(s+1/(i**2))
            print(s)
        else:
                print("Sai n") 
