from datetime import timedelta
# Broker settings.
BROKER_URL = 'redis://localhost:6379/0'
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
# List of modules to import when celery starts.
CELERY_IMPORTS = ('run', )

CELERYBEAT_SCHEDULE = {
    'check-json-data': {
        'task': 'run.init_schedule',
        'schedule': timedelta(minutes=1),

    },
}
