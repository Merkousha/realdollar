from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from datalayer.connection_string import dbpath
from datalayer.models.currency.PriceLog import Base, PriceLog

engine = create_engine(f'sqlite:///{dbpath}')
Session = sessionmaker(bind=engine)
dollar_bazzar_sign='dollar_bazzar'

def update_significant_dollar_price_event(sender, new_price):
    session = Session()
    log_entry = PriceLog(dollar_bazzar_sign, new_price, datetime.now(), True)
    session.add(log_entry)
    session.commit()

def update_dollar_price_event(sender, new_price):
    session = Session()
    log_entry = PriceLog(dollar_bazzar_sign, new_price, datetime.now(), False)
    session.add(log_entry)
    session.commit()
