# Created for the a tech Interview

If you wish to clone this project and run the project on your machine please follow the instructions below.

# This project provides two main api end points.

1 - For the hottest products, where you as an admin can publish from the django admin panel.
2 - And as for the second endpoint you can directly add products items directly from the UI (frontend)

### \_\_\_ENDPOINTS (available for the frontend application)

- http://localhost:8080/api/hotProducts
- http://localhost:8080/api/Products
- http://localhost:8080/api/featured

###### at the end of the this file i will provide the instructions on how to clone and run the project directly on your local machine

## Installing

### Requirements

In this project I am using python version is 3.10.0 and default db.sqlite3

#### For macOS

If you don't have it, install the python and django other extra requirements.
before running the project create a new virtual environment for the souls purpose of running one single projects and installing its dependencies

### Virtual environment

- Create a virtual environment `python3 -m venv venv`
- once the virtual environment is activated `source venv/bin/activate`
- Now you can go ahead clone the the repo and install dependencies. run `pip install -r requirements.txt`

#### Database setup

### Database setup is django default (sqlite)

In another terminal, run the following command to set up your admin user.

- `python manage.py createsuperuser`

This is only a local database, so don't worry about password security.
You can enter something like email: something@gmail.com, pwd: \*\*\*\*

### Static files

- Static files might not support or may need to be gives a correct folder path (depends)
