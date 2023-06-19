from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PriceLog(Base):
    __tablename__ = 'price_log'
    id = Column(Integer, primary_key=True)
    currency_name = Column(String)
    price = Column(Integer)
    update_time = Column(DateTime)
    is_significant_change = Column(Boolean)

    def __init__(self, currency_name, price, update_time, is_significant_change):
        self.currency_name = currency_name
        self.price = price
        self.update_time = update_time
        self.is_significant_change = is_significant_change
