n = int(input("n: "))
if n % 2 == 0 or  n < 1 or n > 99 :
    print("n phải là số lẻ và nhỏ hơn 99/ lớn hơn 1")
else:
    S = sum([1/(i**2) for i in range(1,n+1,2)])
    print(f"Tổng của S là: {S}")