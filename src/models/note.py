from src.db import database, metadata
import orm


class Note(orm.Model):
    __tablename__ = 'note'
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    description = orm.String(allow_null=False, max_length=120)
    status = orm.Boolean(default=True)

    def __str__(self):
        return self.id