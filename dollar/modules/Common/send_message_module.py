import sqlite3
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
import asyncio

from modules.Common.config_texts import telegram_token, channel_id

# refactor this 
async def send_message(userid, message):
    bot = Bot(token=telegram_token)
    
    await bot.send_message(chat_id=str(userid), text=str(message))


def broadcast_message(message):
    with sqlite3.connect('/root/dollar/dollar_persistance/mydatabase.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT id FROM users ')
        existed_users = cur.fetchall()
        exepted_users = ["", ""]
        try:
            for user in existed_users:
                asyncio.run(send_message(user, message))
        except:
            exepted_users.append(user)


def boradcast_vipusers_message(message):

    vipusers = get_vi_users()
    # vipusers = [ "255504158"]
    exepted_users = ["", ""]
    try:
        for user in vipusers:
            asyncio.run(send_message(user, message))
    except:
        exepted_users.append(user)


def publish_new_price_to_channel(message):
    bot = Bot(token=telegram_token)
    asyncio.run(bot.send_message(chat_id=channel_id,
                text=str(message), parse_mode=ParseMode.HTML))


def publish_feed_to_channel(message, link):
    bot = Bot(token=telegram_token)

    button = InlineKeyboardButton(
        text="بیشتر بخوانید", url=link, callback_data="")
    # create a keyboard with the button
    keyboard = InlineKeyboardMarkup([[button]])
    asyncio.run(bot.send_message(chat_id=channel_id,
                text=str(message), reply_markup=keyboard, parse_mode=ParseMode.HTML))


def get_vi_users():
    return ["94974798", "255504158", "380526529", "93175139", "72087817"]
    # return [ "255504158"]
