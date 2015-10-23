# -*- coding: utf-8 -*-

'''
Created on 10.05.2009
@author: Maik Glatki
'''

MONATE = ["Praios", "Rondra", "Efferd", "Travia", "Boron", "Hesinde", "Firun", "Tsa", "Phex", "Peraine", "Ingerimm", "Rahja", "Namenlose Tage"]
JAHRESANFANG = 0
JAHRESENDE = 365

LANDSCHAFT_EIS       = "Eis"
LANDSCHAFT_WUESTE    = "Wüste und Wüstenrand"
LANDSCHAFT_GEBIRGE   = "Gebirge"
LANDSCHAFT_HOCHLAND  = "Hochland"
LANDSCHAFT_STEPPE    = "Steppe"
LANDSCHAFT_GRASLAND  = "Grasland, Wiesen"
LANDSCHAFT_FLUSS     = "Fluss- und Seeufer, Teiche"
LANDSCHAFT_KUESTE    = "Küste, Strand"
LANDSCHAFT_FLUSSAUEN = "Flussauen"
LANDSCHAFT_SUMPF     = "Sumpf und Moor"
LANDSCHAFT_REGENWALD = "Regenwald"
LANDSCHAFT_WALD      = "Wald"
LANDSCHAFT_WALDRAND  = "Waldrand"
LANDSCHAFT_SONSTIGES = "Sonstiges"

LANDSCHAFTEN = {LANDSCHAFT_EIS      :0,
                LANDSCHAFT_WUESTE   :1,
                LANDSCHAFT_GEBIRGE  :2,
                LANDSCHAFT_HOCHLAND :3,
                LANDSCHAFT_STEPPE   :4,
                LANDSCHAFT_GRASLAND :5,
                LANDSCHAFT_FLUSS    :6,
                LANDSCHAFT_KUESTE : 7,
                LANDSCHAFT_FLUSSAUEN : 8,
                LANDSCHAFT_SUMPF : 9,
                LANDSCHAFT_REGENWALD : 10,
                LANDSCHAFT_WALD: 11,
                LANDSCHAFT_WALDRAND: 12,
                LANDSCHAFT_SONSTIGES: 13}

ANZAHL_LANDSCHAFTEN = len(LANDSCHAFTEN.keys())
print LANDSCHAFTEN.keys()
print ANZAHL_LANDSCHAFTEN

def checkDatum(datum):
    if ((datum < JAHRESANFANG) or (datum > JAHRESENDE)):
        raise Exception(("Datum außerhalb des zulässigen Bereichs [%s, %s]" % (JAHRESANFANG,JAHRESENDE)), datum)
    
if __name__ == "__main__":
    ''' DEBUG '''
    print "JAHRESANFANG:", JAHRESANFANG
    print "JAHRESENDE:",   JAHRESENDE
    print "LANDSCHAFTEN:", LANDSCHAFTEN
    print "LANDSCHAFTEN.keys():", LANDSCHAFTEN.keys()
    print "ANZAHL_LANDSCHAFTEN:", ANZAHL_LANDSCHAFTEN 