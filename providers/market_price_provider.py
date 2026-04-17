import yfinance
from core.logger import logger
from core.exceptions import MarketDataError

# to get market price of mon100 etf
class MarketPriceProvider:
    def get_market_price(self):
        try:
            logger.info("Fetching Market price...")
            ticker = yfinance.Ticker("MON100.NS").history(period="1d")
            market_price = ticker["Close"].iloc[-1] #Give me the last row
            logger.debug(f"Market price Retrieved: {market_price}")
            return market_price

            # market_price = ticker.info["regularMarketPrice"]
            # print(f'Market Price -> {market_price}')

        except Exception as e:
            logger.error(f"Market price fetch failed: {e}")
            raise MarketDataError("Failed to fetch market price")
