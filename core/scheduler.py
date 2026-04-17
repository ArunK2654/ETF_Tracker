from apscheduler.schedulers.background import BackgroundScheduler
from services.etf_service import ETFservice
from core.logger import logger
from services.repository_service import save_etf_data

scheduler = BackgroundScheduler()

def run_etf_job():
    try:
        service = ETFservice()
        result = service.calculate_premium()
        save_etf_data(result.get("market_price"),result.get("nav"), result.get("premium_percent"), result.get("status") )
        logger.info(f"Scheduler ETF DATA: {result}")

    except Exception as e:
        logger.error(f"Scheduler error: {e}")

def start_scheduler():
    scheduler.add_job(run_etf_job, trigger="cron", minute="*/1")  # every 1 min (change later)
    scheduler.start()
    logger.info("Scheduler started")

def stop_scheduler():
    scheduler.shutdown()
    logger.info("Scheduler stopped")