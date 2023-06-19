from modules.ExternalProviders.gold_module import get_gold_Ounce_Price, getBaharCoinPrice, getGold18Price, get_gold_all_prices
from modules.ExternalProviders.currency_module import getBazarDollarPrice, getUAEDirhamPrice, getTurkeyLearPrice, getEuroPrice, getPoundPrice, get_harat_dollar_price, iri_gov_dollar_price, iri_gov_euro_price, iraq_dinar_price, kuwait_dinar_price, canada_dollar_price, australia_dollar_price, russia_rubl_price, china_yuann_price, saudi_rial_price, omman_rial_price
from modules.ExternalProviders.crypto_module import getTetterPrice, get_crypto_all_prices
from modules.Common.logging_config import logger

from persiantools.jdatetime import JalaliDateTime
from modules.Common.config_texts import gold_names, crypto_names, whats_up_report_text, exception_error_message, currency_report_text
import pytz


def floatPrice(price):
    text_price = str(price).replace(',', '')
    return float(text_price)


def get_Current_public_Rport(clientname):
    try:
        baharCoinPrice = floatPrice(getBaharCoinPrice())
        OuncePrice = floatPrice(get_gold_Ounce_Price())
        goldDollarPrice = int((baharCoinPrice*4.24927) / OuncePrice)/10

        BazzarDollar = getBazarDollarPrice()

        textprice = whats_up_report_text.format(clientname,                                                                            goldDollarPrice,
                                                BazzarDollar,
                                                format(
                                                    int(goldDollarPrice-BazzarDollar), ','),
                                                getEuroPrice(),
                                                getPoundPrice(),
                                                getUAEDirhamPrice(),
                                                getTurkeyLearPrice(),
                                                getTetterPrice(),
                                                getGold18Price(),
                                                format(
                                                    int(baharCoinPrice), ','),
                                                OuncePrice,
                                                JalaliDateTime.now(pytz.timezone("Asia/Tehran")).strftime("%c"))
    except Exception as e:
        logger.error('An error occurred: %s', e)
        return exception_error_message
    return textprice


def get_current_currency_report():
    try:
        # createGoldDollarPrice
        baharCoinPrice = floatPrice(getBaharCoinPrice())
        OncePrice = floatPrice(get_gold_Ounce_Price())
        goldDollarPrice = int((baharCoinPrice*4.24927) / OncePrice)/10

        BazzarDollar = getBazarDollarPrice()

        textprice = currency_report_text.format(
            format(goldDollarPrice, ','),
            format(BazzarDollar, ','),
            format(int(goldDollarPrice-BazzarDollar), ','),
            format(get_harat_dollar_price(), ','),
            format(iri_gov_dollar_price(), ','),
            format(iri_gov_euro_price(), ','),
            getEuroPrice(),
            getPoundPrice(),
            getUAEDirhamPrice(),
            getTurkeyLearPrice(),
            format(iraq_dinar_price(), ','),
            format(kuwait_dinar_price(), ','),
            format(canada_dollar_price(), ','),
            format(australia_dollar_price(), ','),
            format(russia_rubl_price(), ','),
            format(china_yuann_price(), ','),
            format(saudi_rial_price(), ','),
            format(omman_rial_price(), ','),
            JalaliDateTime.now(pytz.timezone("Asia/Tehran")).strftime("%c"))
    except Exception as e:
        logger.error('An error occurred: %s', e)
        return exception_error_message
    return textprice


def get_cryptos_report():
    try:
        report = "📣 گزارش وضعیت رمز ارزها: \n"
        cryptocurencies = get_crypto_all_prices()
        devider = 1
        for cryptocurency in cryptocurencies:
            report = report + \
                "\n💡 {}  : {} دلار ".format(
                    crypto_names[cryptocurency], cryptocurencies[cryptocurency])
            if (devider % 3 == 0):
                report = report+"\n"
            devider += 1
        report = report+"\n\n زمان صدور گزارش: {} \n\n‏ℹ️برای گزارش های بیشتر میتونید به بات ما سر بزنید: \n @RealDollarBot".format(
            JalaliDateTime.now(pytz.timezone("Asia/Tehran")).strftime("%c"))
    except Exception as e:
        logger.error('An error occurred: %s', e)
        return exception_error_message
    return report


def get_gold_report():
    try:
        report = "📣 گزارش وضعیت بازار طلا: \n"
        gold_prices = get_gold_all_prices()
        devider = 1
        for gold_price in gold_prices:
            currency = "تومان"
            if ("اونس" in gold_names[gold_price]):
                currency = "دلار"

            report = report + \
                "\n💡 {}  : {} {} ".format(
                    gold_names[gold_price], gold_prices[gold_price], currency)
            if (devider % 5 == 0):
                report = report+"\n"
            devider += 1
        report = report+"\n\n زمان صدور گزارش: {} \n\n‏ℹ️برای گزارش های بیشتر میتونید به بات ما سر بزنید: \n @RealDollarBot".format(
            JalaliDateTime.now(pytz.timezone("Asia/Tehran")).strftime("%c"))
    except Exception as e:
        logger.error('An error occurred: %s', e)
        return exception_error_message
    return report
