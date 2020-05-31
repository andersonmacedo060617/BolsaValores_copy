import peewee
from Model.ModelBase import ModelBase
from Model.Empresa import Empresa

class Simbolo(ModelBase):
    idtSimbolo = peewee.PrimaryKeyField()
    codSimbolo = peewee.CharField(max_length = 100, null=True)
    empresa = peewee.ForeignKeyField(Empresa, lazy_load=True)

    def saveNotExists(self):
        simbolo = Simbolo.select().where(Simbolo.codSimbolo == self.codSimbolo)

        if len(simbolo) == 0:
            self.save()

    @classmethod
    def findEmpresa(cls):
        simbolo = Simbolo.select().execute()

        return simbolo