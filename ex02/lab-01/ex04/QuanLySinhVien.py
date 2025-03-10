from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def genarateId(self):
        maxId = 1
        if (self.soluongSinhVien()> 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (sv._id > maxId):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soluongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svId = self.genarateId()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh sinh vien: ")
        diemTB = float(input("Nhap diem sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.XeploaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhap ten sinh vien:")
            sex = input("Nhap gioi tinh sinh vien:")
            major = input("Nhap chuyen nganh sinh vien:")
            diemTB = float(input("Nhap diem sinh vien:"))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.XeploaiHocLuc(sv)
        else: 
            print("Sinh vien co Id = {} khong ton tai".format(ID))
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id,reverse=False)
    
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name,reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB,reverse=False)

    def findByID(self, ID):
        searchResult = None
        if(self.soluongSinhVien()> 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if(self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.lower() in sv._name.lower()):
                    listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        isDeleted = False
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def XeploaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"
    
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex" , "Major","DiemTb", "HocLuc"))
        if(listSV.__len__()> 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8} ".format(sv._id, sv._name, sv._sex,sv._major,sv._diemTB,sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien

    