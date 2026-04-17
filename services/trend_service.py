from sqlalchemy import select
from db.models import ETFPrice

def get_history(db):
    return db.execute(
        select(ETFPrice).order_by(ETFPrice.timestamp)
    ).scalars().all()

def calculate_trend(data):
    if not data:
        return {"error": "No data"}

    premiums = [row.premium_percent for row in data]

    avg_premium = sum(premiums) / len(premiums)
    min_premium = min(premiums)
    max_premium = max(premiums)
    latest_premium = premiums[-1]

    # direction logic (simple but effective)
    if len(premiums) >= 2:
        if premiums[-1] > premiums[0]:
            direction = "UP"
        elif premiums[-1] < premiums[0]:
            direction = "DOWN"
        else:
            direction = "FLAT"
    else:
        direction = "UNKNOWN"

    return {
        "average": round(avg_premium, 2),
        "min": round(min_premium, 2),
        "max": round(max_premium, 2),
        "latest": round(latest_premium, 2),
        "trend": direction
    }

class TrendService:
    def get_trend(self, db):
        data = get_history(db)
        return calculate_trend(data)