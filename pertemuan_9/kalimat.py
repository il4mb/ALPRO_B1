def hitung_kalimat(kalimat=None, include_space=False):

    print(f"{ ' HITUNG KALIMAT '.upper() :-^45}\n")

    if kalimat is None:
        kalimat = input("Masukan kalimat : ")

    def tambahkan(char):
        if char in temp:
            temp[char] += 1
        else:
            temp[char] = 1

    temp = {}
    for x in kalimat:
        if include_space:
            tambahkan(x.lower())
        elif x != " ":
            tambahkan(x.lower())

    charts = sorted(temp.items(), key=lambda x: x[1])
    charts = dict(charts)
    keys = charts.keys()

    out = ""
    for x in keys:
        out += f"{x.upper()} => {charts[x]}\n"

    return out