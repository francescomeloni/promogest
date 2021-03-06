# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2015 by Promotux
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

from promogest.dao.Dao import Dao, Base
from promogest.modules.GestioneFile.dao.Immagine import ImageFile
from promogest.dao.Articolo import Articolo

class ArticoloImmagine(Base, Dao):
    """ ArticoloImmagine class database functions  """
    try:
        __table__ = Table('articolo_immagine',
                    params['metadata'],
                    schema = params['schema'],
                    autoload=True)
    except:
        from data.articoloImmagine import t_articolo_immagine
        __table__ = t_articolo_immagine

    immagine = relationship("ImageFile", backref='artima',cascade="all, delete")
    articolo = relationship("Articolo", backref='artima',
                            cascade="all, delete")

    __mapper_args__ = { 'order_by' : "id_immagine" }

    def __init__(self, req=None):
        Dao.__init__(self, entity=self)

    def filter_values(self,k,v):
        if k == 'id_immagine':
            dic = {k:ArticoloImmagine.__table__.c.id_immagine == v}
        elif k == 'idArticolo':
            dic = {k:ArticoloImmagine.__table__.c.id_articolo == v}
        elif k == 'denominazione':
            dic = {k:and_(ArticoloImmagine.__table__.id_articolo==t_articolo.id,t_immagine.ilike("%"+v+"%"))}
        return  dic[k]
