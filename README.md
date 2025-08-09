
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

## Project Demo

<img width="1771" height="867" alt="5" src="https://github.com/user-attachments/assets/82558452-0c21-49f5-be22-ef5f223b8f30" />
<img width="1380" height="794" alt="2" src="https://github.com/user-attachments/assets/e1b474e8-3c7e-42b4-94a0-728ad9c84f2f" />
<img width="1376" height="760" alt="3" src="https://github.com/user-attachments/assets/ab445acb-c8ab-4b80-9e17-fbac54ccae7e" />
<img width="1360" height="727" alt="5" src="https://github.com/user-attachments/assets/ef689b85-a3df-40ba-ba49-c03a358b3f5a" />
<img width="1367" height="824" alt="6" src="https://github.com/user-attachments/assets/4eb4cb0a-33b3-4c0a-9db0-bbef58023874" />
<img width="1368" height="730" alt="7" src="https://github.com/user-attachments/assets/88dca760-19d4-4df8-b107-d29b84017c14" />
<img width="1358" height="716" alt="8" src="https://github.com/user-attachments/assets/fa5c5e7e-f59c-4f6c-b776-cd65f7b5ac68" />
