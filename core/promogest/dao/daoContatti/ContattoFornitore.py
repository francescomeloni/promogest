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
from sqlalchemy.orm import *
from promogest.Environment import *
from promogest.dao.Dao import Dao, Base
from promogest.dao.Fornitore import Fornitore
from promogest.dao.daoContatti.Contatto import Contatto
from promogest.dao.daoContatti.RecapitoContatto import RecapitoContatto
from promogest.dao.daoContatti.ContattoCategoriaContatto import ContattoCategoriaContatto

from data.contatto import t_contatto
from data.contattoFornitore import t_contatto_fornitore
c_cf = join(t_contatto, t_contatto_fornitore)

class ContattoFornitore(Base, Dao):
    __table__ = c_cf
    id = column_property(t_contatto.c.id, t_contatto_fornitore.c.id)

    fornitore = relationship("Fornitore", backref="contatto_fornitore")
    tipo_contatto = column_property(t_contatto.c.tipo_contatto, t_contatto_fornitore.c.tipo_contatto)

    def __init__(self, req=None):
        Dao.__init__(self, entity=self)


    def _getRecapitiContatto(self):
        self.__dbRecapitiContatto = RecapitoContatto().\
                                            select(id=self.id,batchSize=None)
        self.__recapitiContatto = self.__dbRecapitiContatto[:]
        return self.__recapitiContatto

    def _setRecapitiContatto(self, value):
        self.__recapitiContatto = value

    recapiti = property(_getRecapitiContatto, _setRecapitiContatto)


    def _getCategorieContatto(self):
        self.__dbCategorieContatto = ContattoCategoriaContatto().\
                                            select(id=self.id,batchSize=None)
        self.__categorieContatto = self.__dbCategorieContatto[:]
        return self.__categorieContatto

    def _setCategorieContatto(self, value):
        self.__categorieContatto = value

    categorieContatto = property(_getCategorieContatto, _setCategorieContatto)

    @property
    def appartenenza(self):
        a =  params["session"].query(Fornitore).with_parent(self).\
                            filter(self.id_fornitore==Fornitore.id).all()
        if not a:
            return a
        else:
            return a[0].ragione_sociale or a[0].cognome or a[0].nome


    def filter_values(self, k,v):
        if k == 'idCategoria':
            dic = {k:and_(ContattoCategoriaContatto.id_contatto==Contatto.__table__.c.id, ContattoCategoriaContatto.id_categoria_contatto==v)}
        elif k == 'idFornitore':
            dic = {k:t_contatto_fornitore.c.id_fornitore == v}
        elif k == 'idFornitoreList':
            dic = {k:t_contatto_fornitore.c.id_fornitore.in_(v)}
        elif k == 'cognomeNome':
            dic = {k:or_(Contatto.__table__.c.cognome.ilike("%"+v+"%"),Contatto.__table__.c.nome.ilike("%"+v+"%"))}
        elif k == 'ruolo':
            dic = {k:Contatto.__table__.c.ruolo.ilike("%"+v+"%")}
        elif k == "recapito":
            dic={k:and_(t_contatto_fornitore.c.id==RecapitoContatto.__table__.c.id_contatto,RecapitoContatto.__table__.c.recapito.ilike("%"+v+"%"))}
        elif k == "tipoRecapito":
            dic={k:and_(t_contatto_fornitore.c.id==RecapitoContatto.__table__.c.id_contatto,RecapitoContatto.__table__.c.tipo_recapito ==v)}
        elif k=='descrizione':
            dic = {k:Contatto.__table__.c.descrizione.ilike("%"+v+"%")}
        return  dic[k]
