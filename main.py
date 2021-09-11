class tuonglol:
    def __init__(tuong,tentuong,giamua,chieucuoi):
        tuong.name=tentuong
        tuong.gia= giamua
        tuong.until=chieucuoi
    def inthongtin(tuong):
        print('Tên tướng: '+tuong.name)
        print('Giá mua tướng: '+tuong.gia)
        print('Kĩ năng cuối là :'+tuong.until+'\n')
yasuo=tuonglol('yasuo','6300 tinh hoa lam','trăn trối')
zed=tuonglol('zed','4800 tinh hoa lam','dấu ấn tử thần')
yasuo.inthongtin()
zed.inthongtin()