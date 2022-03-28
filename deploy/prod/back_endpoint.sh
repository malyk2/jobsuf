python /var/www/back/manage.py migrate \
    && python /var/www/back/manage.py crontab add \
    && printenv > /var/www/back/jobsuf/.env #need for cron jobs
    && service supervisor start \
    && uwsgi --ini /var/www/uwsgi.ini