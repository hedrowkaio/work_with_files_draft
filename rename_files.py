import os, sys

fl = []
fl = [f for f in sorted(os.listdir('ur_path'))] # если ur_path пустой, берет данные с текущей директории
fl.remove('rename.py')
var = 1


def delt():
    if len(fl) == 0:
        print("[+]Work done!")
        sys.exit()
    else:
        name = f'account{var}'
        os.rename(fl[0], name)
        del fl[0]


while True:
    delt()
    var += 1
