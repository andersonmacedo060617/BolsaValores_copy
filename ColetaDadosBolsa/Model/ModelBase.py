import peewee

# Criamos o banco de dados
db = peewee.SqliteDatabase('bolsaValoresTransacional.db')


class ModelBase(peewee.Model):

    class Meta:
        database = db