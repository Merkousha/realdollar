import time
import datetime
import pytz
from bs4 import BeautifulSoup
from modules.Common.send_message_module import publish_feed_to_channel
from persiantools.jdatetime import JalaliDateTime
from datalayer.command.feeds.feed_handler import is_feed_new


def get_timestamp_from_eghtesad_date(string_date):
    format = "%a, %d %b %Y %H:%M:%S %z"
    datetime_object = datetime.datetime.strptime(string_date, format)
    return datetime_object.timestamp()


def check_and_publish_feed(feed):
    for item in feed.entries:
        title = item.title
        link = item.link

        if (is_feed_new(link, "Eghtesad_Online") and is_title_related(title)):
            # Get Dates
            timestamp = get_timestamp_from_eghtesad_date(item.published)
            jalali_date = JalaliDateTime.fromtimestamp(
                timestamp, pytz.timezone("Asia/Tehran")).strftime("%c")

            # CleanUP and format the message text with the news details
            description = BeautifulSoup(item.description, "html.parser").text
            message_text = f"<b>{title}</b>\n\n{description}\n\n\n تاریخ انتشار: {jalali_date}<a href='{link}'>.</a>"

            # Send the message to the Telegram channel
            publish_feed_to_channel(message_text, link)

        time.sleep(300)


def is_title_related(title):
    if (title.contains("ارز") or title.contains("دلار") or title.contains("یورو") or title.contains("درهم")):
        return True
    else:
        return False
