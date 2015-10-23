# -*- coding: utf-8 -*-
'''
Created on 10.05.2009

@author: mgla
'''
from CONST import checkDatum
class Ernte:
    """ Diese Klasse realisiert eine Erntezeit einer Pflanze"""
    
    def __init__(self, von, bis):
        checkDatum(von)
        checkDatum(bis)
        self.von = von
        self.bis = bis
    
    def istErntezeit(self, datum):
        if ((self.von <= datum) and (datum <= self.bis)):
            return 1
        else:
            return 0
        