#realDollarBot Token
telegram_token = "Your Telegram bot Token"
channel_id='@SwingDollar'

#MerkoushaBot Token
# telegram_token = "Your Telegram bot Token"
# channel_id='@fakedollarchanell'

# Define events
UPDATE_Significant_DOLLAR_EVENT = 'update_Significant_dollarprice'
UPDATE_DOLLAR_EVENT = 'update_dollarprice'

dollar_refresh_time = 10    #10 seconds
feeds_refresh_time = 1800    #30 minutes
eghtesad_online_RSS_url ="https://www.eghtesadonline.com/fa/feeds/?p=Y2F0ZWdvcmllcz03"


significant_change = 100
crypto_names = {
    "BTCUSDT": "بیت‌کوین",
    "ETHUSDT": "اتریوم",
    "BUSDUSDT": "بی‌یو‌اس‌دی",
    "BNBBUSD": "بینانس کوین",
    "USDCBUSD": "یو‌اس‌دی‌سی",
    "XRPUSDT": "ریپل",
    "ADABUSD": "کاردانو",
    "DOGEUSDT": "دوج کوین",
    "MATICUSDT": "ماتیک",
    "SOLUSDT": "سولانا",
    "DOTUSDT": "دات",
    "LTCUSDT": "لایت‌کوین",
    "SHIBUSDT": "شیبا",
    "TRXUSDT": "ترون"
}

currencies=['["BTCUSDT","ETHUSDT","BUSDUSDT","BNBBUSD","USDCBUSD","XRPUSDT"]',
            '["ADABUSD","DOGEUSDT","MATICUSDT","BUSDUSDT","SOLUSDT"]',
            '["DOTUSDT","LTCUSDT","SHIBUSDT","TRXUSDT"]']

gold_names = {"emami_coin": "سکه امامی", "bahar_coin": "سکه بهارآزادی", "half_coin": "نیم سکه", "quarter_coin": "ربع سکه", "gerami_coin": "سکه گرمی",
              "18_carat_gold": "طلای 18 عیار", "24_carat_gold": "طلای 24 عیار", "global_gold_once": "اونس طلا", "global_silver_once": "اونس نقره", "gold_shekel": "مثقال طلا"}

irarz_endpoint = 'https://irarz.com/'
navasan_endpoint = 'https://fa.navasan.net/initrates.php?_='
gold_ounce_endpoint = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=XAU&to_currency=USD&apikey=XVM2JQE56T3NVKKO"





###############################################
#            Reports Templages                #
###############################################

start_message ="""✅رفیق عزیز سلام
امیدوارم که خوب باشی و کمتر حرص و جوش نوسان ها رو بخوری
به هر شکل ما در این بات سرویس های مختلفی رو برای شما در دست توسعه داریم تا بتونید دید شفاف تری به این وضعیت و مدیریت درست سرمایه ها و معاملاتتون داشته باشید.

در این لحظه سرویس اصلی آماده ی استفاده شما به شرح زیر هستند:
1️⃣- گزارش کلی بازار:
/whatsup
2️⃣-گزارش بازار ارز:
/currency
3️⃣-گزارش وضعیت رمز ارزها:
/Crypto
4️⃣-گزارش وضعیت بازار طلا:
/Gold
5️⃣- نمودار دلار امروز
 /todaydollarchart
6️⃣- نمودار دلار هفته
 /todaydollarchart

🔵 البته که شما همه ی سرویس های فعال ما رو در منوی بات هم میتونید ببینید.


باعشق♥️
تیم @RealDollarBot """


decrease_price_text = """
📣
📉کاهش {} تومانی دلار بازار

قیمت قبلی :  {} تومان
قیمت جدید:  {} تومان

@RealDollarBot
"""
increase_price_text = """
📣
📈افزایش {} تومانی دلار بازار

قیمت قبلی :  {} تومان
قیمت جدید:  {} تومان

@RealDollarBot
"""


whats_up_report_text="""📣 سلام {}
    
    
✅ قیمت دلار طلا: {} تومان
⛳️ قیمت دلار بازار: {} تومان
💰 این یعنی حباب برابره با: {} تومان

💶 قیمت یورو در بازار: {} تومان
‏🏴󠁧󠁢󠁥󠁮󠁧󠁿 پوند انگلیس در بازار: {} تومان
‏🇦🇪 درهم امارات در بازار: {} تومان
‏🇹🇷 لیر ترکیه در بازار: {} تومان


✳️ قیمت تتر در بازار: {} تومان
🔱 طلای 18 عیار بازار: {} تومان
🪙 سکه تمام بهار آزادی: {} تومان
🥇 اونس طلا در بازارهای جهانی {} دلار


زمان صدور گزارش: {}

برای گزارش های بیشتر میتونید به بات ما سر بزنید: \n@RealDollarBot"""

currency_report_text="""📣 گزارش وضعیت ارزهای بازار
    
    
✅ قیمت دلار در سکه طلا: {} تومان
⛳️ دلار بازار آزاد نقدی: {} تومان
💰 اختلاف قیمت دلار بازار آزاد با دلار محاسبه شده در نرخ سکه: {} تومان

‏🇦🇫 دلار هراتی: {} تومان
‏🇮🇷 دلار دولتی: {} تومان
‏🇮🇷 یورو مبادلاتی: {} تومان
💶 قیمت یورو در بازار: {} تومان
‏🏴󠁧󠁢󠁥󠁮󠁧󠁿 پوند انگلیس در بازار: {} تومان

‏🇦🇪 درهم امارات در بازار: {} تومان
‏🇹🇷 لیر ترکیه در بازار: {} تومان
‏🇮🇶 دینار عراق در بازار: {} تومان
‏🇰🇼 دینار کویت در بازار: {} تومان
‏🇨🇦 دلار کانادا در بازار: {} تومان
‏🇦🇺 دلار استرالیا در بازار: {} تومان
‏🇷🇺 روبل روسیه در بازار: {} تومان
‏🇨🇳 یوان چین در بازار: {} تومان
‏🇸🇦 ریال عربستان در بازار: {} تومان
‏ ریال عمان در بازار: {} تومان




زمان صدور گزارش: {}

برای گزارش های بیشتر میتونید به بات ما سر بزنید: \n@RealDollarBot"""


exception_error_message = "یکی پاشو گذاشته رو سیم هامون :)"