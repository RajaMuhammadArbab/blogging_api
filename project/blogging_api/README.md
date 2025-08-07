
# Blogging Platform API

This is a Django REST Framework-based API for a simple blogging system.

##  Features

- User Registration and Login (JWT Authentication)
- Create, Read, Update, Delete (CRUD) for Blog Posts
- Add, View, Delete Comments on Posts
- Role-based Access Control (users can modify only their content)
- Error handling and proper HTTP response codes

##  Project Structure

```
blogging_api/
├── blog/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── blogging_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
```

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd blogging_api
```

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database

- Create a PostgreSQL database and user.
- Update `settings.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your-db-name>',
        'USER': '<your-db-user>',
        'PASSWORD': '<your-db-password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Start Server

```bash
python manage.py runserver
```

### 8. Test with Postman

- Register: `POST /api/register/`
- Login: `POST /api/token/`
- CRUD Posts: `GET/POST/PUT/DELETE /api/posts/`
- Comments: `POST /api/posts/<id>/comments/`

##  Requirements

- Python 3.10+
- Django 4.x
- djangorestframework
- psycopg2 (for PostgreSQL)
- SimpleJWT

##  Export Database (Optional)

To dump your PostgreSQL database:

```bash
pg_dump -U <username> -d <dbname> -f blogging_backup.sql
```

---
