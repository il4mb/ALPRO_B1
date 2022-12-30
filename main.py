import glob, os, datetime


# EDIT GANTI MENJADI FOLDER TUJUAN
dir = 'pertemuan_10'

###########################  START  ###############################


def readLines(file: str):
    lines = list()
    with open(file) as f:
        lines = f.readlines()
    return lines


main_dir = os.path.join(os.getcwd(), dir)
modules = glob.glob(os.path.join(main_dir, "*.py"))
with open("temp.py", "w") as f:
    f.write(f"\"\"\"\n{'THIS FILE CREATE AUTOMATICALLY': ^50}\n{'FILE INI DIBUAT SECARA OTOMATIS': ^50}\n{'!!!TIDAK PERLU MENGEDIT DILE INI!!!': ^50}\n\nThis file is auto-generated in main.py and used for main.py, run main.py to run the code in this file\nFile ini dibuat otomatis di main.py dan digunakan untuk main.py, jalankan main.py untuk menjalan kode  di file ini\n\nGenerated : {datetime.datetime.now()}\n\"\"\"\n")
    for fp in modules:
        lines = readLines(fp)
        for line in lines:
            f.write(line)
        f.write("\n\n")

###########################  END  ###############################

from temp import *

class ASCII:

    def decode(self, codes: list):
        out = ""
        for x in codes:
            for y in x:
                if y == 0:
                    out += " "
                elif y == 1:
                    out += "_"
                elif y == 2:
                    out += "/"
                elif y == 3:
                    out += "\\"
                elif y == 4:
                    out += "'"
                elif y == 5:
                    out += "`"
                elif y == 6:
                    out += "L"
                elif y == 7:
                    out += "<"
                

            out += "\n"
        return out

    def encode(self, string: str):

        lines = string.split("\n")
        data = []
        for line in lines:
            listChr = list(line)
            lineData = []
            for chr in listChr:
                if chr == " ":
                    lineData.append(0)
                if chr == "_":
                    lineData.append(1)
                if chr == "/":
                    lineData.append(2)
                if chr == "\\":
                    lineData.append(3)
                if chr == "'":
                    lineData.append(4)
                if chr == "`":
                    lineData.append(5)
                if chr == "L":
                    lineData.append(6)
                if chr == "<" :
                    lineData.append(7)


            data.append(lineData)
        return data


IL = [
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    [2, 3, 1, 1, 0, 0, 1, 3, 0, 0, 0, 0, 2, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 3, 2, 3, 0, 3, 0, 0, 0, 0, 2, 3, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 2, 4, 3, 1, 2, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 1, 5, 3, 0, 0, 0, 0, 0], 
    [3, 2, 1, 2, 3, 0, 3, 2, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 1, 3, 0, 3, 0, 0, 0, 3, 0, 3, 0, 3, 6, 3, 0, 3, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 6, 3, 0, 3, 0, 0, 0], 
    [0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 1, 1, 0, 0, 3, 0, 3, 0, 0, 1, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 1, 1, 0, 3, 0, 0, 3, 0, 3, 0, 3, 1, 1, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 1, 0, 7, 4, 0, 0], 
    [0, 0, 0, 0, 3, 1, 3, 0, 3, 1, 1, 0, 0, 0, 3, 0, 3, 0, 3, 6, 3, 0, 3, 0, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 3, 0, 3, 0, 3, 2, 3, 0, 3, 0, 0, 3, 0, 3, 0, 3, 1, 2, 3, 0, 3, 0, 0, 1, 1, 0, 0, 0, 3, 0, 3, 0, 3, 6, 3, 0, 3, 0], 
    [0, 0, 0, 0, 2, 3, 1, 1, 1, 1, 1, 3, 0, 0, 0, 3, 0, 3, 1, 1, 1, 1, 2, 0, 0, 0, 3, 0, 3, 1, 3, 0, 3, 1, 3, 0, 0, 0, 3, 0, 3, 1, 3, 0, 3, 1, 3, 0, 0, 3, 0, 3, 1, 3, 3, 0, 3, 1, 3, 2, 3, 1, 3, 0, 0, 0, 3, 0, 3, 1, 1, 1, 1, 2, 0], 
    [0, 0, 0, 0, 3, 2, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 3, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 3, 2, 1, 2, 3, 2, 1, 2, 0, 0, 0, 0, 3, 2, 1, 2, 3, 2, 1, 2, 0, 0, 0, 3, 2, 1, 2, 0, 3, 2, 1, 2, 3, 2, 1, 2, 0, 0, 0, 0, 3, 2, 1, 1, 1, 2, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


funcs = []
msg = "Daftar function yang terbaca :\n"
index = 1

for key, value in list(globals().items()):
    
    if callable(value) and value.__module__ != __name__ and not key.__contains__("__"):
        funcs.append(key)
        msg += f"{index} => {key}\n"
        index += 1
        
        
        
if len(funcs) <= 0:
    msg += f"{'** Null **': ^25}\n"


while True:

    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("\033[H\033[J", end="")
    
    ascii = ASCII().decode(IL)
    print(ascii + "\n" + msg)
    p = input("Masukan pilihan : ")

    if p.isnumeric() and int(p) > 0 and int(p) <= len(funcs):

        fun = locals()[funcs[int(p)-1]]

        parameters = list()

        if fun.__code__.co_argcount > 0 :
            print("Pisakan dengan komma untuk membuat array")
        for x in range(0, int(fun.__code__.co_argcount)):

            param = fun.__code__.co_varnames[x]

            inp = input(f"Masukan nilai ({param}) : ")

            if inp.__contains__(","):
                inp = inp.split(",")

            parameters.append(inp)

        parameters = tuple(parameters)

        try:

            hasil = fun(*parameters)

            if hasil == None or (type(hasil) == str and len(hasil) <= 0):
                hasil = f"{'Tidak ada hasil': ^25}"

            print(hasil)

        except:

            print("Error...")

        (lambda: input("\nPress enter!!!"))()

    else:
        print("Pilihan tidak valid!!!")
