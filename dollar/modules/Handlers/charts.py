import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import sqlite3
import io
import pytz
import telegram
from persiantools.jdatetime import JalaliDateTime
import asyncio
from modules.Common.logging_config import logger
from modules.Common.config_texts import telegram_token
from datalayer.query.currency.dollar import get_today_dollar_dataframe , get_thisweek_dollar_dataframe
from telegram import InputMediaPhoto
import matplotlib.dates as mdates

def get_today_dollar_chart():
    try:
        # Get today dollar price dataframe
        data = get_today_dollar_dataframe()

        # Create a line plot
        plt.figure(figsize=(10, 6))
        df = pd.DataFrame(data, columns=['update_time', 'price'])
        avg_price = df['price'].mean()
        df['update_time'] = pd.to_datetime(df['update_time'])
        df.set_index('update_time', inplace=True)
        plt.plot(df, color='blue', linewidth=2, linestyle='--')

        # Add horizontal line for average price
        plt.axhline(y=avg_price, color='red',
                    linestyle='-', label='Average Price')

        plt.grid(True)
        plt.rcParams.update({'font.size': 12})
        plt.legend(['Price', 'Average Price'], loc='upper left')
        plt.rcParams['axes.facecolor'] = 'lightgray'
        plt.xlabel('Date')
        plt.ylabel('Price')
         # Set x-axis tick format to display time only
        hours = mdates.HourLocator(interval=1)
        time_format = mdates.DateFormatter('%H:%M')
        plt.gca().xaxis.set_major_locator(hours)
        plt.gca().xaxis.set_major_formatter(time_format)
        plt.title('Dollar Price Swing')
        # Save the plot as an image in memory
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        media = InputMediaPhoto(buf.getvalue(), caption="نمودار قیمت امروز دلار ( " + str(JalaliDateTime.now(
            pytz.timezone("Asia/Tehran")).strftime("%A %Y-%m-%d"))+" )\n\n\n ربات ما: @RealDollarbot \n کانال ما: @SwingDollar")
        # Close the plot
        plt.close()
        # wrap the media object in a list to create a single-item array
        media_array = [media]
        return media_array

    except Exception as e:
        logger.error('An error occurred: %s', e)



def get_this_week_dollar_chart():
    try:
        # Get today dollar price dataframe
        data = get_thisweek_dollar_dataframe()
        
        # set the locator interval
        locator_interval = 24
            
             
        # Create a line plot
        plt.figure(figsize=(10, 6))
        df = pd.DataFrame(data, columns=['update_time', 'price'])
        avg_price = df['price'].mean()
        df['update_time'] = pd.to_datetime(df['update_time'])
        df.set_index('update_time', inplace=True)
        plt.plot(df, color='blue', linewidth=2, linestyle='--')

        # Add horizontal line for average price
        plt.axhline(y=avg_price, color='red',
                    linestyle='-', label='Average Price')

        plt.grid(True)
        plt.rcParams.update({'font.size': 12})
        plt.legend(['Price', 'Average Price'], loc='upper left')
        plt.rcParams['axes.facecolor'] = 'lightgray'
        plt.xlabel('Date')
        plt.ylabel('Price')
        
        # Set x-axis tick format to display time only
        hours = mdates.HourLocator(interval=locator_interval)
        time_format = mdates.DateFormatter('%A %H:%M')
        plt.gca().xaxis.set_major_locator(hours)
        plt.gca().xaxis.set_major_formatter(time_format)
        plt.title('Dollar Price Swing')
       
        # Save the plot as an image in memory
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        media = InputMediaPhoto(buf.getvalue(), caption="نمودار قیمت هفته پیش دلار بازار \n\n\n ربات ما: @RealDollarbot \n کانال ما: @SwingDollar")
        
        # Close the plot
        plt.close()
        
        # wrap the media object in a list to create a single-item array
        media_array = [media]
        return media_array

    except Exception as e:
        logger.error('An error occurred: %s', e)
