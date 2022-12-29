def Fibonanci(param:str) :
    out = ""
    if param.isnumeric() :
        param = int(param)
        a,b=0,1
        while b < param :
            out += f"{b}\n"
            a,b = b, int(a+b)
    return out