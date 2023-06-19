from cachetools import cached, TTLCache

gold_cache_ttl = 120
currency_cache_ttl = 60
crypto_cache_ttl = 2
cash_max_size = 1000
cache_settings = {
          'gold': TTLCache(maxsize=cash_max_size, ttl=gold_cache_ttl),
          'currency': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'crypto': TTLCache(maxsize=cash_max_size, ttl=crypto_cache_ttl),
          'gold_all_prices': TTLCache(maxsize=cash_max_size, ttl=gold_cache_ttl),
          'OncePrice': TTLCache(maxsize=cash_max_size, ttl=gold_cache_ttl),
          'SilverOuncePrice': TTLCache(maxsize=cash_max_size, ttl=gold_cache_ttl),
          'BaharCoin': TTLCache(maxsize=cash_max_size, ttl=gold_cache_ttl),
          'Gold18': TTLCache(maxsize=cash_max_size, ttl=gold_cache_ttl),
          'BazarDollar': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'UAEDirham': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'TurkeyLear': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'EuroPrice': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'PoundPrice': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'harat_dollar': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'iri_gov_dollar': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'iri_gov_euro': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'iraq_dinar': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'kuwait_dinar': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'canada_dollar': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'australia_dollar': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'russia_rubl': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'china_yuann': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'saudi_rial': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'omman_rial': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          'TetterPrice': TTLCache(maxsize=cash_max_size, ttl=currency_cache_ttl),
          }
