from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from youtube.views import fetch_videos

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(fetch_videos, 'interval', seconds=10)
	scheduler.start()