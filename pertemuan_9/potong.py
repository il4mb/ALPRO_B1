def potong(x=None):

    print(f"{ ' POTONG '.upper() :-^45}\n")

    if x is None:
        x = int(input("Masukan nilai belanja : "))

    dis = 0
    if x < 1000000:
        dis = 0
    elif x >= 1000000 and x < 5000000:
        dis = (20/100) * x
    elif x >= 5000000:
        dis = (35/100) * x

    print(f"Besar diskon yang diberikan : {dis:.2f}")
    print(f"Besar harga yang harus di bayarkan : {x - dis:.2f}")