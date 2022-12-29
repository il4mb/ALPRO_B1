"""
         THIS FILE CREATE PROGRAMATICALLY         
         FILE INI DIBUAT SECARA OTOMATIS          
       !!!TIDAK PERLU MENGEDIT DILE INI!!!        

Generated : 2022-12-29 14:21:55.582647
"""
def Faktorial(param:str) :

    out = ""
    if param.isnumeric() :
        borrow = 1
        for x in range( 1 , int(param)+1) :
            out += f"{x: <3} faktorial => {x * borrow}\n"
            borrow = x * borrow

    return out

def Fibonanci(param:str) :
    out = ""
    if param.isnumeric() :
        param = int(param)
        a,b=0,1
        while b < param :
            out += f"{b}\n"
            a,b = b, int(a+b)
    return out

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

def Mengurutkan(param: str) :

    if param.__contains__(',') :
        param = param.split(',')

    lis = list(param)

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



    return f"output => {lis}"

