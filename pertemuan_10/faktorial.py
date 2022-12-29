def Faktorial(param:str) :

    out = ""
    if param.isnumeric() :
        borrow = 1
        for x in range( 1 , int(param)+1) :
            out += f"{x: <3} faktorial => {x * borrow}\n"
            borrow = x * borrow

    return out