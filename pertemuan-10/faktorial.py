def Faktorial(param:str) :

    if param.isnumeric() :
        borrow = 1
        for x in range( 1 , int(param)+1) :
            print(f"{x: <3} faktorial => {x * borrow}")
            borrow = x * borrow