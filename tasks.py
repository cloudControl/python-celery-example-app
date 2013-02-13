import json
from os import getenv

from celery import Celery

# read credentials from runtime environment
amqp_url = getenv('CLOUDAMQP_URL')

celery = Celery('tasks', broker=amqp_url)


@celery.task
def add(x, y):
    return x + y
