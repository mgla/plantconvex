# -*- coding: utf-8 -*-

'''
Created on 08.05.2009
@author: Maik Glatki
'''

def monatZuDatum(monat):
    monate = {"Praios":0, "Rondra":1, "Efferd":2, "Travia":3,
                 "Boron":4, "Hesinde":5, "Firun":6, "Tsa":7,
                 "Phex":8, "Peraine":9, "Ingerimm":10, "Rahja":11,
                 "Namenlose Tage":12}
    if (monate.has_key(monat)):
        return monate[monat] * 30
    else:
        raise Exception("Monat unbekannt",monat)
def macheDatum((tag,monat)):
    return monatZuDatum(monat) *  tag -1
    
