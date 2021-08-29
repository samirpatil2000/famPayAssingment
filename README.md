# Youtube API



#### Tech Stacks
##### 1. Python , Django

# Installation to our django project

[![Python Version](https://img.shields.io/badge/python-3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2-brightgreen.svg)](https://djangoproject.com)

## Features
1. YouTube API continuously in the background (async) with 20 sec
2. Store the data in the database (title,desc, thumbnail, publish date,) with its category 
3. Advance searching and sorting with categories
4. Pagination, DashBoard
5. Works with multiple API keys 
6. Dockerize the project.

## Running the Project Locally

* First, clone the repository to your local machine:

```bash
https://github.com/samirpatil2000/famPayAssingment.git
```
* Create & Activate Virtual Environment For Windows

```bash
py -m venv env
.\env\Scripts\activate
```

* Create & Activate Virtual Environment For MacOs/Linux

```bash
python3 -m venv env
source env/bin/activate
```


* Install the requirements:

```bash
pip install -r requirements.txt
```


* Create the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

* Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.




#### Contributors





[Back to the top](#HackathonProject)



