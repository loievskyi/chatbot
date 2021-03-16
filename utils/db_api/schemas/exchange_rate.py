from sqlalchemy import Column, BigInteger, String, Float, sql

from utils.db_api.db_gino import db


class ExchangeRate(db.Model):
    __tablename__ = "cource_update"

    id = Column(BigInteger, primary_key=True)
    base_currency = Column(String(5), nullable=False)
    final_curency = Column(String(5), nullable=False)
    course = Column(Float, nullable=False)

    query: sql.Select

    def __str__(self):
        return f"1 {self.base_currency}: {self.course:.2f} {self.final_curency}"
