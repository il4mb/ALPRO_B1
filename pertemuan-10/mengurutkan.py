def Mengurutkan(param: str) :

    if param.__contains__(',') :
        param = param.split(',')

    lis = list(param)

    try :
        for i in range(len(lis) -1, -1, -1) :
            for ii in range(0, i) :

                if lis[i].isdigit() and lis[ii].isdigit() :
                    if lis[i] < lis[ii] :
                        tem = lis[i]
                        lis[i] = lis[ii]
                        lis[ii] = tem
                else :
                    if ord(lis[i]) < ord(lis[ii]) :
                        tem = lis[i]
                        lis[i] = lis[ii]
                        lis[ii] = tem
    except :
        print("Program Error coba lagi!!!")

    print(f"output => {lis}") 