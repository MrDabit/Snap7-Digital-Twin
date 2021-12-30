# --------------------------------------------------------------------------------------
# | Py module: readDB.py                                                               |
# | Author: David García Rincón                                                        |
# | Date: 20210719                                                                     |
# | Version: 1.0 x64                                                                   |
# | Purpose: free software for testing and developing. Right working is not guarantied |
# --------------------------------------------------------------------------------------
# |                                        description                                 |
# --------------------------------------------------------------------------------------
# | This module is conecting to the PLC with the IP address defined in #1              |
# | Read the CPU name and CPU status in #2                                             |
# | Then will point the DB defined in #3 and returns values of system and DB           |
# | Mandatory to install snap7 module                                                  |
# --------------------------------------------------------------------------------------

import snap7
from snap7.util import *
from snap7.types import *
from time import sleep


IP = '127.0.0.1'
RACK = 0
SLOT = 2

DB_NUMBER = 3
START_ADDRESS = 0
SIZE = 259

plcOnline = False
plc = snap7.client.Client()

# 1.1 PLC connection via snap7 client module+


tries = 1
if tries < 2 and not plc.get_connected():
    try:
        print(f"trying to connect to PLC with IP {IP}")
        time.sleep(0.5)
        plc.connect(IP, RACK, SLOT)

    except Snap7Exception as e:
        logger.error("Warning in PLC connection >>{}.format(e)")
        sleep(0.5)
        if tries == 1:
            print("error in plc connection")
tries += 1


def plc_connect():
    plc = snap7.client.Client()
    tries = 1
    while tries < 2 and not plc.get_connected():
        try:
            print(f"trying to connect to PLC with IP {IP}")
            time.sleep(0.5)
            plc.connect(IP, RACK, SLOT)
            return True

        except Snap7Exception as e:
            logger.error("Warning in PLC connection >>{}.format(e)")
            sleep(0.5)
            if tries == 1:
                print("error in plc connection")
                return False
        tries += 1
    return False


def writeDBbit(dbNr, byte, bit, bitvalue):
    db = plc.db_read(dbNr, byte, 2)
    snap7.util.set_bool(db, byte, bit, bitvalue)
    plc.db_write(dbNr, 0, db)


def plcStatus():  # function readDB

    # 1. PLC connection definition
    IP = '127.0.0.1'
    RACK = 0
    SLOT = 2

    DB_NUMBER = 3
    START_ADDRESS = 0
    SIZE = 259

    # 1.1 PLC connection via snap7 client module
    plc = snap7.client.Client()
    plc.connect(IP, RACK, SLOT)

    # 2. Read PLC data
    plc_info = plc.get_cpu_info()
    plc_Type = plc_info.ModuleTypeName.decode('UTF-8').strip('\x00')
    #print(f'Module Type: {plc_info.ModuleTypeName}')
    plc_state = plc.get_cpu_state()
    # print(f'State:{plc_state}')

    # 3. Point DB and read data
    db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
    product_name = db[2:256].decode('UTF-8').strip('\x00')
    ## print(f'PRODUCT NAME: {product_name}')
    product_value = int.from_bytes(db[256:258], byteorder='big')
    ## print(f'PRODUCT VALUE: {product_value}')
    product_status = bool(db[258])
    # print(product_status)

    return (plc_Type, plc_state, product_name, product_value, product_status)


# if __name__ == '__main__':
    print('hola')
 #   plc = snap7.client.Client()
 #   plc.connect(IP, RACK, SLOT)
 #   writeDBbit(1, 0, 1, True)
    # datos = readDB()
    # print(datos)
