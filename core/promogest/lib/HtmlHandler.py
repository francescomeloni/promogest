# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2012 by Promotux
#                       di Francesco Meloni snc - http://www.promotux.it/

#    Author: Francesco Meloni  <francesco@promotux.it>
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


import os
import sys
from datetime import datetime
from promogest.ui.gtk_compat import *
from threading import Timer
from promogest.lib import feedparser

from gi.repository.WebKit import WebView
from gi.repository.WebKit import WebSettings
WEBKIT = True
import urllib2
import webbrowser
from promogest import Environment
from  promogest.lib import utils
from promogest.dao import DaoUtils as daoutils
from jinja2 import Environment  as Env
from jinja2 import FileSystemLoader,FileSystemBytecodeCache,environmentfilter, Markup, escape
import re

templates_dir = [os.path.join('templates'),os.path.join('report-templates')]
jinja_env = None

def env(templates_dir):
    jinja_env = Env(loader=FileSystemLoader(templates_dir),
                    extensions=['jinja2.ext.i18n',"jinja2.ext.do"])
# Era un parametro della classe Env  bytecode_cache=FileSystemBytecodeCache(os.path.join(Environment.promogestDir, 'temp'), '%s.cache'),
    jinja_env.globals['environment'] = Environment
    jinja_env.globals['utils'] = utils
    jinja_env.globals['daoutils'] = daoutils
    jinja_env.globals['datetime'] = datetime
    jinja_env.filters['dateformat'] = dateformat
    jinja_env.filters['datetimeformat'] = datetimeformat
    jinja_env.filters['nl2br'] = nl2br
    jinja_env.filters['nonone'] = noNone
    jinja_env.filters['uu'] = uu
    try:
        # installa gettext per i18n
        jinja_env.install_gettext_callables(_, ngettext, newstyle=True)
        jinja_env.globals.update({
            '_': _,
            'ngettext': ngettext
        })
    except:
        pass
    return jinja_env

def datetimeformat(value, format='%d/%m/%Y %H:%M '):
    if not value:
        return ""
    else:
        return value.strftime(format)

def dateformat(value, format='%d/%m/%Y '):
    if not value:
        return ""
    else:
        return value.strftime(format)

def noNone(value):
    if value =="None":
        return ""
    elif not value:
        return ""
    else:
        return value

def uu(value):
    from utils import uu as uuu
    return uuu(value)

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@environmentfilter
def nl2br(eval_ctx, value):
    if value:
        result =  '<br />\n'.join(value.split('\n'))
        if eval_ctx.autoescape:
            result = Markup(result)
        return result
    else:
        return ""


"""
    createHtmlObj = restituisce un oggetto del render html o gtkhtml2 o webkit
    renderHTMLTemplate o renderTemplate = Restituiscono una stringa html dopo la
                                            renderizzazione del template engine
    renderHTML = inserisce il codice html dentro l'oggetto
"""
def apriAnagraficaArticoliEdit(articoloId):
    from promogest.ui.anagArti.AnagraficaArticoli import AnagraficaArticoli
    from promogest.ui.anagArti.AnagraficaArticoliEdit import AnagraficaArticoliEdit
    from promogest.dao.Articolo import Articolo
    a = AnagraficaArticoli()
    art = Articolo().getRecord(id=articoloId)
    a.on_record_edit_activate(a, dao=art)

def apriTestataDocumentoEdit(testataDocumentoId):
    from promogest.ui.anagDocumenti.AnagraficaDocumenti import AnagraficaDocumenti
#    from promogest.ui.AnagraficaDocumentiEdit import AnagraficaDocumentiEdit
    from promogest.dao.TestataDocumento import TestataDocumento
    a = AnagraficaDocumenti()
    art = TestataDocumento().getRecord(id=testataDocumentoId)
    a.on_record_edit_activate(a, dao=art)

def apriTestataMovimentoEdit(testataMovimentoId):
    from promogest.ui.anagMovimenti.AnagraficaMovimenti import AnagraficaMovimenti
    from promogest.dao.TestataMovimento import TestataMovimento
    a = AnagraficaMovimenti()
    art = TestataMovimento().getRecord(id=testataMovimentoId)
    a.on_record_edit_activate(a, dao=art)

def apriAnagraficaPromemoriaNew(selectedData=None):
    from promogest.ui.anagPromemoria.AnagraficaPromemoria import AnagraficaPromemoria
    a = AnagraficaPromemoria(selectedData=selectedData)
    a.on_record_new_activate(a)

