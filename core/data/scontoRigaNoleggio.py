# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2013 by Promotux
#                        di Francesco Meloni snc - http://www.promotux.it/

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

from sqlalchemy import *

class ScontoRigaNoleggioDb(object):

    def __init__(self, schema = None,mainSchema=None, metadata=None, session=None,debug=False):
        self.metadata = metadata
        self.session_sl = session
        self.schema = schema
        self.debug = debug

    def create(self):

        rigaNoleggioTable = Table('riga_noleggio', self.metadata, autoload=True, schema=self.schema)
        scTable = Table('sconto', self.metadata, autoload=True, schema=self.schema)

        scontoRigaNoleggioTable = Table('sconto_riga_noleggio', self.metadata,
                Column('id',Integer,ForeignKey(self.schema+'.sconto.id',onupdate="CASCADE",ondelete="CASCADE"),primary_key=True),
                Column('id_riga_noleggio',Integer,ForeignKey(self.schema+'.riga_noleggio.id',onupdate="CASCADE",ondelete="CASCADE")),
                schema=self.schema
                )
        scontoRigaNoleggioTable.create(checkfirst=True)

    def update(self, req=None, arg=None):
        pass

    def alter(self, req=None, arg=None):
        pass
