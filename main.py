from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from services.etf_service import ETFservice
from core.exceptions import MarketDataError, NavDataError
from contextlib import asynccontextmanager
from core.scheduler import start_scheduler, stop_scheduler
from db.models import ETFPrice
from db.sessions import engine, Base, SessionLocal
from services.trend_service import TrendService

@asynccontextmanager
async def lifespan(app: FastAPI):   # 👈 MUST be async
    start_scheduler()
    yield
    stop_scheduler()

app = FastAPI(lifespan=lifespan)
service = ETFservice()

# it converts Python models → database tables, if they dont exist in db
Base.metadata.create_all(bind=engine)

@app.get("/get_mon100_premium")
async def premium():
    try:
        return service.calculate_premium()

    except MarketDataError:
        raise HTTPException(status_code=500, detail="Market data unavailable")

    except NavDataError:
        raise HTTPException(status_code=500, detail="NAV data unavailable")

    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong")


def get_db():
    db1 = SessionLocal()
    try:
        yield db1
    finally:
        db1.close()


@app.get("/latest")
async def latest(db: Annotated[Session, Depends(get_db)]):
    return db.query(ETFPrice).order_by(ETFPrice.timestamp.desc()).limit(1).all()

@app.get("/history")
async def history(db: Annotated[Session, Depends(get_db)], limit=50):
    return db.query(ETFPrice).order_by(ETFPrice.timestamp.desc()).limit(limit).all()

trend_service = TrendService()

@app.get("/trend")
async def trend(db: Session = Depends(get_db)):
    return trend_service.get_trend(db)