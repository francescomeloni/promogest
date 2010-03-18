# -*- coding: utf-8 -*-
# Promogest
#
# Copyright (C) 2005-2008 by Promotux Informatica - http://www.promotux.it/

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import pool
from sqlalchemy.ext.sqlsoup import SqlSoup
import csv

AZIENDA_DESTINAZIONE = "elisir"
DATABASE = "promogest_db"
PORT = "5432"
USER = "promoadmin"
PASSWORD = "admin"
HOST = "192.168.1.101"
FILE_CSV = "inv_2010_gradisca01_def.csv"
MAINSCHEMA = "promogest2"
DELIMITER = ","
QUOTECHAR = '"'

class GenericFillData(object):
    def __init__(self):
        """ QUESTO script permette di importare la tabella inventario così come
            esportata dal modulo stesso. Il funzionamento è semplice:
            si lancia lo script con "python nomescript" avendo cura che
            il file csv si trovi nella stessa cartella dello script stesso

            schema csv :
               riga = ('Codice, Descrizione, Quantita\', Valore unitario, U.M., ' +
                    'Codice a barre, Famiglia, Categoria,Anno ,idMagazzino , idArticolo ,data_aggiornamento\n')
            schema tabella:
            anno ,id_magazzino , id_articolo , quantita , valore_unitario,data_aggiornamento
        """
        self.connection()

    def connection(self):
        engine = create_engine('postgres:'+'//'+USER+':'
                            + PASSWORD+ '@'
                            + HOST + ':'
                            + PORT + '/'
                            + DATABASE,
                            encoding='utf-8',
                            convert_unicode=True )

        engine.echo = True
        meta = MetaData(engine)
        self.pg_db_dest = SqlSoup(meta)
        self.pg_db_dest.schema = AZIENDA_DESTINAZIONE
        self.readFile()

    def readFile(self):
        spamReader = csv.reader(open(FILE_CSV), delimiter=DELIMITER, quotechar=QUOTECHAR)
        self.fillDataContact(spamReader)

    def fillDataContact(self,spamReader):
        for row in spamReader:
            print "TUUUUUUUUUUUUUUUUUUUUUUUU", row[2].strip().replace(",",".")
            quantita = float(row[2].strip().replace(",","."))
            if quantita >0:
                _field = self.pg_db_dest.inventario()
                _field.anno=int(row[8])
                _field.id_magazzino = int(row[9])
                _field.id_articolo = int(row[10])

                _field.quantita = quantita
                _field.valore_unitario = float(row[3].strip().replace(",","."))
                _field.data_aggiornamento = row[11] or None
                print _field.__dict__
                sqlalchemy.ext.sqlsoup.Session.add(_field)
                sqlalchemy.ext.sqlsoup.Session.commit()

#        self.pg_db_dest.flush()

if __name__ == "__main__":
    GenericFillData()
