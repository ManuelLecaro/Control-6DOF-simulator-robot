#import servo as serv
import struct

def load(result):
    for i in range(len(result)):
        paquete = struct.pack('f', result[i])
        serv.send_raw_data(paquete)
    #for data in result:
    #   serv.send_raw_data(data)

def take_time(data):
    tiempo = []
    init_time = 0
    for i in range(0, len(data)):
        tiempo.append(init_time)
        init_time+=0.01
    return tiempo,data