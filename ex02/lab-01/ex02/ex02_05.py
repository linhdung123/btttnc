so_gio_lam = float(input("nhap so gio lam moi tuan:"))
luong_gio = float(input("nhap thu lao tren moi gio"))
gio_tc = 44
gio_vuot_tc = max(0,so_gio_lam - gio_tc)
thuc_linh = gio_tc * luong_gio + gio_vuot_tc * luong_gio * 1.5
print(f"so tien thuc linh cua nhan vien: {thuc_linh}")