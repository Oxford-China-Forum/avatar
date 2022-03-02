from sqlalchemy.sql import func

from ocf import db


class Ticket(db.Model):
    '''Model for the tickets table.'''

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, name={self.name!r})'
