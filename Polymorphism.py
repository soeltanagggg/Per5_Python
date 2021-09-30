class Handphone:
    def __init__(self, nama, jenis, harga):
        self.Nama_Handphone = nama
        self.Jenis_Handphone = jenis  
        self.Harga_Handphone = harga

    def showInfo(self):
        print ("Ini adalah Handphone")
        print ("Nama HP     :", self.Nama_Handphone)
        print ("Jenis HP    :", self.Jenis_Handphone)
        print ("Harga HP    :", self.Harga_Handphone)

class Xiaomi(Handphone):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis, 3500000)
    
    def showInfo(self):
        print ("Just for fans")
        print ("Nama HP     :", self.Nama_Handphone)
        print ("Jenis HP    :", self.Jenis_Handphone)
        print ("Harga HP    :", self.Harga_Handphone)
        print ("Cipset      : Snapdragon 732")
        print ("Internal    : 128 GB")
        print ("Layar       : AMOLED")
        print ("RAM         : 6GB")

class Samsung(Handphone):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis, 10000000)

    def showInfo(self):
        print ("More Than A Phone")
        print ("Nama HP     :", self.Nama_Handphone)
        print ("Jenis HP    :", self.Jenis_Handphone)
        print ("Harga HP    :", self.Harga_Handphone)
        print ("Cipset      : Exynos 9611")
        print ("Internal    : 256 GB")
        print ("Layar       : AMOLED")
        print ("RAM         : 8GB")
        print ("Fitur Camera: AI Camera")

class Huawei(Handphone):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis, 7000000)

    def showInfo(self):
        print ("Make it Possible")
        print ("Nama HP       :", self.Nama_Handphone)
        print ("Jenis HP      :", self.Jenis_Handphone)
        print ("Harga HP      :", self.Harga_Handphone)
        print ("Cipset        : Kirin High-end")
        print ("Internal      : 128 GB")
        print ("Layar         : AMOLED")
        print ("RAM           : 6GB")
        print ("Sistem Operasi: Harmony OS")

class Iphone(Handphone):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis, 15000000)

    def showInfo(self):
        print ("Think Different")
        print ("Nama HP       :", self.Nama_Handphone)
        print ("Jenis HP      :", self.Jenis_Handphone)
        print ("Harga HP      :", self.Harga_Handphone)
        print ("Cipset        : A14 Bionic")
        print ("Internal      : 256 GB")
        print ("Layar         : AMOLED")
        print ("RAM           : 8GB")
        print ("Sistem Operasi: IOS")

Hp1 = Xiaomi("Mi 11 Lite", "Entry level")
Hp2 = Samsung("Galaxy M52", "Top Class")
Hp3 = Huawei("Nova 9", "Top Class")
Hp4 = Iphone("Iphone 12 Pro", "Mid Range")

Hp1.showInfo()
print("")
Hp2.showInfo()
print("")
Hp3.showInfo()
print("")
Hp4.showInfo()




