def potong(nominal):

    nominal = int(nominal)
    dis = 0

    if nominal < 1000000:
        dis = 0

    elif nominal >= 1000000 and nominal < 5000000:
        dis = (20/100) * nominal

    elif nominal >= 5000000:
        dis = (35/100) * nominal

    return f"Besar diskon yang diberikan : {dis:.2f}\nBesar harga yang harus di bayarkan : {nominal - dis:.2f}"