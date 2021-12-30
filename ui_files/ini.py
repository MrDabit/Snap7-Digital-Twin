import PLCcom


def Ini():
    PLCcom.writeDBbit(1, 0, 1, True)
    PLCcom.writeDBbit(1, 0, 2, True)
