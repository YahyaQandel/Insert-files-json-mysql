from classes.main import JSONScript
from celery import Celery

app = Celery()
app.config_from_object('celery_conf')


@app.task
def init_schedule():
	script = JSONScript()
	script.run()
	del script