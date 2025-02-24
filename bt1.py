#baitap1
Hoten = input("nhap ten ban: ")
tuoi = input("nhap tuoi ban: ")
print("hoten",Hoten)
print("tuoi",tuoi)
# #baitap2
import math
r = float(input("nhap ban kinh: "))
dientich = math.pi*r*r
print("dien tich hinh tron la: ",dientich)
# #baitap3
n = int(input("nhap n: "))
if n % 2 ==0:
    print("n la so chan")
else:
    print("n la so le")

#baitap4 tạo danh sách rỗng duyệt từ 2000 đến 3200 xem i có chia hết cho 7 và không phải là bội của 5 hay không
list = []
for i in range(2000,3200):
    if i % 7 == 0 and i % 5 != 0:
        list.append(str(i))
print(list)

# baitap5 nhập xuất và tính giờ làm
gio_vo = int(input("nhap so gio lam: "))
gio_ra = int(input("nhap so gio tan ca: "))
gio_lam= gio_ra - gio_vo
print("so gio lam la: ",gio_lam)




