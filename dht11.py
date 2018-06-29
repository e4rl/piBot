# !/usr/bin/python
# -*- coding: UTF-8 -*-

def currentTEMP(temp):
    tmp = float(temp)
    if tmp != 0:
        tmp = tmp / 1000
    return tmp


def currentHumidity(humidity):
    tmp = float(humidity)
    if tmp != 0:
        tmp = tmp / 1000
    return tmp


def get():
    info = {}
    TEMP = 0
    HUMIDITY = 0
    while True:
        try:
            TEMP = open('/sys/bus/iio/devices/iio:device0/in_temp_input').read()
            HUMIDITY = open('/sys/bus/iio/devices/iio:device0/in_humidityrelative_input').read()
            TEMP = currentTEMP(TEMP)
            HUMIDITY = currentHumidity(HUMIDITY)
        except:
            TEMP = TEMP + 0.01
            HUMIDITY = HUMIDITY + 0.01

        info["TEMP"] = "%.0f" % TEMP
        info["HUMIDITY"] = "%.0f" % HUMIDITY
        return info

if __name__ == '__main__':
    get()