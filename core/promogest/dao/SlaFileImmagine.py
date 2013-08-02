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

from sqlalchemy import *
from sqlalchemy.orm import *
from promogest.Environment import *
from promogest.dao.Dao import Dao

try:
    t_slafile_immagine=Table('slafile_immagine',
                    params['metadata'],
                    schema = params['schema'],
                    autoload=True)
except:
    from data.slafileImmagine import t_slafile_immagine


class SlaFileImmagine(Dao):
    """ RoleAction class database functions  """

    def __init__(self, req=None):
        Dao.__init__(self, entity=self)

    def filter_values(self,k,v):
        if k == 'id_immagine':
            dic = {k:t_slafile_immagine.c.id_immagine == v}
        elif k == 'id_slafile':
            dic = {k:t_slafile_immagine.c.id_slafile == v}
        return  dic[k]

std_mapper = mapper(SlaFileImmagine, t_slafile_immagine, properties={
                }, order_by=t_slafile_immagine.c.id_immagine)
