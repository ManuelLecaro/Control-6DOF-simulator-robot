import servo as serv
import struct

def load(result):
    for i in range(len(result)):
        paquete = struct.pack('f', result[i])
        serv.send_raw_data(paquete)
    #for data in result:
    #   serv.send_raw_data(data)