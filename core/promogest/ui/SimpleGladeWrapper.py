# -*- coding: utf-8 -*-

"""
 Derived from:
 SimpleGladeApp.py
 Module that provides an object oriented abstraction to pygtk and libglade.
 Copyright (C) 2004 Sandino Flores Moreno
"""

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

from __future__ import division
import os
import re
import warnings

with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter('ignore')
import tokenize
from promogest import Environment
from promogest.ui.gtk_compat import *
import weakref
import inspect
import os.path, warnings

__version__ = "1.0"
__author__ = 'Sandino "tigrux" Flores-Moreno'


class SimpleGladeWrapper:
    """ """
    def __init__(self, path=None, root=None, domain=None,\
                            callbacks_proxy=None, isModule=False, **kwargs):
        """
        Load a glade file specified by glade_filename, using root as
        root widget and domain as the domain for translations.

        If it receives extra named arguments (argname=value), then they are used
        as attributes of the instance.

        path:
            path to a glade filename.
            If glade_filename cannot be found, then it will be searched in the
            same directory of the program (sys.argv[0])

        root:
            the name of the widget that is the root of the user interface,
            usually a window or dialog (a top level widget).
            If None or ommited, the full user interface is loaded.

        domain:
            A domain to use for loading translations.
            If None or ommited, no translation is loaded.

        callbacks_proxy:
            An object for binding callbacks.
            If None or omitted, 'self' will be used

        **kwargs:
            a dictionary representing the named extra arguments.
            It is useful to set attributes of new instances, for example:
                glade_app = SimpleGladeApp("ui.glade", foo="some value", bar="another value")
            sets two attributes (foo and bar) to glade_app.
        """
        gl = None
        prefix = ""
        #GTK3
        pp = './gui/'
        self.glade = None
        #else:
        if path and os.path.exists(pp + prefix + path) and not isModule:
            self.glade_path = pp + prefix + path
        elif path and os.path.exists(pp + path) and not isModule:
            self.glade_path = pp + path
        elif isModule:
            self.glade_path = './promogest/modules/'+ path
            file_glade = prefix + os.path.split(self.glade_path)[1]
            if os.path.exists(os.path.join(os.path.split(self.glade_path)[0], file_glade)):
                self.glade_path = os.path.join(os.path.split(self.glade_path)[0], file_glade)
            else:
                file_glade = os.path.split(self.glade_path)[1]
                self.glade_path = os.path.join(os.path.split(self.glade_path)[0], file_glade)

        #else:
                #glade_dir = os.path.dirname( sys.argv[0] )
                #self.glade_path = os.path.join(glade_dir, path)

        for key, value in kwargs.items():
            try:
                setattr(self, key, weakref.proxy(value))
            except TypeError:
                setattr(self, key, value)
        if not gl:
            gl = gtk.Builder()
            #self.builda = gtk.Buildable()
        gl.set_translation_domain("promogest")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            if os.name=="posix":
                print "FILE GLADE:" + str(self.glade_path)
            gl.add_from_file(self.glade_path)

#        Environment.pg2log.info("FILE GLADE:"+str(self.glade_path))
        self.widgets = gl.get_objects()
        if root:
            self.main_widget = gl.get_object(root)
        #else:
            #self.main_widget = None
        self.normalize_names()
        if callbacks_proxy is None:
            callbacks_proxy = self
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            gl.connect_signals(callbacks_proxy)
        self.gl = gl
        #self.new()


#    def __repr__(self):
#        class_name = self.__class__.__name__
#        if self.main_widget:
##            root = gtk.Widget.get_name(self.main_widget)
#            root = gtk.Buildable.get_name(self.main_widget)
#            repr = '%s(path="%s", root="%s")' % (class_name, self.glade_path, root)
#        else:
#            repr = '%s(path="%s")' % (class_name, self.glade_path)
#        return repr


    def new(self):
        """
        Method called when the user interface is loaded and ready to
        be used.  At this moment, the widgets are loaded and can be
        refered as self.widget_name
        """
        pass


    def add_callbacks(self, callbacks_proxy):
        """
        It uses the methods of callbacks_proxy as callbacks.
        The callbacks are specified by using:
            Properties window -> Signals tab
            in glade-2 (or any other gui designer like gazpacho).

        Methods of classes inheriting from SimpleGladeApp are used as
        callbacks automatically.

        callbacks_proxy:
            an instance with methods as code of callbacks.
            It means it has methods like on_button1_clicked, on_entry1_activate, etc.
        """
        self.glade.signal_autoconnect(callbacks_proxy)


    def normalize_names(self):
        """
        It is internally used to normalize the name of the widgets.
        It means a widget named foo:vbox-dialog in glade
        is refered self.vbox_dialog in the code.

        It also sets a data "prefixes" with the list of
        prefixes a widget has for each widget.
        """
        for widget in self.widgets:
            try:
