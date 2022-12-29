def hallo(name=None):

    print(f"{ ' SAY HALLO '.upper() :-^45}\n")

    if name is None:
        name = input("Masukan nama : ")

    print(f"output => Hallo {name}")

def luas_persegi_panjang(p=None, l=None):

    print(f"{ ' LUAS PERSEGI PANJANG '.upper() :-^45}\n")

    if p is None:
        p = int(input("Masukan nilai P : "))
    if l is None:
        l = int(input("Masukan nilai L : "))

    print(f"output => Luas persegi panjang adalah : { float(p * l) }")


def keliling_persegi_panjang(p=None, l=None):

    print(f"{ ' KELILING PERSEGI PANJANG '.upper() :-^45}\n")

    if p is None:
        p = int(input("Masukan nilai P : "))
    if l is None:
        l = int(input("Masukan nilai L : "))

    print(
        f"output => Keliling persegi panjang adalah : { float(2 * (p + l)) }")


def createArray() :
    arr = list()
    def add() :
        val = input("Masukan angka : ")
        arr.append(val)

    add()
    while True :
        
        op = input("Apakah ingin manambahkan isi array ? ketik (Y/N) : ")

        if op.lower() == "y" :
            add()
        elif op.lower() == "n" :
            return arr

def min(array=None):

    print(f"{ ' MIN '.upper() :-^45}\n")

    if array is None:
        array = createArray()

    val = array.__getitem__(0)
    for x in array:
        if x < val:
            val = x
    print(f"output => {val}")

def max(array=None):

    print(f"{ ' MAX '.upper() :-^45}\n")

    if array is None:
        array = createArray()

    val = array.__getitem__(0)
    for x in array:
        if x > val:
            val = x
    print(f"output => {val}")


def rata2(array=None):

    print(f"{ ' RATA-RATA '.upper() :-^45}\n")

    if array is None:
        array = createArray()

    _len = len(array)
    _sum = sum(array)

    print(f"output => {float(_sum / _len)}")


def potong(x=None):

    print(f"{ ' POTONG '.upper() :-^45}\n")

    if x is None:
        x = int(input("Masukan nilai belanja : "))

    dis = 0
    if x < 1000000:
        dis = 0
    elif x >= 1000000 and x < 5000000:
        dis = (20/100) * x
    elif x >= 5000000:
        dis = (35/100) * x

    print(f"Besar diskon yang diberikan : {dis:.2f}")
    print(f"Besar harga yang harus di bayarkan : {x - dis:.2f}")


def hitung_kalimat(kalimat=None, include_space=False):

    print(f"{ ' HITUNG KALIMAT '.upper() :-^45}\n")

    if kalimat is None:
        kalimat = input("Masukan kalimat : ")

    def tambahkan(char):
        if char in temp:
            temp[char] += 1
        else:
            temp[char] = 1

    temp = {}
    for x in kalimat:
        if include_space:
            tambahkan(x.lower())
        elif x != " ":
            tambahkan(x.lower())

    charts = sorted(temp.items(), key=lambda x: x[1])
    charts = dict(charts)
    keys = charts.keys()

    for x in keys:
        print(f"{x.upper()} => {charts[x]}")


def menu(msg = None):

    mList = ["hallo", "luas_persegi_panjang", "keliling_persegi_panjang",
             "min", "max", "rata2", "potong", "hitung_kalimat"]

    strm = f"\nList Function Dari Code Ini"
    for idx, item in enumerate(mList):
        strm += f"\n{idx +1} = {item}"

    if msg is None :
        msg = ""

    print(f"{strm}\n\n{msg}")
    p = input("\nMasukan pilihan : ")

    if p.isnumeric() and int(int(p) - 1) >= 0 and int(int(p) - 1) <= int(len(mList)):

        idx = int(int(p) - 1)
        fun = globals()[mList[idx]]

        print(f"{ ' FUNCTION '.upper() :-^45}")
        fun()

        while True :
            option = input("Apakah ingin mengulang? (Y/N) : ")
            if option.lower() == "y" :
                menu()
                break
            elif option.lower() == "n" :
                break
                
    else:
        menu("Index tidak valid !!!")


menu()
