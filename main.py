import glob
import os, datetime


# EDIT GANTI MENJADI FOLDER TUJUAN
dir = 'pertemuan_9'

###########################  START  ###############################
def readLines(file : str):
    lines = list()
    with open(file) as f:
        lines = f.readlines()
    return lines

main_dir = os.path.join(os.getcwd(), dir)
modules = glob.glob(os.path.join(main_dir, "*.py"))
with open("temp.py", "w") as f:
    f.write(f"\"\"\"\n{'THIS FILE CREATE PROGRAMATICALLY': ^50}\n{'FILE INI DIBUAT SECARA OTOMATIS': ^50}\n{'!!!TIDAK PERLU MENGEDIT DILE INI!!!': ^50}\n\nThis file is auto-generated in main.py and used for main.py, run main.py to run the code in this file\nFile ini dibuat otomatis di main.py dan digunakan untuk main.py, jalankan main.py untuk menjalan kode  di file ini\n\nGenerated : {datetime.datetime.now()}\n\"\"\"\n")
    for fp in modules:
        lines = readLines(fp)
        for line in lines:
            f.write(line)
        f.write("\n\n")

###########################  END  ###############################


from temp import *

funcs = []
msg = "Daftar function yang terbaca :\n"
index = 1
for key, value in list(globals().items()):
    if callable(value) and value.__module__ != __name__:

        funcs.append(key)
        msg += f"{index} => {key}\n"
        index +=1
if len(funcs) <= 0 :
    msg += f"{'** Null **': ^25}\n"

while True :

    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print(msg)
    p = input("Masukan pilihan : ")

    if p.isnumeric() and int(p) > 0 and int(p) <= len(funcs):


        fun = locals()[funcs[int(p)-1]]


        parameters = list()

        print("Pisakan dengan komma untuk membuat array")
        for x in range(0, int(fun.__code__.co_argcount)) :

            param = fun.__code__.co_varnames[x]

            inp = input(f"Masukan nilai ({param}) : ")

            if inp.__contains__(",") :
                inp = inp.split(",")

            parameters.append(inp)


        parameters = tuple(parameters)


        try :


            hasil = fun(*parameters)

            if hasil == None or len(hasil) <= 0 :
                hasil = f"{'Tidak ada hasil': ^25}"

            print(hasil)


        except :

            print("Error...")



        (lambda : input("\nPress enter!!!"))()


    else :
        print("Pilihan tidak valid!!!")

