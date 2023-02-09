import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicine_app.settings')

app = Celery('medicine_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()