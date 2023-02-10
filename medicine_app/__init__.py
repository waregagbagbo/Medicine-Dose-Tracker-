# edit and add the code to ensure celery is import to django anytime we initiate the process
from .celery import app as celery_app

__all__ = ['celery_app']