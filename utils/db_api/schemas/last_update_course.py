import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, sql

from utils.db_api.db_gino import db


class LastUpdateCourse(db.Model):
    __tablename__ = "last_update_currence"

    id = Column(BigInteger, primary_key=True)
    currency = Column(String(5), unique=True, nullable=False)
    last_update = Column(DateTime,
                         default=datetime.datetime.utcnow,
                         onupdate=datetime.datetime.utcnow,
                         nullable=False)

    query: sql.Select

    def __str__(self):
        return f"{str(self.currency)} updated ad {str(self.last_update)}"
