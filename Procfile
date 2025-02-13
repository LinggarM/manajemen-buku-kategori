web: gunicorn manajemen_buku.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn manajemen_buku.wsgi
