# gunicorn.conf.py
import multiprocessing


workers = multiprocessing.cpu_count() * 2 + 1

bind = "0.0.0.0:8000"


timeout = 120
keepalive = 5


accesslog = "-" 
errorlog = "-"
loglevel = "info"


wsgi_app = "your_project_name.wsgi:application"