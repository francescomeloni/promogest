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
from Dao import Dao, Base


class CategoriaArticolo(Base,Dao):
    try:
        __table__ = Table('categoria_articolo',
            params['metadata'],
            schema = params['schema'],
            autoload=True)
    except:
        from data.categoria_articolo import t_categoria_articolo
        __table__ = t_categoria_articolo

    def __init__(self, req=None):
        Dao.__init__(self, entity=self)

    def filter_values(self,k,v):
        if k == 'denominazione':
            dic= {k: CategoriaArticolo.__table__.c.denominazione.ilike("%"+v+"%")}
        elif k == "denominazioneBreve":
            dic= {k: CategoriaArticolo.__table__.c.denominazione_breve.ilike("%"+v+"%")}
        elif k == "denominazioneBreveEM":
            dic= {k: CategoriaArticolo.__table__.c.denominazione_breve == v}
        elif k == "fullsearch":
            dic = {k: or_(CategoriaArticolo.__table__.c.denominazione.ilike("%"+v+"%"),
            CategoriaArticolo.__table__.c.denominazione_breve.ilike("%" + v + "%")
                                                                            )}

        return  dic[k]

    def preSave(self):
        """ Put in this Func all the integrity checks """
        categorie_articolo = None
        if len(self.denominazione_breve) > 10:
            self.denominazione_breve = self.denominazione_breve[0:9]
        else:
            return True
