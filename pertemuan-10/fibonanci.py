def Fibonanci(param:str) :
    if param.isnumeric() :
        param = int(param)
        a,b=0,1
        while b < param :
            print(b)
            a,b = b, int(a+b)