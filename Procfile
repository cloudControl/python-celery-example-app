web: celery flower --port=$PORT --broker=$CLOUDAMQP_URL --basic_auth=$FLOWER_AUTH
worker: celery -A tasks worker --loglevel=info
