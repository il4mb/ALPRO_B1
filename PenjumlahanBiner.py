def sumBin(bin1, bin2) :

    bin1 = list(str(bin1))
    bin2 = list(str(bin2))

    print(bin1)
    print(bin2)

    pos = (len(bin1) -1)

    carry = False

    val = ""
    for x in range(pos, -1, -1) :

        sv = int(bin1[x] + bin2[x])
        if(carry != False) :
            sv += carry

        if sv == 2 :
            carry = 1
            val += "0"
        elif sv == 1 :
            val += "1"
        elif sv == 0 :
            val += "0"

    return val




a = '0111'
b = '1110'

x = sumBin(a, b)

print(x)