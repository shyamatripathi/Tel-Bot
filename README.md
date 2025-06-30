# Django Project

This is a backend-focused Django project it demonstrates practical implementation of:
- Django REST Framework (DRF)
- JWT Authentication
- Celery with Redis
- Telegram Bot integration
- Clean code management using .env configuration

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/shyamatripathi/Tel-Bot
cd internship-project
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables
Create a `.env` file in the root directory:
```
SECRET_KEY=your-secret-key
DEBUG=False
EMAIL_HOST=your-email-host
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password
```

---

## Running the Project Locally

### 1. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Create Superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 3. Run the Server
```bash
python manage.py runserver
```

---

## Running Background Worker (Celery)

Start Redis server (must be installed separately):
```bash
redis-server
```

Start Celery worker:
```bash
celery -A project worker --loglevel=info
```

---

## Running the Telegram Bot

Before running, make sure to:
- Replace BOT_TOKEN in `telegram_bot.py` with the actual bot token.(I have used dummy token to publish)

Then run:
```bash
python telegram_bot.py
```

---

## API Endpoints
Example JWT login request:
```json
POST /api/token/
{
  "username": "",
  "password": ""
}
```

## Features Implemented

- Django REST Framework APIs
- JWT Authentication
- Background task via Celery and Redis
- Telegram bot integration
- Environment-based configuration
- Admin interface for viewing Telegram users

---

## Author

Shyama Tripathi  
Email:shyamatripathi101@gmail.com
GitHub: https://github.com/shyamatripathi

---

## Notes
- The application runs locally.
- API can be tested using Postman or curl.
