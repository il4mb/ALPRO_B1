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