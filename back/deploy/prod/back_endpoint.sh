python /var/www/back/manage.py migrate \
    && python /var/www/back/manage.py crontab add \
    && python /var/www/back/manage.py collectstatic --no-input \
    && printenv > /var/www/back/jobsuf/.env \
    && /etc/init.d/cron start \
    && uwsgi --ini /var/www/uwsgi.ini