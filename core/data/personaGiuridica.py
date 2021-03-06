# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2015 by Promotux
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

try:
    t_persona_giuridica = Table('persona_giuridica', params["metadata"],
                                        schema=params["schema"],
                                        autoload=True)
except:
    t_persona_giuridica = Table('persona_giuridica', params["metadata"],
            Column('id', Integer, primary_key=True),
            Column('codice', String(50), nullable=True,),
            Column('ragione_sociale',String(200), nullable=True),
            Column('insegna',String(100), nullable=True),
            Column('cognome',String(70), nullable=True),
            Column('nome',String(70), nullable=True),
            Column('sede_operativa_indirizzo',String(300), nullable=True),
            Column('sede_operativa_cap',String(10), nullable=True),
            Column('sede_operativa_provincia',String(50), nullable=True),
            Column('sede_operativa_localita',String(200), nullable=True),
            Column('sede_legale_indirizzo',String(300), nullable=True),
            Column('sede_legale_cap',String(10), nullable=True),
            Column('sede_legale_provincia',String(50), nullable=True),
            Column('sede_legale_localita',String(200), nullable=True),
            Column('nazione',String(100), nullable=True),
            Column('codice_fiscale',String(16), nullable=True),
            Column('partita_iva',String(30), nullable=True),
            Column('id_user',Integer, ForeignKey(fk_prefix_main+'utente.id')),
            Column('note', Text),
            Column('cancellato', Boolean, default=False),
            extend_existing=True,
            schema=params["schema"]
            )
    t_persona_giuridica.create(checkfirst=True)
