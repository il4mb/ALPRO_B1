"""
         THIS FILE CREATE PROGRAMATICALLY         
         FILE INI DIBUAT SECARA OTOMATIS          
       !!!TIDAK PERLU MENGEDIT DILE INI!!!        

This file is auto-generated in main.py and used for main.py, run main.py to run the code in this file
File ini dibuat otomatis di main.py dan digunakan untuk main.py, jalankan main.py untuk menjalan kode  di file ini

Generated : 2022-12-29 16:03:33.059000
"""
def hallo(name):

    return str(f"output => Hallo {name}")

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

    out = ""
    for x in keys:
        out += f"{x.upper()} => {charts[x]}\n"

    return out

def luas_persegi_panjang(panjang, lebar):
    return f"output => Luas persegi panjang adalah : { float(int(panjang) * int(lebar)) }"


def keliling_persegi_panjang(panjang, lebar):
    return f"output => Keliling persegi panjang adalah : { float(2 * (int(panjang) + int(lebar))) }"


def min(array :list):

    val = int(array.__getitem__(0))

    for x in array:
        x = int(x)
        if x < val:
            val = x

    return f"output => {val}"

def max(array=None):

    val = int(array.__getitem__(0))

    for x in array:
        x = int(x)
        if x > val:
            val = x

    return f"output => {val}"


def rata2(array):

    _len = len(array)
    _sum = sum(array)

    return f"output => {float(_sum / _len)}"

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

