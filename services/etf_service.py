from providers.market_price_provider import MarketPriceProvider
from providers.nav_price_provider import NavPriceProvider
from core.logger import logger
from core.exceptions import MarketDataError, NavDataError
from core.notifier import send_telegram_message

# to compute premium
class ETFservice:

    def __init__(self):
        self.market_price_provider = MarketPriceProvider()
        self.nav_price_provider = NavPriceProvider()

    def calculate_premium(self):
        try:
            market_price = self.market_price_provider.get_market_price()
            inav_price = self.nav_price_provider.get_nav_price()

        except MarketDataError as e:
            logger.error(f"Market data error in service: {e}")
            raise

        except NavDataError as e:
            logger.error(f"NAV data error in service: {e}")
            raise

        logger.info("Calculating premium...")

        percent = ((market_price - inav_price)/inav_price) * 100

        if percent < 10:
            send_telegram_message(f"🚨 MON100 Alert!\nPremium: {round(percent, 2)}%")

        if percent > 0:
            premium_percent = round(percent,2)
            status = "premium"
        else:
            premium_percent = abs(round(percent, 2))
            status = "discount"

        logger.info(f"{status} percent is {premium_percent}%")

        return {
                  "etf": "MON100",
                  "market_price": market_price,
                  "nav": inav_price,
                  "premium_percent": premium_percent,
                  "status": status
                }


