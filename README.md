zuqi - an online quiz website
========================

This is an online quiz website. Users will be able to create quizzes and take them.

It will run on Django.

The name is an anagram of quiz.

The license is zlib/libpng.

Installing
----------

You must install two python packages using pip to help develop.
* pip install django
* pip install -e git+git://github.com/silverfix/django-nested-inlines.git#egg=django-nested-inlines

Please ask if you need asistance in doing this.

To run a server run these two commands.

When running this line make an account

    python manage.py syncdb 
    python manage.py runserver

You can access your new site at

http://localhost:8000/admin
