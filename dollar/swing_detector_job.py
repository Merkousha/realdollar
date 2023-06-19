import os

# import necessary libraries
import schedule
import time
from pydispatch import dispatcher
import feedparser


# import prjectmodules
from modules.Common.send_message_module import boradcast_vipusers_message, publish_new_price_to_channel
from modules.ExternalProviders.currency_module import get_navasan_dollar_price
from modules.Common.config_texts import decrease_price_text, increase_price_text, UPDATE_DOLLAR_EVENT, significant_change, UPDATE_Significant_DOLLAR_EVENT , dollar_refresh_time,feeds_refresh_time , eghtesad_online_RSS_url , exception_error_message
from datalayer.command.currency.dollar import update_significant_dollar_price_event, update_dollar_price_event
from datalayer.query.currency.dollar import get_last_dollar_price, get_last_significant_dollar_price
from modules.Common.feed_parser import check_and_publish_feed
from modules.Common.logging_config import logger


# Register listeners with events
dispatcher.connect(update_significant_dollar_price_event,
                   signal=UPDATE_Significant_DOLLAR_EVENT)
dispatcher.connect(update_dollar_price_event, signal=UPDATE_DOLLAR_EVENT)


def send_new_dollar_price():
    try:
        # Send a message to the user
        lst_significant_dollar_price = get_last_significant_dollar_price()
        currenct_dollar_price = get_navasan_dollar_price()
        update_telegram_channel(currenct_dollar_price)

        if (currenct_dollar_price != lst_significant_dollar_price):
            if (currenct_dollar_price > lst_significant_dollar_price):
                if ((currenct_dollar_price - lst_significant_dollar_price) >= significant_change):
                    boradcast_vipusers_message(increase_price_text.format(
                        currenct_dollar_price - lst_significant_dollar_price, lst_significant_dollar_price, currenct_dollar_price))
                    dispatcher.send(signal=UPDATE_Significant_DOLLAR_EVENT,
                                    sender=None, new_price=currenct_dollar_price)
            else:
                if (lst_significant_dollar_price - currenct_dollar_price >= significant_change):
                    boradcast_vipusers_message(decrease_price_text.format(
                        lst_significant_dollar_price - currenct_dollar_price, lst_significant_dollar_price, currenct_dollar_price))
                    dispatcher.send(signal=UPDATE_Significant_DOLLAR_EVENT,
                                    sender=None, new_price=currenct_dollar_price)
    except Exception as e:
        logger.error('An error occurred: %s', e)
        return exception_error_message

def update_telegram_channel(currenct_dollar_price):
    try:
        lst_dollar_price = get_last_dollar_price()
        if (currenct_dollar_price != lst_dollar_price):
            if (currenct_dollar_price > lst_dollar_price):
                publish_new_price_to_channel(increase_price_text.format(
                    currenct_dollar_price - lst_dollar_price, lst_dollar_price, currenct_dollar_price))
                dispatcher.send(signal=UPDATE_DOLLAR_EVENT,
                                sender=None, new_price=currenct_dollar_price)
            else:
                publish_new_price_to_channel(decrease_price_text.format(
                    lst_dollar_price - currenct_dollar_price, lst_dollar_price, currenct_dollar_price))
                dispatcher.send(signal=UPDATE_DOLLAR_EVENT,
                                sender=None, new_price=currenct_dollar_price)
    except Exception as e:
        logger.error('An error occurred: %s', e)
        return exception_error_message


def Check_for_new_feeds():
    rss_url = eghtesad_online_RSS_url
    feed = feedparser.parse(rss_url)
    check_and_publish_feed(feed)


# Schedule the task to run every 5 minutes
schedule.every(dollar_refresh_time).seconds.do(send_new_dollar_price)
schedule.every(feeds_refresh_time).seconds.do(Check_for_new_feeds)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
