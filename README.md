# Ghar Kharid

A complete web application built in django, html, css and javascript that provides a common platform for property buyers & sellers to locate properties of interest
across all over the world, and source information about all property related issues.

The idea is to make easy the management of properties and occupants by proposing many services:

1) Able to Gather all information of your properties, upload property photos and details in one place.
2) Seller's can easily list their property without any hidden charges 
and buyer's can buy the property without any hidden charges or brokage.
3) Easy communication between seller's and buyer's, where seller can easily able to 
enquire about any property.

## Getting started

Steps To Follow:


#### create virtual environment

    $ virtualenv <env_name> -p python3.7

#### Activate the environment

    $ source <env_name>/bin/activate

#### Install all the dependency in blog_env
    $ pip install -r requirements.txt

#### Run the migrations for databases:

    $ python manage.py makemigrations
    $ python manage.py migrate

##### Create Superuser to logged in Django admin panel (it is one time procedure)

    $ python manage.py createsuperuser

#### Start server in Development mode:

    $ python manage.py runserver 0.0.0.0:8080
