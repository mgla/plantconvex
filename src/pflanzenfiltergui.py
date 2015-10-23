# -*- coding: utf-8 -*-

'''
Created on 08.05.2009
@author: Maik Glatki
'''

import pygtk
pygtk.require('2.0')
import gtk
from gtk import gdk
from CONST import *

class pflanzenfiltergui:

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        #### GUI ####
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("pflanzenfilter - GUI")

        # handler exit gtk
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)

## HBox Toolbar
        self.HBoxToolbar = gtk.HBox(False, 5)
        "Obere Leiste für Buttons, Datumsauswahl, evtl. Filter"

        self.button1 = gtk.Button("button1")
        self.HBoxToolbar.pack_start(self.button1, expand=False)
#        self.buttonCalcDPS.connect("clicked", self.calcDPS)        
        self.button2 = gtk.Button("button2")
        self.HBoxToolbar.pack_start(self.button2, expand=False)
        self.LabelMonat = gtk.Label("Monat:")
        self.HBoxToolbar.pack_start(self.LabelMonat, False)
        "Dropdown box"
        self.DropdownMonat = gtk.combo_box_entry_new_text()        
        for mon in MONATE:
            self.DropdownMonat.append_text(mon)
        self.DropdownMonat.set_active(0)
        self.HBoxToolbar.pack_start(self.DropdownMonat, False)
        self.HBoxToolbar.show()
        self.HBoxToolbar.show_all()
     
## VBox Sidebar
        "Sidebar für Koordinaten und Ergebnisse"
        self.VBoxSidebar = gtk.VBox(False,2)
    # Label
        self.LabelTitel = gtk.Label("Ergebnisse:")
        self.VBoxSidebar.pack_start(self.LabelTitel, expand=False)
        self.Ergebnisse = gtk.ListStore(str, str) # 2x Strings
        self.VBoxSidebar.show_all()
        
## AscpectFrame Karte
        
        "Große Angezeigte Karte"
        self.KartenFrame = gtk.Frame()
    # Karte
        self.ImageKarte = gtk.Image()
        # 2000x2731
        scale = 2731.0/2000.0
        width = 600
        self.ImageKarte.set_from_pixbuf(gdk.pixbuf_new_from_file("karte.png").scale_simple(width,int(round(width*scale)),gtk.gdk.INTERP_BILINEAR))
        self.ImageKarte.show()
        self.KartenFrame.add(self.ImageKarte)
        self.KartenFrame.show()
                
## HBox Main
        "Teil unter der Buttonleiste"
        self.HBoxMain = gtk.HBox(False, 5)
        self.HBoxMain.pack_start(self.VBoxSidebar, expand=False)
        self.HBoxMain.pack_start(self.KartenFrame, expand=False)
        self.HBoxMain.show()
        
## Vbox Gesamt
        "Gesamte Oberfläche"
        self.VBoxAll = gtk.VBox(False, 5)
        self.window.add(self.VBoxAll)

        self.VBoxAll.pack_start(self.HBoxToolbar, True, True, 0)
        self.VBoxAll.pack_start(self.HBoxMain, True, True, 0)
        self.VBoxAll.show()        
        # Destroyer
        self.window.connect("destroy", self.destroy)
        # Fenster zeigen
        self.window.show()

    def main(self):
        # Auf Events warten        
        gtk.main()

# Wenn Programm direkt gestartet wird, dann GUI starten
if __name__ == "__main__":
    GUI = pflanzenfiltergui()
    GUI.main()
