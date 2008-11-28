# -*- coding: iso-8859-15 -*-

# Promogest
#
# Copyright (C) 2005 by Promotux Informatica - http://www.promotux.it/
# Author: Andrea Argiolas <andrea@promotux.it>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import gtk
import gobject
from GladeWidget import GladeWidget

from promogest import Environment
from promogest.dao.Dao import Dao
import promogest.dao.Listino
from promogest.dao.Listino import Listino

from utils import *



class ElencoListini(GladeWidget):
    """ Elenco listini """

    def __init__(self, mainWindow, aziendaStr):
        self._mainWindow = mainWindow
        self.aziendaStr = aziendaStr
        self._currentDao = None
        GladeWidget.__init__(self, 'elenco_listini_frame', fileName='_elenco_listini_elements.glade')
        self.orderBy = 'denominazione'
        self.draw()


    def draw(self):
        # Colonne della Treeview dell' elenco
        treeview = self.elenco_listini_treeview
        renderer = gtk.CellRendererText()

        column = gtk.TreeViewColumn('Denominazione', renderer, text=1)
        column.set_sizing(gtk.TREE_VIEW_COLUMN_GROW_ONLY)
        column.set_clickable(True)
        column.connect("clicked", self._changeOrderBy, 'denominazione')
        column.set_resizable(True)
        column.set_expand(False)
        column.set_min_width(150)
        treeview.append_column(column)

        column = gtk.TreeViewColumn('Descrizione', renderer, text=2)
        column.set_sizing(gtk.TREE_VIEW_COLUMN_GROW_ONLY)
        column.set_clickable(True)
        column.connect("clicked", self._changeOrderBy, 'descrizione')
        column.set_resizable(True)
        column.set_expand(True)
        column.set_min_width(200)
        treeview.append_column(column)

        column = gtk.TreeViewColumn('Data listino', renderer, text=3)
        column.set_sizing(gtk.TREE_VIEW_COLUMN_GROW_ONLY)
        column.set_clickable(True)
        column.connect("clicked", self._changeOrderBy, 'data_listino')
        column.set_resizable(True)
        column.set_expand(False)
        column.set_min_width(100)
        treeview.append_column(column)

        treeview.set_search_column(1)

        model = gtk.ListStore(object, str, str, str)
        treeview.set_model(model)

        self.refresh()


    def show_all(self):
        """ Visualizza/aggiorna tutta la struttura dell'elenco """
        self._elenco_listini_elements.show_all()


    def refresh(self):
        # Aggiornamento Treeview
        model = self.elenco_listini_treeview.get_model()
        model.clear()

        liss = Listino(isList=True).select(orderBy='denominazione',
                                            batchSize=None,
                                            offset=None)

        for l in liss:
            model.append((l,
                          (l.denominazione or ''),
                          (l.descrizione or ''),
                          dateToString(l.data_listino)))
        if "ImportPriceList" not in Environment.modulesList:
            self.importazione_listini_togglebutton.set_sensitive(False)

    def _changeOrderBy(self, widget, campi):
        print "CAMBI L?ORDINE", campi
        self.orderBy = campi
        self.refresh()


    def on_elenco_listini_treeview_cursor_changed(self, treeview):
        sel = treeview.get_selection()
        (model, iterator) = sel.get_selected()
        if iterator is not None:
            self._currentDao = model.get_value(iterator,0)


    def on_elenco_listini_treeview_row_activated(self, treeview, path, column):
        self.articoli_listino_togglebutton.set_active(True)


    def on_listini_togglebutton_clicked(self, toggleButton):
        if not(toggleButton.get_active()):
            toggleButton.set_active(False)
            return

        denominazione = None
        if self._currentDao is not None:
            denominazione = self._currentDao.denominazione
        from AnagraficaListini import AnagraficaListini
        anag = AnagraficaListini(denominazione, self.aziendaStr)
        anagWindow = anag.getTopLevel()

        showAnagraficaRichiamata(self._mainWindow, anagWindow, toggleButton, self.refresh)


    def on_articoli_listino_togglebutton_clicked(self, toggleButton):
        if not(toggleButton.get_active()):
            toggleButton.set_active(False)
            return

        idListino = None
        if self._currentDao is not None:
            idListino = self._currentDao.id
        from AnagraficaListiniArticoli import AnagraficaListiniArticoli
        anag = AnagraficaListiniArticoli(None, idListino, self.aziendaStr)
        anagWindow = anag.getTopLevel()

        showAnagraficaRichiamata(self._mainWindow, anagWindow, toggleButton, self.refresh)

    def on_importazione_listini_togglebutton_clicked(self, toggleButton):
        from promogest.modules.ImportPriceList.ui.ImportPriceList import ImportPriceList
        if not(toggleButton.get_active()):
            toggleButton.set_active(False)
            return

        idListino = None
        if self._currentDao:
            idListino = self._currentDao.id
        anag = ImportPriceList(self._mainWindow)
        anagWindow = anag.getTopLevel()

        showAnagraficaRichiamata(self._mainWindow, anagWindow, toggleButton)