#                widget_name = gtk.Widget.get_name(widget)
                widget_name = gtk.Buildable.get_name(widget)
                prefixes_name_l = widget_name.split(":")
                prefixes = prefixes_name_l[ : -1]
                widget_api_name = prefixes_name_l[-1]
                widget_api_name = "_".join( re.findall(tokenize.Name, widget_api_name))
                gtk.Widget.set_name(widget, widget_api_name)
                if hasattr(self, widget_api_name):
                    raise AttributeError("instance %s already has an attribute %s" % (self,widget_api_name))
                else:
                    setattr(self, widget_api_name, widget)
                    if prefixes:
                        widget.prefixes = prefixes
                if widget.__gtype__.name == "GtkSpinButton":
                    self.spinSanitaze(widget)
                if widget.__gtype__.name == "UnsignedIntegerEntryField":
                    setattr(widget, "nomee",widget_api_name)
                    self.entryGlobalcb(widget)
                if widget.__gtype__.name == "GtkEntry":
                    self.entryGlobalcb(widget)
            except:
#                pass
                try:
                    widget_name = gtk.Buildable.get_name(widget)
                    prefixes_name_l = widget_name.split(":")
                    prefixes = prefixes_name_l[ : -1]
                    widget_api_name = prefixes_name_l[-1]
                    widget_api_name = "_".join( re.findall(tokenize.Name, widget_api_name))
                    if hasattr(self, widget_api_name):
                        raise AttributeError("instance %s already has an attribute %s" % (self,widget_api_name))
                    else:
                        setattr(self, widget_api_name, widget)
                    if widget.__gtype__.name == "GtkTreeViewColumn":
                        widget.connect("clicked", self._reOrderBy)
                    #print "WIDGET NON WIDGET", widget.get_name(), widget
                except:
                    pass

    def _reOrderBy(self, column):
        pass

    def virgolaAdd(self, spin, event):
        """Funzione che permette di usare il punto del tastierino numerico nelle
        spinbutton di nuova generazione che accettano solo la vurgola per i de
        cimali"""
        c = len(spin.get_text())
        # print(value.string)
        keyval = event.keyval
        name = Gdk.keyval_name(keyval)
        if name == "KP_Decimal":
            a = spin.get_text()
            spin.insert_text(",",c+1)
            spin.set_position(c+2)

    def spinSanitaze(self, spin):
        if spin.get_numeric() and spin.get_digits():
            spin.connect("key-release-event", self.virgolaAdd)

    def onlyDigits(self,entry, event):
        """Funzione di gestione delle entry che accettano SOLO cifre
        per cui sono la riedizione delle vecchie UnSignedIntegerEntryField"""
        controlKeys = (
            'Delete', 'KP_Delete', 'BackSpace', 'Tab', 'ISO_Left_Tab',
            'Left', 'Right', 'Down', 'Up',
            'KP_Left', 'KP_Right', 'KP_Down', 'KP_Up',
            'Home', 'End', 'KP_Home', 'KP_End', 'Return', 'KP_Enter')
        keyval = event.keyval
        name = Gdk.keyval_name(keyval)
        modKeys = ('Ctrl+Mod2+X','Ctrl+Mod2+C', 'Ctrl+Mod2+V')
        mod = Gtk.accelerator_get_label(keyval, event.state)
        # print("NAME",keyval, name, mod)
        if not name.isdigit() and name not in controlKeys and mod not in modKeys:
            return True


    def on_focus_in_event(self, widget, event):
        color_base = "#FFFFE0"
        color_text = "black"
        provider = Gtk.CssProvider()
        # provider.load_from_data(".entry:focused {background: #FFFFE0;}")
        provider.load_from_data(""".entry:focused {background:#FFFFE0}
                                    .entry:selected {background-color: #7F7F7F;}

        """)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),
                                                 provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        # widget.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(440))
        # widget.modify_text(GTK_STATE_NORMAL, GDK_COLOR_PARSE(color_text))
        # provider = Gtk.CssProvider()
        # provider.load_from_data('.entry { background: red; }')
        # Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),
        #                                          provider,
        #                                          Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def entryGlobalcb(self,entry):
        entry.connect("icon-press", self.on_icon_press)
        entry.connect("focus-in-event", self.on_focus_in_event)
        entry.connect("focus-out-event", self.on_focus_out_event)
        entry.connect("focus-out-event", self.on_focus_out_event_calcolate)
        if gtk.Buildable.get_name(entry) != "password_entry":
            entry.set_property("secondary_icon_stock", "gtk-clear")
            entry.set_property("secondary_icon_activatable", True)
            entry.set_property("secondary_icon_sensitive", True)
        if entry.get_input_purpose() == Gtk.InputPurpose.DIGITS:
            entry.connect("key-press-event", self.onlyDigits)

    def on_icon_press(self, widget,position,event):
        pass


    def on_focus_out_event(self, widget, event):
        pass

    def on_focus_out_event_calcolate(self, widget, event):
        testo =  widget.get_text()
        if len(testo) > 0 and testo[0] == "=":
            dt = testo[1:]

            try:
                nt = eval(dt)
            except:
                nt=""
            widget.set_text(str(nt))
            print " VALUTATA in ", nt

    def add_prefix_actions(self, prefix_actions_proxy):
        """
        By using a gui designer (glade-2, gazpacho, etc)
        widgets can have a prefix in theirs names
        like foo:entry1 or foo:label3
        It means entry1 and label3 has a prefix action named foo.

        Then, prefix_actions_proxy must have a method named prefix_foo which
        is called everytime a widget with prefix foo is found, using the found widget
        as argument.

        prefix_actions_proxy:
            An instance with methods as prefix actions.
            It means it has methods like prefix_foo, prefix_bar, etc.
        """
        prefix_s = "prefix_"
        prefix_pos = len(prefix_s)

        is_method = lambda t : callable( t[1] )
        is_prefix_action = lambda t : t[0].startswith(prefix_s)
        drop_prefix = lambda (k,w): (k[prefix_pos:],w)

        members_t = inspect.getmembers(prefix_actions_proxy)
        methods_t = filter(is_method, members_t)
        prefix_actions_t = filter(is_prefix_action, methods_t)
        prefix_actions_d = dict( map(drop_prefix, prefix_actions_t) )

        for widget in self.widgets:
            prefixes = widget.prefixes
            if prefixes:
                for prefix in prefixes:
                    if prefix in prefix_actions_d:
                        prefix_action = prefix_actions_d[prefix]
                        prefix_action(widget)


    def custom_handler(self,
            glade, function_name, widget_name,
            str1, str2, int1, int2):
        """
        Generic handler for creating custom widgets, internally used to
        enable custom widgets (custom widgets of glade).

        The custom widgets have a creation function specified in design time.
        Those creation functions are always called with str1,str2,int1,int2 as
        arguments, that are values specified in design time.

        Methods of classes inheriting from SimpleGladeApp are used as
        creation functions automatically.

        If a custom widget has create_foo as creation function, then the
        method named create_foo is called with str1,str2,int1,int2 as arguments.
        """
        try:
            print "VEDIAMO UN PO", function_name
            handler = getattr(self, function_name)
            return handler(str1, str2, int1, int2)
        except AttributeError:
            return None


    def gtk_widget_show(self, widget, *args):
        """
        Predefined callback.
        The widget is showed.
        Equivalent to widget.show()
        """
        widget.show()


    def gtk_widget_hide(self, widget, *args):
        """
        Predefined callback.
        The widget is hidden.
        Equivalent to widget.hide()
        """
        widget.hide()


    def gtk_widget_grab_focus(self, widget, *args):
        """
        Predefined callback.
        The widget grabs the focus.
        Equivalent to widget.grab_focus()
        """
        widget.grab_focus()


    def gtk_widget_destroy(self, widget, *args):
        """
        Predefined callback.
        The widget is destroyed.
        Equivalent to widget.destroy()
        """
        widget.destroy()


    def gtk_window_activate_default(self, window, *args):
        """
        Predefined callback.
        The default widget of the window is activated.
        Equivalent to window.activate_default()
        """
        widget.activate_default()


    def gtk_true(self, *args):
        """
        Predefined callback.
        Equivalent to return True in a callback.
        Useful for stopping propagation of signals.
        """
        return True


    def gtk_false(self, *args):
        """
        Predefined callback.
        Equivalent to return False in a callback.
        """
        return False


    def gtk_main_quit(self, *args):
        """
        Predefined callback.
        Equivalent to self.quit()
        """
        Environment.pg2log.info("<<<<<<<<<<  CHIUSURA PROMOGEST >>>>>>>>>>>>>")
        self.quit()


    def on_keyboard_interrupt(self):
        """
        This method is called by the default implementation of run()
        after a program is finished by pressing Control-C.
        """
        Environment.pg2log.info("<<<<<<<<<<  CHIUSURA PROMOGEST >>>>>>>>>>>>>")
        gtk.main_quit()


    def quit(self):
        """
        Quit processing events.
        The default implementation calls gtk.main_quit()

        Useful for applications that needs a non gtk main loop.
        For example, applications based on gstreamer needs to override
        this method with gst.main_quit()
        """
        Environment.pg2log.info("<<<<<<<<<<  CHIUSURA PROMOGEST >>>>>>>>>>>>>")
        gtk.main_quit()


    def install_custom_handler(self, custom_handler):
        gtk.glade.set_custom_handler(custom_handler)


    def create_glade(self, glade_path, root, domain):
        return gtk.glade.XML(self.glade_path, root, domain)


    def get_widget(self, widget_name):
        return self.glade.get_widget(widget_name)


    def get_widgets(self):
        #return self.glade.get_widget_prefix("")
        return self.glade.get_objects()


    def getTopLevel(self):
        """ Restituisce il widget al livello piu` alto della gerarchia """
        return self.main_widget
