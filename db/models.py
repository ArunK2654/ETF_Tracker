from datetime import datetime

from db.sessions import Base
from sqlalchemy import Column, Integer, Float, DateTime, String

class ETFPrice(Base):
    __tablename__ = "etf_price"

    no = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    market_price = Column(Float)
    inav_price = Column(Float)
    premium_percent = Column(Float)
    status = Column(String)