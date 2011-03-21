# -*- coding: utf-8 -*-

#    Copyright (C) 2005, 2006, 2007 2008, 2009, 2010 by Promotux
#                        di Francesco Meloni snc - http://www.promotux.it/

# Author: Alceste Scalas <alceste@promotux.it>
# Author: Andrea Argiolas <andrea@promotux.it>
# Author: Francesco Meloni <francesco@promotux.it

#    This file is part of Promogest.

#    Promogest is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.

#    Promogest is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Promogest.  If not, see <http://www.gnu.org/licenses/>.

import time
import gtk
import gobject
import os
import sys
import threading
import os.path
from promogest.Environment import conf
from GladeWidget import GladeWidget
from promogest.ui.widgets.FilterWidget import FilterWidget
from promogest.lib.XmlGenerator import XlsXmlGenerator
from promogest.lib.CsvGenerator import CsvFileGenerator
from utils import *
import Login
import subprocess ,shlex
from promogest import Environment
from calendar import Calendar
#if Environment.new_print_enjine:
from promogest.lib.sla2pdf.Sla2Pdf_ng import Sla2Pdf_ng
from promogest.lib.sla2pdf.SlaTpl2Sla import SlaTpl2Sla as SlaTpl2Sla_ng
from promogest.lib.SlaTpl2Sla import SlaTpl2Sla
#else:


from promogest.ui.SendEmail import SendEmail
from promogest.lib.HtmlHandler import createHtmlObj, renderTemplate, renderHTML
from promogest.dao.Azienda import Azienda


class AnagraficaPrintPreview(GladeWidget):
    """ Print preview """
    # FIXME: a lot of duplicated code from AnagraficaFilter here!

    def __init__(self, anagrafica, windowTitle, previewTemplate):
        GladeWidget.__init__(self, 'htmlviewer')
        self.windowTitle = windowTitle
        self.visualizzatore_html.set_title(windowTitle)
        self._anagrafica = anagrafica

        self.bodyWidget = FilterWidget(owner=self, resultsElement='html')
        self.html_scrolledwindow.add_with_viewport(self.bodyWidget.getTopLevel())
#        self.bodyWidget.filter_body_label.set_no_show_all(True)
#        self.bodyWidget.filter_body_label.set_property('visible', False)

        self.print_on_screen_html = self.bodyWidget.resultsElement
        self._gtkHtmlDocuments = None # Will be filled later
        self._previewTemplate = previewTemplate
        self.html = createHtmlObj(self)
        self._changeOrderBy = self.bodyWidget._changeOrderBy
        self.orderBy = self.bodyWidget.orderBy
        self.batchSize = self.bodyWidget.batchSize
        self.offset = self.bodyWidget.offset
        self.numRecords = self.bodyWidget.numRecords
        self._filterClosure = self._anagrafica.filter._filterClosure
        self._filterCountClosure = self._anagrafica.filter._filterCountClosure
        #self._allResultForHtml = self._anagrafica.filter._allResultForHtml
#        self.visualizzatore_html.set_transient_for(self._anagrafica.getTopLevel())
        self.placeWindow(self.visualizzatore_html)


        self.codBar_combo = gtk.combo_box_new_text()
        self.codBar_combo.append_text("Genera Pdf Anteprima Html")
        self.codBar_combo.append_text("Genera CSV da Anteprima Html")
        self.bodyWidget.hbox1.pack_start(self.codBar_combo)
        self.codBar_combo.connect('changed', self.on_generic_combobox_changed )

        self.bodyWidget.generic_button.set_no_show_all(True)
        self.bodyWidget.generic_button.set_property('visible', False)
        #generaButton = self.bodyWidget.generic_button
        #generaButton.connect('clicked', self.on_generic_button_clicked )
        #generaButton.set_label("Genera Pdf Anteprima Html")
        self.refresh()

    def on_pdf_button_clicked(self, button):
        from PrintDialog import PrintDialogHandler
        try:
            import ho.pisa as pisa
        except:
            print "ERRORE NELL'IMPORT DI PISA"
#                import pisaLib.ho.pisa as pisa
            return
        f = self.html_code
        g = file(Environment.tempDir+".temp.pdf", "wb")
        pdf = pisa.CreatePDF(str(f),g)
        g .close()
        anag = PrintDialogHandler(self,self.windowTitle)
        anagWindow = anag.getTopLevel()
        returnWindow = self.bodyWidget.getTopLevel().get_toplevel()
        anagWindow.set_transient_for(returnWindow)
        anagWindow.show_all()

    def on_csv_button_clicked(self, button):
        messageInfo(msg="NON ANCORA IMPLEMENTATO")


    def on_generic_combobox_changed(self,combobox):
        if self.codBar_combo.get_active()==0:
            from PrintDialog import PrintDialogHandler
            try:
                import ho.pisa as pisa
            except:
                print "ERRORE NELL'IMPORT DI PISA"
#                import pisaLib.ho.pisa as pisa
                return
            f = self.html_code
            g = file(Environment.tempDir+".temp.pdf", "wb")
            pdf = pisa.CreatePDF(str(f),g)
            g .close()
            anag = PrintDialogHandler(self,self.windowTitle)
            anagWindow = anag.getTopLevel()
            returnWindow = self.bodyWidget.getTopLevel().get_toplevel()
            anagWindow.set_transient_for(returnWindow)
            anagWindow.show_all()
            #self.codBar_combo.set_active(0)
        elif self.codBar_combo.get_active()==1:
            print "ANTEPRIMA CSV"
        else:
            self.codBar_combo.set_active(-1)

    def _refreshPageCount(self):
        """ Aggiorna la paginazione """
        self.bodyWidget.numRecords = self.numRecords
        self.bodyWidget._refreshPageCount()

    def refresh(self):
        """ show the html page in the custom widget"""
        self.bodyWidget.orderBy = self.orderBy
        daos = self.bodyWidget.runFilter(offset=None, batchSize=None,
                                         filterClosure=self._filterClosure)
        self.numRecords = self.bodyWidget.countFilterResults(self._filterCountClosure)
        self._refreshPageCount()
        pageData = {}
        self.html_code = "<html><body></body></html>"
        if daos:
            pageData = {
                    "file" :self._previewTemplate[1],
                    "dao":daos,
                    "objects":daos
                    }
            self.html_code = renderTemplate(pageData)
        renderHTML(self.print_on_screen_html,self.html_code)

    def on_print_on_screen_dialog_response(self, dialog, responseId):
        if responseId == gtk.RESPONSE_CLOSE:
            self.on_print_on_screen_dialog_delete_event()

    def on_print_on_screen_dialog_delete_event(self, dialog=None, event=None):
        self.destroy()