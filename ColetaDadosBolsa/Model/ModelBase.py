import peewee

# Criamos o banco de dados
#db = peewee.SqliteDatabase('bolsaValoresTransacional.db')
db = peewee.MySQLDatabase("BolsaDeValores_Transacional",host = "192.168.99.100", port=3306, user="root", passwd="4nd3rs0N")

class ModelBase(peewee.Model):

    class Meta:
        database = db