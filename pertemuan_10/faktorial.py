def Faktorial(bilangan:str) :

    out = ""
    if bilangan.isdigit() :
        borrow = 1
        for x in range( 1 , int(bilangan)+1) :
            out += f"{x: <3} faktorial => {x * borrow}\n"
            borrow = x * borrow

    return out