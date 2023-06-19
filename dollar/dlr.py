# import necessary libraries
from telegram import Update 
from telegram.ext import ApplicationBuilder,  ContextTypes, CommandHandler

# import prjectmodules
from modules.Handlers.report_module import get_Current_public_Rport, get_current_currency_report , get_cryptos_report ,get_gold_report
from modules.Common.log_module import log_user_event
from modules.Common.config_texts import telegram_token, start_message
from modules.Handlers.charts import  get_today_dollar_chart ,get_this_week_dollar_chart


async def whatsup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    eventname = 'whatsup'
    log_user_event(update.effective_user.id, update.effective_user.first_name,
                   update.effective_user.full_name, eventname)
    await update.message.reply_text(get_Current_public_Rport(update.effective_user.first_name))


async def Currency(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    eventname = 'Currency'
    log_user_event(update.effective_user.id, update.effective_user.first_name,
                   update.effective_user.full_name, eventname)
    await update.message.reply_text(get_current_currency_report())
    
async def Crypto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    eventname = 'Crypto'
    log_user_event(update.effective_user.id, update.effective_user.first_name,
                   update.effective_user.full_name, eventname)
    await update.message.reply_text(get_cryptos_report())    
    

async def Gold(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    eventname = 'Gold'
    log_user_event(update.effective_user.id, update.effective_user.first_name,
                   update.effective_user.full_name, eventname)
    await update.message.reply_text(get_gold_report())    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    eventname = 'start'
    log_user_event(update.effective_user.id, update.effective_user.first_name,
                   update.effective_user.full_name, eventname)
    await update.message.reply_text(start_message)
    
async def today_dollar_chart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    eventname = 'todaydollarchart'
    log_user_event(update.effective_user.id, update.effective_user.first_name,
                   update.effective_user.full_name, eventname)
    await update.message.reply_media_group( get_today_dollar_chart()) 

async def thisweek_dollar_chart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    eventname = 'thisweekdollarchart'
    log_user_event(update.effective_user.id, update.effective_user.first_name,
                   update.effective_user.full_name, eventname)
    await update.message.reply_media_group( get_this_week_dollar_chart()) 
    
app = ApplicationBuilder().token(telegram_token).build()
app.add_handler(CommandHandler("whatsup", whatsup))
app.add_handler(CommandHandler("currency", Currency))
app.add_handler(CommandHandler("crypto", Crypto))
app.add_handler(CommandHandler("gold", Gold))
app.add_handler(CommandHandler("todaydollarchart", today_dollar_chart))
app.add_handler(CommandHandler("weekdollarchart", thisweek_dollar_chart))
app.add_handler(CommandHandler("start", start))
app.run_polling()

