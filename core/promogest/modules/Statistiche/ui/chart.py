# -*- coding: utf-8 -*-

# Promogest
#
# Copyright (C) 2005 by Promotux Informatica - http://www.promotux.it/
# Author: Andrea Argiolas <andrea@promotux.it>
# Author: Francesco Meloni  <francesco@promotux.it>

import matplotlib.pyplot as plt
import gtk
from matplotlib.figure import Figure
from numpy import arange, sin, pi

from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas

from matplotlib.backends.backend_gtkagg import NavigationToolbar2GTKAgg as NavigationToolbar

class chartViewer():
    def __init__(self, func= None, scontrini = None):
        member = getattr(self, func)
        self.fig = member(scontrini=scontrini)
        self.draw(func)

    def draw(self,func):

        win = gtk.Window()
        win.connect("destroy", lambda x: gtk.main_quit())
        win.set_default_size(800,600)
        win.set_title("Chart statistiche PromoGest2")
        vbox = gtk.VBox()

        win.add(vbox)
        sw = gtk.ScrolledWindow()
        vbox.pack_start(sw)
        sw.set_border_width (10)
        sw.set_policy (hscrollbar_policy=gtk.POLICY_AUTOMATIC,
               vscrollbar_policy=gtk.POLICY_ALWAYS)

        canvas = FigureCanvas(self.fig)  # a gtk.DrawingArea

        sw.add_with_viewport (canvas)
        toolbar = NavigationToolbar(canvas, win)
        toolbar.set_message(func)
        vbox.pack_start(toolbar, False, False)
        win.show_all()
        gtk.main()

    def affluenzaOrariaGiornaliera(self, scontrini=None):
        """ TODO: Avvisare con un messaggio quando i dati non sono omogenei
            esempio ci sono più giorni negli scontrini """
        ore = []
        if scontrini:
            for sco in scontrini:
                ore.append(sco.data_inserimento.hour)
        f = plt.figure()
        ax = f.add_subplot(111)

        plt.plot([a for a in range(8,25)], [ore.count(b) or 0 for b in range(8,25)], color='red',label='Q/h',linewidth=2)

        ax.xaxis.set_major_locator(plt.FixedLocator(range(8,25)))
        ax.yaxis.set_major_locator(plt.FixedLocator(range(0,len(ore)+1)))

        plt.ylabel('Numero scontrini emessi')
        plt.xlabel('Orario 8,00 alle 24,00')

        plt.axis()
        plt.legend()
        plt.grid(True)
        return f

    def affluenzaGiornalieraMensile(self, scontrini=None):
        """ TODO: Avvisare con un messaggio quando i dati non sono omogenei
            esempio ci sono più mesi negli scontrini """
        giorni = []
        if scontrini:
            for sco in scontrini:
                giorni.append(sco.data_inserimento.day)
        f = plt.figure()
        ax = f.add_subplot(111)

        plt.plot([a for a in range(1,32)], [giorni.count(b) or 0 for b in range(0,31)], color='green',label='Q/h',linewidth=2)

        ax.xaxis.set_major_locator(plt.FixedLocator(range(1,32)))
        ax.yaxis.set_major_locator(plt.FixedLocator(range(0,len(giorni)+1)))

        plt.ylabel('Numero scontrini emessi')
        plt.xlabel('Giorni del mese')

        plt.axis()
        plt.legend()
        plt.grid(True)
        return f
