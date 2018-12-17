import servo as serv

def load(result):
    for data in result:
        serv.send_raw_data(data)