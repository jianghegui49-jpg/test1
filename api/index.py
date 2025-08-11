# api/index.py
import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

application = get_wsgi_application()   # Vercel 需要的 app 变量