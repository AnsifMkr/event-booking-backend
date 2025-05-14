# 🎟️ Event Booking Backend

This is the backend API for the Event Booking application built using **Django** and **Django REST Framework**. It supports features like user authentication, event management, and booking.

## 🌐 Live Demo (Optional)
> [deployed link( on Render)](https://event-booking-backend-rsnj.onrender.com/)

---

## 📂 Features

- 🔐 User Registration & JWT Authentication
- 📅 Event Creation & Listing
- 🧾 Booking System with Seat Availability Check
- 🖼️ Event Image Upload
- 👩‍💼 Admin Dashboard Access

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Django 4+**
- **Django REST Framework**
- **Simple JWT** for Authentication
- **SQLite / PostgreSQL** (configurable)
- **CORS Headers**

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AnsifMkr/event-booking-backend.git
cd event-booking-backend
```

### 2. Create virtual environment and activate
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```

### 📡 API Endpoints
| Method | Endpoint            | Description                |
| ------ | ------------------- | -------------------------- |
| GET    | /api/events/        | List all events            |
| POST   | /api/create-event/  | Create a new event (admin) |
| POST   | /api/book-event/    | Book an event              |
| GET    | /api/my-bookings/   | View user bookings         |
| POST   | /api/token/         | Obtain JWT token           |
| POST   | /api/token/refresh/ | Refresh JWT token          |

### 🧪 Authentication
 Authentication is done using JWT tokens:
1.Obtain token:
```http
POST /api/token/
```
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
2.Use token in requests:
```makefile
Authorization: Bearer <your_access_token>
```

### 🖼️ Image Upload Support
Ensure MEDIA_ROOT and MEDIA_URL are correctly configured in settings.py. Example:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
And add the following to urls.py in development:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 📄 License
This project is open source and available under the MIT License.

### ✨ Author
Developed by Ansif
