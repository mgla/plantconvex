# -*- coding: utf-8 -*-

'''
Created on 08.05.2009
@author: Maik Glatki
'''

import pflanzen
from ernte import Ernte
import datum
from filter import Filter

"""
DSA-Kräuterfilter
Author: Maik Glatki
"""
class Pflanzenfilter:
    def __init__(self):
        self.Liste = pflanzen.pflanzenListe()
    
    def getPflanzenByDatum(self, datum):
        res = []
        for p in self.Liste.keys():
            if self.Liste[p].erntezeit(datum) == True:
                res.append(self.Liste[p].getName())
        return res
    
    def getPflanzenByFilter(self, filter):
        '''Filtert Pflanzen nach Orts, Landschafts und Zeitfilter'''
        # (Name, Suchschwierigkeit, [Heil/Giftpflanze]
        res = []
        for item in self.Liste.keys(): # Iteriere über alle Pflanzen in der Datenbank
            p = self.Liste[item]
            # TODO: Abgleich der Erntezeiten
            # TODO: Abgleich der Landschaften
            # TODO: Abgleich der Pflanzentypen
            # TODO: Abgleich nach Koordinaten
            # TODO: Besonderes: (Ruinen, Höhlen, etc)
        
if __name__ == "__main__":
    print "Pflanzenfilter Testmodul"
    pFilter = Pflanzenfilter()
    res = pFilter.getPflanzenByDatum(datum.monatZuDatum("Hesinde"))
    fil = Filter()
    print res
    