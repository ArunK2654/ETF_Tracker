import requests
from core.logger import logger
from core.exceptions import NavDataError

class NavPriceProvider:
    # to get inav price of mon100 etf
    def get_nav_price(self):
        logger.info("Fetching iNav price...")
        url = "https://www.amfiindia.com/spages/NAVAll.txt"
        headers = {
            "Accept": "text/plain",
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            logger.error(f"AmfiIndia Website returned StatusCode: {response.status_code}")
            raise NavDataError("Failed to fetch Nav details" )

        inav_price = None

        array_of_lines = response.text.split("\n")
        for line in array_of_lines:
            parts_array = line.split(";")

            if len(parts_array) != 6:
                continue

            scheme_name = parts_array[3]

            if "Motilal Oswal Nasdaq 100 ETF" in scheme_name:
                inav_price = float(parts_array[4])
                logger.debug(f"iNav price Retrieved: {inav_price}")
                return inav_price
                # print(f"INav Price -> {inav_price}")

        if inav_price is None:
            logger.error(f"MON100 not found in AmfiIndia response")
            exit()
