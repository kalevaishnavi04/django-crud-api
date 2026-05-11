# 🚀 Django CRUD REST API Project

This is a simple backend project built using **Django** and **Django REST Framework (DRF)**.  
It demonstrates full CRUD (Create, Read, Update, Delete) operations using REST APIs.

## 📌 Features

✔ Create User (POST)  
✔ Get All Users (GET)  
✔ Update User (PUT)  
✔ Delete User (DELETE)  

## 🛠️ Tech Stack

- Python 🐍
- Django 🌐
- Django REST Framework (DRF)
- SQLite Database
- 
## 📂 Project Structure
backend_assignment/
│
├── core/ # Main app
│ ├── models.py # Database models
│ ├── views.py # API logic
│ ├── urls.py # App routes
│ ├── serializers.py # Data conversion
│
├── backend/ # Project settings
├── manage.py

## 🚀 How to Run Project

### 1. Clone repo

git clone https://github.com/your-username/django-crud-api.git

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install django djangorestframework

### 4. Run migrations
python manage.py makemigrations
python manage.py migrate

### 5. Start server
python manage.py runserver

## 🔗 API Endpoints
### 📌 Get Users
GET /api/users/

### 📌 Create User
POST /api/create/

### 📌 Update User
PUT /api/update/<id>/

### 📌 Delete User
DELETE /api/delete/<id>/

## 📌 Sample JSON (POST/PUT)

```json
{
    "name": "Vaishnavi",
    "email": "test@gmail.com",
    "phone": "1234567890"
}
