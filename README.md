# Bodynetic Backend

## ✨ Create a new `.env` file using sample `env.sample`

The meaning of each variable can be found below: 

- `DEBUG`: if `True` the app runs in develoment mode
  - For production value `False` should be used
- `ASSETS_ROOT`: used in assets management
  - default value: `/static/assets`
- `OAuth` via Github
  - `GITHUB_ID`=<GITHUB_ID_HERE>
  - `GITHUB_SECRET`=<GITHUB_SECRET_HERE> 

<br />

## ✨ How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-soft-ui-dashboard.git
$ cd django-soft-ui-dashboard
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py generate-api     # optional
```

<br />

> Start the app

```bash
$ python manage.py runserver
// OR with https
$ python manage.py runsslserver 
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py generate-api     # optional
```

<br />

> Start the app

```bash
$ python manage.py runserver
// OR with https
$ python manage.py runsslserver 
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## ✨ API Generator

This module helps to generate secure APIs using DRF via a simple workflow: 

- Edit/add your model in `apps/models.py`
- Migrate the database:
  - `python manage.py makemigrations apps` # this will generate the new SQL
  - `python manage.py migrate`             # this will apply the changes
- Update Configuration:
  - `core/settings.py`, section `API_GENERATOR` 
- Generate the API code:
  - `python manage.py generate-api`        # the new code is saved in `apps/api`
- Access the API in the browser:
  - `/api/MODEL_NAME/`

The API is secured using the JWT token provided by `/login/jwt/` request (username & password should be provided).  

- GET requests are public (GET all, get Item)
- Mutating requests are protected by token generated based on the user credentials (`username`, `pass`). 

> Two POSTMAN Collections are provided in the `media` directory: 

- [Books API](./media/api-books.postman_collection) - that uses PORT **5000* for the api
- [Books API 2](./media/api-books-docker.postman_collection) - that uses PORT **5085* for the api (default port in Docker)

In case both port are unusable in your environment, feel free to edit the files before POSTMAN import.

<br />

## ✨ Dynamic DataTables

This module helps to generate dynamic view for all models defined in `apps/models.py`. How to use it: 

- Edit/add your model in `apps/models.py`
- Migrate the database:
  - `python manage.py makemigrations` # this will generate the new SQL
  - `python manage.py migrate`             # this will apply the changes
- Update Configuration:
  - `core/settings.py`, section `DYNAMIC_DATATB` 
- Access the dynamic view in the browser:
  - `/datatb/MODEL_NAME/`  

<br />

## ✨ Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:8000/register/`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:8000/login/`

<br />

## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## PRO Version

> For more components, pages and priority on support, feel free to take a look at this amazing starter:

Bodynetic Dashboard is a premium Bootstrap 5 Design now available for download in Django. Made of hundred of elements, designed blocks, and fully coded pages, Bodynetic Dashboard PRO is ready to help you create stunning websites and web apps.

- 👉 [Bodynetic Dashboard PRO Django](https://appseed.us/product/soft-ui-dashboard-pro/django/) - product page
  - ✅ `Enhanced UI` - more pages and components
  - ✅ `Priority` on support
  
<br >

![Bodynetic Dashboard PRO - Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/170829870-8acde5af-849a-4878-b833-3be7e67cff2d.png)

<br />

---
[Bodynetic Dashboard](https://appseed.us/generator/soft-ui-dashboard/) Django - Open-source starter generated by **[AppSeed Generator](https://appseed.us/generator/)**.
