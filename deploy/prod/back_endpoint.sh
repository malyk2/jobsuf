python /var/www/back/manage.py migrate \
    && python /var/www/back/manage.py crontab add \
    && service supervisor start \
    && uwsgi --ini /var/www/uwsgi.ini