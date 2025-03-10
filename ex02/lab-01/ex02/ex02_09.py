def kiem_tra_snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("nhap vao so can kiem tra: "))
if(kiem_tra_snt(number)):
    print(number,"la so nt")
else:
    print(number,"khong la so nt")