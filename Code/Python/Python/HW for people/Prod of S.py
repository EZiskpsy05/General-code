n = int(input("n: "))
if n % 2 != 0 or  n < 2 or n > 100 :
    print("n phải là số lẻ và nhỏ hơn 100/ lớn hơn 2")
else:
    S = 1
    for i in range(2, n+1, 2):
        S *= i
    print(f"Tổng của S là: {S}")    