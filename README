CSRF example app
================

This application is a super-simple Twitter clone written in Django, built to demonstrate a CSRF attack.

If you are not familiar with the term CSRF, check out [this article that explains what an CSRF vulnerability is and how you can ensure that your Django app doesn't have one.](https://consideratecode.com/2017/08/31/csrf/)

**NOTE:** This app was intentionally made vulnerable to CSRF attacks by removing the CsrfViewMiddleware.


Live-Demo
---------
A live demo is running at https://csrf-example.herokuapp.com

Create a user and post a status. Then go look at a [cute kitten](https://consideratecode.github.io/csrf_example/kitten.html) (with JavaScript enabled).


Usage
-----
This application has been tested with Python 3.6 and Django 1.11.

To run the application locally, follow these steps:

    $ virtualenv venv  # create a virtual environment
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ DJANGO_DEBUG=1 python manage.py runserver

Note: by default, the application runs with DEBUG=False. Set the environment
variable DJANGO_DEBUG to enable debug mode, like in the example above.

A static HTML page that exploits the CSRF vulnerability can be found in docs/local_kitten.html

Author: Daniel Hepper <daniel@consideratecode.com>
License: MIT

This application is obviously neither affiliated with nor endorsed by Twitter, Inc.
