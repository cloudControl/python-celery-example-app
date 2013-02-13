web: celery flower --port=$PORT --broker=$CLOUDAMQP_URL
worker: celery -A tasks worker --loglevel=info
