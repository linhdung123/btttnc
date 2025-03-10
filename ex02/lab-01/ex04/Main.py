from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()
while (1 == 1):
    print ("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("**************************MENU**************************")
    print("1. Them moi sinh vien.")
    print("2. Cap nhat thong tin sinh vien boi ID.")
    print("3. Xoa sinh vien boi ID.")
    print("4. Tim kiem sinh vien theo ten.")
    print("5. Sap xep sinh vine theo diem trung binh.")
    print("6. Sap xep sinh vine theo ten chuyen nganh.")
    print("7. Hien thi danh sach sinh vien.")
    print("0. Thoat.")
    print("********************************************************")

    key = int (input("Nhap lua chon cua ban: "))
    if (key == 1):
        print("\n 1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\n Them sinh vien thanh cong!")

    elif (key == 2):
        if(qlsv.soluongSinhVien() > 0):
            print("\n 2. Cap nhat thong tin sinh vien boi ID.")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien rong!")

    elif(key == 3):
        if(qlsv.soluongSinhVien() > 0):
            print("\n 3. Xoa sinh vien boi ID.")
            print("\nNhap ID: ")
            ID = int(input())
            if(qlsv.deleteByID(ID)):
                print("\nSinh vien co id =",ID, "da bi xoa!")
            else:
                print("\nKhong tim thay sinh vien co id =",ID,"trong danh sach")
        else:
            print("Danh sach sinh vien rong!")

    elif (key == 4):
        if(qlsv.soluongSinhVien() > 0):
            print("\n 4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien rong!")

    elif (key == 5):
        if(qlsv.soluongSinhVien() > 0):
            print("\n 5. Sap xep sinh vine theo diem trung binh.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong!")

    elif (key == 6):
        if(qlsv.soluongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 7 ):
        if(qlsv.soluongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong!")
    
    elif (key == 0):
        print("\n 0. Ket thuc chuong trinh")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu")