# -*- coding: utf-8 -*-
'''
Created on 10.05.2009

@author: mgla
'''

import datum
from CONST import *
from ernte import Ernte

class Filter(object):
    '''Klasse zum Filtern von Ergebnissen'''
    def __init__(self,
                 ernten = [Ernte(datum.monatZuDatum(MONATE[0]), datum.monatZuDatum(MONATE[12]))],
                 landschaften = range(ANZAHL_LANDSCHAFTEN),
                 typ = "Heilpflanze",
                 koordinaten = (0,0)
                 ):
        self.__ernten = ernten
        self.__landschaften = landschaften
        self.__typ = typ
        self.__koordinaten = koordinaten


    def getLandschaften(self):
        return self.__landschaften


    def getTyp(self):
        return self.__typ


    def getKoordinaten(self):
        return self.__koordinaten


    def setLandschaften(self, value):
        self.__landschaften = value


    def setTyp(self, value):
        self.__typ = value


    def setKoordinaten(self, value):
        self.__koordinaten = value

    
        