def apriAnagraficaPromemoriaEdit(promemoriaId):
    from promogest.ui.anagPromemoria.AnagraficaPromemoria import AnagraficaPromemoria
    from promogest.dao.Promemoria import Promemoria
    a = AnagraficaPromemoria()
    pro = Promemoria().getRecord(id=promemoriaId)
    a.on_record_edit_activate(a, dao=pro)


def renderPage(feedToHtml):
    """ show the html page in the custom widget"""
    pageData = {
            "file" :"feed.html",
            "objects" :feedToHtml,
            }
    html = renderTemplate(pageData)
    renderHTML(Environment.htmlwidget,html.decode("utf-8"))

def getfeedFromSite():
    string = ""
    if Environment.feedAll == "":
        d = feedparser.parse("http://www.promogest.me/newsfeed")
    else:
        d = Environment.feedAll
    feedList = d['entries']
    feedToHtml = []
    for feed in feedList[0:3]:
        try:
            body = feed['content'][0]['value']
        except:
            body = feed["summary_detail"]['value']
        feed = {
            "title" :feed['title'],
            "links": feed['links'][0]['href'],
            "body" : body,
            "updated" : feed['updated'][4:-13],
            "autore" : feed['author']
            }
        feedToHtml.append(feed)
    Environment.feedCache = feedToHtml
    renderPage(feedToHtml)


def _on_navigation_requested(view, frame, req, data=None):
    uri = req.get_uri()
    if uri.startswith("program:/"):
        agg = uri.split("/")[1]
        if "articoloId" in agg:
            exec(agg)
            apriAnagraficaArticoliEdit(articoloId)
        elif "newPromemoria" in agg:
            data = agg.split("=")[1].replace("-","/")
            dta = data.split("/")
            datadef = dta[2]+"/"+dta[1]+"/"+dta[0]
            selectedData = datadef+" 09:00"
            apriAnagraficaPromemoriaNew(selectedData=selectedData)
        elif "promemoriaId" in agg:
            exec(agg)
            apriAnagraficaPromemoriaEdit(promemoriaId)
        elif "testataDocumentoId" in agg:
            try:
                exec(agg)
                apriTestataDocumentoEdit(testataDocumentoId)
            except:
                return
        elif "testataMovimentoId" in agg:
            try:
                exec(agg)
                apriTestataMovimentoEdit(testataMovimentoId)
            except:
                return
        elif "recuperafeed" in agg:
            if utils.setconf("Feed", "feed"):
                feedAll = Environment.feedAll
                feedToHtml = Environment.feedCache
                if feedAll != "" and feedAll and feedToHtml:
                    renderPage(feedToHtml)
                else:
                    gobject.idle_add(getfeedFromSite)
    elif "ads" in uri or "cdn" in uri:
        return False
    elif "http" in uri:
        linkOpen(uri)
    else:
        return False
    return True

def createHtmlObj(mainWidget,widget=None):
    a= WebView()
    a.connect('navigation-requested', _on_navigation_requested,a)
    return a

#@utils.timeit
def renderTemplate(pageData):
    jinja_env.globals['environment'] = Environment
    jinja_env.globals['utils'] = utils
    pageData["titolo"] = pageData["file"].split(".")[0].capitalize()
    if "dao" in pageData:
        html = jinja_env.get_template("/"+pageData["file"]).render(pageData = pageData, dao=pageData["dao"])
    else:
        html = jinja_env.get_template("/"+pageData["file"]).render(pageData = pageData)
    return html


def _on_html_request_url(document, url, stream):
    def render():
        try:
            f = open(url, 'rb')
            stream.write(f.read())
            f.close()
            stream.close()
        except:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            t = Timer(5.0, response.close)
            t.start()
            html = response.read()
            stream.write(html)
            stream.close()
    gobject.idle_add(render)

def linkOpen(link):
    webbrowser.open_new_tab(link)

def _on_html_link_clicked(url, link):
    agg = link.split("/")[1]
    if "articoloId" in agg:
        exec(agg)
        apriAnagraficaArticoliEdit(articoloId)
    elif "newPromemoria" in agg:
            apriAnagraficaPromemoriaNew()
    else:
        gobject.idle_add(linkOpen, link)
    return True

def renderHTMLTemplate(pageData):
    return renderTemplate(pageData)

def renderHTML(widget, html):

    c = WebSettings()
    c.set_property('user-agent', None)
    c.set_property("minimum_font_size", 8)
    c.set_property("javascript-can-open-windows-automatically", True)
    c.set_property("default-encoding", "Utf-8")
    c.set_property("enable-file-access-from-file-uris", True)
    c.set_property("enable-universal-access-from-file-uris", True)
    c.set_property("enable-site-specific-quirks", True)
    widget.set_settings(c)
    widget.load_html_string(html, "file:///"+sys.path[0]+os.sep)
    widget.show()

