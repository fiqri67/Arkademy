class biodata:
    def __init__(self,name,umur):
        self.name=name
        self.umur=umur
        self.addres="Jl.Mendut no 45, Keluarahan Taman Baru, Kec. Banyuwangi. Kab Banyuwangi"
        hobby = ["futsal", "kuliner", "traveling"]
        for i in hobby:
            print("Hobby saya adalah" + i)
        print("is married", bool(False))
        sekolah= ["SD 1 Muhammadiyah", 2003, 2009],["SMP 1 Banyuwangi", 2009, 2012],["SMA 1 Giri", 2012, 2015],["Universitas Jember", 2015, 2019]
        for i in sekolah:
            for j in i:

                    print("Nama Sekolah", i)
                    print("Tahun Masuk", j)

        skill=["MySQl", "Beginer"],["Analyst", "Beginner", "Design System", "Beginner"]
        for keahlian in skill:
            print("Keahlian", keahlian)
            for level in keahlian:
                print ("Level", level)
        print("interest_in_coding", bool(True))


biodata("Fiqri Yusril Rizal", 22)








