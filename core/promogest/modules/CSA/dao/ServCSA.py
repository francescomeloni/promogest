# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2014 by Promotux
#                        di Francesco Meloni snc - http://www.promotux.it/

#    Author: Francesco Meloni <francesco@promotux.it>

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
from promogest.modules.CSA.dao.LuogoInstallazione import LuogoInstallazione , t_luogo_installazione
from promogest.modules.CSA.dao.TipoCombustibile import TipoCombustibile , t_tipo_combustibile
#from promogest.dao.Articolo import Articolo

from promogest.dao.Cliente import Cliente, t_cliente
from promogest.dao.PersonaGiuridica import PersonaGiuridica_ , t_persona_giuridica

try:
    t_serv_csa = Table('servizio_csa', params['metadata'],
                         schema=params['schema'], autoload=True)
except:
    params["session"].close() # Questo comando chiude la sessione appesa
                              # e permette la creazione della tabella
    t_serv_csa = Table('servizio_csa',
        params['metadata'],
        Column('id', Integer, primary_key=True),
        Column('id_articolo', Integer,
               ForeignKey(fk_prefix + 'articolo.id',
                          onupdate='CASCADE', ondelete='CASCADE'),nullable=True),
        Column('id_cliente', Integer,
               ForeignKey(fk_prefix + 'cliente.id',
                          onupdate='CASCADE', ondelete='CASCADE'),nullable=True),
        Column('numero_serie', String(200), nullable=True),
        #Column('combustibile', String(200), nullable=True),
        Column('data_avviamento', DateTime, nullable=True),
        Column('tenuta_libretto', Boolean, default=False, nullable=False),

        Column('id_luogo_installazione', Integer,
               ForeignKey(fk_prefix + 'luogo_installazione.id',
                          onupdate='CASCADE', ondelete='CASCADE'),nullable=True),
        Column('id_tipo_combustibile', Integer,
               ForeignKey(fk_prefix + 'tipo_combustibile.id',
                          onupdate='CASCADE', ondelete='CASCADE'),nullable=True),
        Column('id_persona_giuridica', Integer,
               ForeignKey(fk_prefix + 'persona_giuridica.id',
                          onupdate='CASCADE', ondelete='CASCADE'),nullable=True),
        Column('manutenzione', String(100), nullable=True),
        Column('cadenza', String(1000), nullable=True),
        schema=params['schema'],
        extend_existing=True,
        )

    t_serv_csa.create(checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()

class ServCSA(Dao):

    def __init__(self, req=None):
        Dao.__init__(self, entity=self)

    def filter_values(self, k, v):
        if k == 'id':
            dic = {k: t_serv_csa.c.id==v}
        elif k == 'idArticolo':
            dic = {k: t_serv_csa.c.id_articolo==v}
        elif k == 'idCliente':
            dic = {k: t_serv_csa.c.id_cliente==v}
        elif k == 'numeroSerie':
            dic = {k: t_serv_csa.c.numero_serie.ilike("%"+v+"%")}
        return dic[k]

    @property
    def luogo_installazione(self):
        #a = GasRefrigerante().getRecord(id=self.id_gas_refrigerante)
        if self.luogoinsta:
            return self.luogoinsta.denominazione
        else:
            return ""

    @property
    def tipo_combustibile(self):
        #a = GasRefrigerante().getRecord(id=self.id_gas_refrigerante)
        if self.tipocombu:
            return self.tipocombu.denominazione
        else:
            return ""

    @property
    def cliente(self):
        if self.CLI:
            return self.CLI.ragione_sociale or self.CLI.cognome+" "+self.CLI.nome
        else:
            return ""
    @property
    def installatore(self):
        if self.PG:
            return self.PG.ragione_sociale or self.PG.cognome+" "+self.PG.nome
        else:
            return ""


    @property
    def articolo(self):
        if self.arti:
            return self.arti.denominazione
        else:
            return ""

std_mapper = mapper(ServCSA, t_serv_csa,   properties={

        "luogoinsta":relation(LuogoInstallazione,
            primaryjoin=t_serv_csa.c.id_luogo_installazione== t_luogo_installazione.c.id,
            backref="serv_csa"),
        "CLI":relation(Cliente,
            primaryjoin=t_serv_csa.c.id_cliente== t_cliente.c.id,
            backref="serv_csa"),
        "PG":relation(PersonaGiuridica_,
            primaryjoin=t_serv_csa.c.id_persona_giuridica== t_persona_giuridica.c.id,
            backref="serv_csa"),
        "tipocombu":relation(TipoCombustibile,
            primaryjoin=t_serv_csa.c.id_tipo_combustibile== t_tipo_combustibile.c.id,
            backref="serv_csa"),


                    },   order_by=t_serv_csa.c.id)
