# -*- coding: utf-8 -*-

'''
Created on 08.05.2009
@author: Maik Glatki
'''

import datum
from pflanzenfilter import Ernte
from pflanze import Pflanze 
"""
Sehr häufig: +1
Häufig: +2
Gelegentlich: +4
Selten: +8
Sehr selten: +16
"""

def pflanzenListe():
    liste = {}
    liste["Defaultkraut"] = Pflanze("Defaultkraut",
                                    bestimmung=5,
                                    verbreitung={
                                        "Eis": 16,
                                        "Wüste und Wüstenrand": 0,
                                        "Gebirge":0,
                                        "Hochland":0,
                                        "Steppe":0,
                                        "Grasland, Wiesen":0,
                                        "Fluss- und Seeufer, Teiche":0,
                                        "Küste, Strand":0,
                                        "Flussauen":0,
                                        "Sumpf und Moor":0,
                                        "Regenwald":0,
                                        "Wald":0,
                                        "Waldrand":0,
                                        "Sonstiges": (0, "Kommentar")
                                    },
                                    ernten=[Ernte(datum.monatZuDatum("Praios") + 0, datum.monatZuDatum("Namenlose Tage") + 5)]
                                    )
    liste["Vierblättrige Einbeere"] = Pflanze("Vierblättrige Einbeere",
                                              bestimmung = 5,
                                              verbreitung = 
                                              {"Eis": 16,
                                               "Gebirge":16,
                                               "Hochland":16,
                                               "Steppe":16,
                                               "Grasland, Wiesen":4,
                                               "Fluss- und Seeufer, Teiche":16,
                                               "Küste, Strand":16,
                                               "Flussauen":16,
                                               "Sumpf und Moor":16,
                                               "Wald":2,
                                               "Waldrand":2,
                                               "Sonstiges": (0, "Kommentar")
                                               },
                                               ernten = [Ernte(datum.monatZuDatum("Phex"), datum.monatZuDatum("Praios")),
                                                         Ernte(datum.monatZuDatum("Praios"), datum.monatZuDatum("Hesinde") + 30)]
                                               )
                                                               

    return liste

