from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datalayer.connection_string import dbpath
from datalayer.models.currency.PriceLog import Base, PriceLog
from datetime import datetime , timedelta
from modules.ExternalProviders.currency_module import  get_navasan_dollar_price

engine = create_engine(f'sqlite:///{dbpath}')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
dollar_bazzar_sign='dollar_bazzar'

def get_last_dollar_price():
    session = Session()
    existed_dollar_price = session.query(PriceLog.price)\
        .filter_by(currency_name=dollar_bazzar_sign)\
        .order_by(PriceLog.update_time.desc())\
        .first()
    if not existed_dollar_price:
        current_dollar_price = get_navasan_dollar_price()
        new_log = PriceLog(currency_name=dollar_bazzar_sign, price=current_dollar_price)
        session.add(new_log)
        session.commit()
        existed_dollar_price = current_dollar_price
    session.close()
    return existed_dollar_price[0]

def get_last_significant_dollar_price():
    session = Session()
    existed_dollar_price = session.query(PriceLog.price)\
        .filter_by(currency_name=dollar_bazzar_sign, is_significant_change=True)\
        .order_by(PriceLog.update_time.desc())\
        .first()
    if not existed_dollar_price:
        current_dollar_price = get_navasan_dollar_price()
        new_log = PriceLog(currency_name=dollar_bazzar_sign, price=current_dollar_price)
        session.add(new_log)
        session.commit()
        existed_dollar_price = current_dollar_price
    session.close()
    return existed_dollar_price[0]

def get_today_dollar_dataframe():
    session = Session()
    start_time = datetime.now().strftime('%Y-%m-%d')
    today_prices_log = session.query(PriceLog.update_time, PriceLog.price)\
        .filter(PriceLog.update_time.like(f'%{start_time}%'))\
        .all()
 
    if(len(today_prices_log) == 0):
     now = datetime.now()   
     today_start = datetime(now.year, now.month, now.day)
     last_available_price = session.query(PriceLog.update_time, PriceLog.price)\
        .order_by(PriceLog.update_time.desc()).first()
     today_prices_log.append((today_start,last_available_price[1]))  
     today_prices_log.append((datetime.now(), last_available_price[1]))
    session.close()   
    return today_prices_log

def get_thisweek_dollar_dataframe():
    session = Session()
    today = datetime.now()
    start_of_week = today - timedelta(days=7) 
    print(start_of_week)
    today_prices_log = session.query(PriceLog.update_time, PriceLog.price)\
        .filter(PriceLog.update_time > start_of_week)\
        .all()
 
    if(len(today_prices_log) == 0):
     now = datetime.now()   
     today_start = datetime(now.year, now.month, now.day)
     last_available_price = session.query(PriceLog.update_time, PriceLog.price)\
        .order_by(PriceLog.update_time.desc()).first()
     today_prices_log.append((today_start,last_available_price[1]))  
     today_prices_log.append((datetime.now(), last_available_price[1]))
    session.close()   
    return today_prices_log
