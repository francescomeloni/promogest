# -*- coding: utf-8 -*-

#    Copyright (C) 2014 by Promotux
#                       di Francesco Meloni snc - http://www.promotux.it/

#    Author: Francesco Meloni  <francesco@promotux.it>

#    This file is part of OdCollect.

#    OdCollect is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.

#    OdCollect is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with OdCollect.  If not, see <http://www.gnu.org/licenses/>.

from sqlalchemy import *
from promogest.Environment import *

session.close()
t_main_faq= Table('main_faq', meta,
        Column('id', Integer, primary_key=True),
        Column('question', String(200), nullable=False),
        Column('argomento', String(200), nullable=True),
        Column('tags', String(600), nullable=True),
        Column('answer', Text, nullable=True),
        Column('imagepath', String(400), nullable=True),
        Column('insert_date', DateTime, nullable=True),
        Column('clicks', Integer),
        Column("permalink", String(500), nullable=True),
        Column('active', Boolean, default=0),
        schema=mainSchema,
        extend_existing=True)
t_main_faq.create(checkfirst=True)
