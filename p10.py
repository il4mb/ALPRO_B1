import os

def Mengurutkan(param: str) :

    if param.__contains__(',') :
        param = param.split(',')

    lis = list(param)

    try :
        for i in range(len(lis) -1, -1, -1) :
            for ii in range(0, i) :

                if lis[i].isdigit() and lis[ii].isdigit() :
                    if lis[i] < lis[ii] :
                        tem = lis[i]
                        lis[i] = lis[ii]
                        lis[ii] = tem
                else :
                    if ord(lis[i]) < ord(lis[ii]) :
                        tem = lis[i]
                        lis[i] = lis[ii]
                        lis[ii] = tem
    except :
        print("Program Error coba lagi!!!")

    print(f"output => {lis}") 


def IsPrime(param: str) :

    if param.isnumeric() :
        x = int(param)
        if x == 2 or x == 3 : return True
        if x%2 == 0 or x < 2 : return False
        for i in range(3, int(x**.5)+1, 2) :
            if x%i == 0 :
                return False
        return True
    return False


def Faktorial(param:str) :

    if param.isnumeric() :
        borrow = 1
        for x in range( 1 , int(param)+1) :
            print(f"{x: <3} faktorial => {x * borrow}")
            borrow = x * borrow
            

def Fibonanci(param:str) :
    if param.isnumeric() :
        param = int(param)
        a,b=0,1
        while b < param :
            print(b)
            a,b = b, int(a+b)

li = list(locals().items())
funLi = []
for key, value in li :
    if callable(value) and value.__module__ == __name__:
        funLi.append(key)
menu = "List function dalam file ini :\n"
for index, item in enumerate(funLi) :
    menu += f"{int(index +1): <2} = {item}\n"


while True :
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print(menu)
    p = input("Masukan pilihan : ")
    if p.isnumeric() and int(int(p)) > 0 and int(int(p)) <= int(len(funLi)) : 

        print("Batasi dengan koma untuk array!!!")
        param = input("Masukan parameter : ")
        result = locals()[funLi[int(p) -1]](param)
        if result != None and len(str(result)) > 0 :
            print(f"output => {result}") 

        (lambda : input("\n\nPress enter untuk melanjutkan!!!"))()

    else :
        print("Tidak ditemukan!!!")
