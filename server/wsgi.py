"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application
# activate virtualenv
#activate_this = os.path.expanduser("/var/www/www-root/data/www/informatization.tech/venv/bin/activate_this.py")
#execfile(activate_this, dict(__file__=activate_this))
# add the hellodjango project path into the sys.path
sys.path.append('/var/www/www-root/data/www/informatization.tech')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/var/www/www-root/data/www/informatization.tech/test-info')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()
