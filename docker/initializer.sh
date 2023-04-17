#!/bin/sh

init (){
    python manage.py migrate --noinput
    python manage.py collectstatic --clear --no-input
    exec gunicorn -b 0.0.0.0:8000 -w 5 -t 16 \
              --access-logfile - \
              --error-logfile - \
              --reload \
              --timeout 500 \
              wallet_generator.wsgi:application
}

case "$1" in
    init)
        init
    ;;
esac
