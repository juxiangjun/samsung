import sys, os, sae
from mysamsung import wsgi
application = sae.create_wsgi_app(wsgi.application)
