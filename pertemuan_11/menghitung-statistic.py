def MenghitungStatistic() :

    ListNilaiUAS = [77,75,85,78,87,79,84,93,55,80,76]
    ListNilaiUTS = [67,76,55,88,91,100,88,83,45,89,75]

    def statistik(code, array) :

        out = f"{code.upper()}\n"
        out += f"{'Nilai tertinggi': <17} : {max(array)}\n"
        out += f"{'Nilai terendah': <17} : {min(array)}\n"
        out += f"{'Jumlah nilai': <17} : {sum(array)}\n"
        out += f"{'Rata-rata nilai': <17} : {average(array)}\n"
        return out


    def min(array) :

        val = int(array.__getitem__(0))
        for x in array:
            x = int(x)
            if x < val:
                val = x
        return val

    def max(array) :

        val = int(array.__getitem__(0))
        for x in array:
            x = int(x)
            if x > val:
                val = x
        return val

    def sum(array) :

        total = 0
        for x in array :
            total += x
        return total 

    def average(array) :
        _len = len(array)
        _ttl = sum(array)
        return float(_ttl/_len)

    UAS = statistik("UAS",ListNilaiUAS)
    UTS = statistik("UTS",ListNilaiUTS)

    return f"{UAS}\n{UTS}"