# kpa_project


#  Wheel Specification Form API (Django + PostgreSQL)

A Django REST API to submit and fetch wheel specification data for railway components. Data is stored in PostgreSQL and supports dynamic nested field storage via JSONField.

---

##  Features

-  Submit a new wheel specification form (`POST`)
-  Retrieve filtered forms using query parameters (`GET`)
-  PostgreSQL integration with `.env` config
-  Fully tested via Postman
-  Organized Django project structure

---

##  Project Structure

```
kpa_project/
├── kpa_project/
│   ├── settings.py
│   ├── urls.py
├── wheel_spec/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── .env
|__venv
├── manage.py
└── README.md
```

---

##  Tech Stack

- **Backend:** Django 
- **API Framework:** Django REST Framework
- **Database:** PostgreSQL
- **Env Management:** python-dotenv
- **Testing:** Postman

---

## Requirements

Create a `requirements.txt` file:

```txt
asgiref==3.9.1
Django==5.2.4
djangorestframework==3.16.0
psycopg2-binary==2.9.10
python-decouple==3.8
sqlparse==0.5.3
tzdata==2025.2

```

Install all with:

```bash
pip install -r requirements.txt
```

---

## .env File

Place this in your project root:

```
DB_NAME=kpa_db
DB_USER=kpa_user
DB_PASSWORD=kpa_pass
DB_HOST=localhost
DB_PORT=5432
```

---

## PostgreSQL Setup

Run these in `psql` or pgAdmin:

```sql
CREATE DATABASE kpa_db;
CREATE USER kpa_user WITH PASSWORD 'kpa_pass';
ALTER ROLE kpa_user SET client_encoding TO 'utf8';
ALTER ROLE kpa_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE kpa_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE kpa_db TO kpa_user;
```

---

## settings.py (Partial)

In your Django settings:

```python
from dotenv import load_dotenv
import os

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}
```

Also ensure:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'wheel_spec',
]
```

---

##  API Usage (Postman)

###  POST `/api/forms/wheel-specifications/`

Send this JSON:

```json
{
  "fields": {
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "bearingSeatDiameter": "130.043 to 130.068",
    "condemningDia": "825 (800-900)",
    "intermediateWP": "20 TO 28",
    "lastShopIssueSize": "837 (800-900)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "treadDiameterNew": "915 (900-1000)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelDiskWidth": "127 (+4/-0)",
    "wheelGauge": "1600 (+2,-1)",
    "wheelProfile": "29.4 Flange Thickness"
  },
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03"
}
```

### GET `/api/forms/wheel-specifications`

Example:

```
/api/forms/wheel-specifications?formNumber=WHEEL-2025-001
```

Filters supported:
- `formNumber`
- `submittedBy`
- `submittedDate`

---
##  API Documentation

You can test or view the complete API docs here:
 [Postman API Docs](https://documenter.getpostman.com/view/37306365/2sB34foMVW)
 
##  Run Locally

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/api/forms/wheel-specifications/`

---

##  Git Commit Instruction

```bash
git init
git add .
git commit -m "Initial project setup with REST APIs for wheel specs using PostgreSQL"
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

---



##  Contact

For any issues or improvements, feel free to raise an issue or contact me directly.

---

##  End

Thanks for checking out this project!
