def qu_chong(gun,latest):#前面的参数是原来的列表，后面的是去重之后的列表
    for A in gun:
        if A not in latest:
            latest.append(A)
    for B in latest:
        print("%s出现了%d次"%(B,gun.count(B)))
    print(latest)

