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
from promogest.Environment import *


t_codice_barre_articolo = Table('codice_a_barre_articolo', params["metadata"],
        Column('id',Integer,primary_key=True),
        Column('codice',String(50),nullable=False, unique=True),
        Column('id_articolo',Integer,ForeignKey(fk_prefix+'articolo.id', onupdate="CASCADE", ondelete="CASCADE")),
        Column('primario',Boolean,nullable=True),
        schema=params["schema"],
        extend_existing=True
        )
t_codice_barre_articolo.create(checkfirst=True)
