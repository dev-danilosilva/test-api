import databases
import sqlalchemy


database = databases.Database('sqlite:///dev.sqlite')
metadata = sqlalchemy.MetaData()
