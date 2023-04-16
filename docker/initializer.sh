#!/bin/sh

init (){
    python manage.py makemigrations --noinput
    python manage.py migrate --noinput
    python manage.py collectstatic --clear --no-input
    python manage.py runserver
}

case "$1" in
    init)
        init
    ;;
esac
