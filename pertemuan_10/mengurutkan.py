def Mengurutkan(array) :
    
    lis = list(array)

    for i in range(len(lis) -1, -1, -1) :
        for ii in range(0, i) :

            try :
                if int(lis[i]) < int(lis[ii]) :
                    tem = int(lis[i])
                    lis[i] = int(lis[ii])
                    lis[ii] = tem
            except :
                if ord(lis[i]) < ord(lis[ii]) :
                    tem = lis[i]
                    lis[i] = lis[ii]
                    lis[ii] = tem

    return f"output => {lis}"