# -*- coding: utf-8 -*-
from NeuroPy import NeuroPy
from time import sleep
import threading
from api_service import *

neuropy = NeuroPy("COM4")  # type: NeuroPy
#neuropy = NeuroPy("/dev/rfcomm0",57600)  # type: NeuroPy

def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return 0

def meditation_callback(meditation_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of meditation is: ", meditation_value)
    return 1

def rawValue_callback(rawValue_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
   # print ("Value of rawValue is: ", rawValue_value)
    return 2

def delta_callback(delta_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of delta is: ", delta_value)
    return 3

#callbacks_sensor = []

#aten = neuropy.setCallBack("attention", attention_callback)
#medi = neuropy.setCallBack("meditation", meditation_callback)
#neuropy.setCallBack("rawValue", rawValue_callback)
#delta = neuropy.setCallBack("delta", delta_callback)

#print("saida",delta ,medi, aten)


def start_capture(datas_user):    
    neuropy.start()
    while True:
        sleep(1)

        send_datas(datas_user,neuropy)

        print( neuropy.attention,
            neuropy.meditation,
            neuropy.rawValue,
            neuropy.delta,
            neuropy.theta,
            neuropy.lowAlpha,
            neuropy.highAlpha,
            neuropy.lowBeta,
            neuropy.highBeta,
            neuropy.lowGamma,
            neuropy.midGamma,
            neuropy.poorSignal,
            neuropy.blinkStrength)


try:
    while True:
        sleep(0.2)
finally:
    neuropy.stop()