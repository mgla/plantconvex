# -*- coding: utf-8 -*-

'''
Created on 08.05.2009
@author: Maik Glatki
'''

from ernte import Ernte

class Pflanze:
    def __init__(self, name, bestimmung = 0, verbreitung = {}, ernten = Ernte(0,365)):
        self.name = name
        self.bestimmung = bestimmung
        self.verbreitung = {}
        self.ernten = ernten
 
    def erntezeit(self, datum):
        "Prüft ob eine Pflanze im moment erntbar ist."
        for e in self.ernten:
            if e.istErntezeit(datum):
                return True
        return False
        
    def getName(self):
        return self.name
