# 🚀 Django Backend Assignment

This is a fully dockerized Django REST Framework project built for a backend development internship assignment. It includes:

- ✅ Django REST API (public & protected endpoints)
- 🔐 Token Authentication (DRF)
- 📨 Celery + Redis for background task (send welcome email)
- 🤖 Telegram Bot API integration (/start saves username)
- ⚙️ Admin panel enabled
- 🐳 Docker & docker-compose for easy local development

---

## 📁 Project Structure

backend_project/
├── api/ # Main app: views, models, serializers, tasks
├── backend/ # Django settings, URLs, WSGI, Celery setup
├── telegram_bot/ # Telegram bot logic
├── Dockerfile # Docker build file
├── docker-compose.yml # Orchestration file
├── requirements.txt # Python dependencies
├── .env # Environment config (not in GitHub)
└── README.md


---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- [Docker Desktop] (https://www.docker.com/products/docker-desktop)
- VS Code or terminal
- GitHub account (to upload & share the repo)

---

## 🔐 Environment Variables

Create a `.env` file in the root folder (`backend_project/.env`) with:

```env
DEBUG=False
SECRET_KEY=your-django-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
TELEGRAM_BOT_TOKEN=your-telegram-bot-token


> ⚠️ Important: Never commit your actual `.env` file to GitHub. It should be listed in `.gitignore`.

## 💻 How to Run Locally

Make sure Docker is running, then follow these steps:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/gurusaiss/django-backend.git
cd django-backend

2️⃣ Add Your .env File
Create a file named .env and paste the variables shown above.

3️⃣ Build and Start the Containers
bash
Copy
Edit
docker-compose up --build
4️⃣ Run Migrations & Create Superuser
bash
Copy
Edit
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
5️⃣ Start the Celery Worker (New Terminal)
bash
Copy
Edit
docker-compose exec celery celery -A backend worker --loglevel=info
6️⃣ Start Telegram Bot
bash
Copy
Edit
docker-compose exec web python telegram_bot/bot.py
