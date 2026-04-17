from db.sessions import SessionLocal
from db.models import ETFPrice

def save_etf_data(market_price, nav_price, premium_percent, status):
    db = SessionLocal()

    record = ETFPrice(
        market_price=round(market_price,2),
        inav_price=round(nav_price,2),
        premium_percent=premium_percent,
        status=status
    )

    db.add(record)
    db.commit()
    db.close()
