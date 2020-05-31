import peewee
from Model.ModelBase import ModelBase

class Empresa(ModelBase):

    idt_empresa = peewee.PrimaryKeyField()
    codigoCvm = peewee.CharField(max_length = 200, null=True)
    razaoSocial = peewee.CharField(max_length = 500, null=True)
    nomePregao = peewee.CharField(max_length = 500, null=True)
    segmentoBolsa = peewee.CharField(max_length = 500, null=True)
    CNPJ = peewee.CharField(max_length = 500, null=True)
    AtividadePriTxt = peewee.CharField(max_length = 2000, null=True)
    classificaSetorial = peewee.CharField(max_length = 2000, null=True)
    linkCadastroEmpresa = peewee.CharField(max_length=2000, null=True)

    def saveNotExists(self):
        empresa = Empresa.select().where(Empresa.codigoCvm == self.codigoCvm)

        if len(empresa) == 0:
            self.save()

    @classmethod
    def findEmpresa(cls):
        empresas = Empresa.select().execute()

        return empresas



