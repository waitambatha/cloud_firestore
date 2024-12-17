
# 🚀 **Django User Profile API**

This project is a simple **User Profile Management System** built with **Django** and **Django REST Framework (DRF)**. It allows users to create, view, update, and delete user profiles via a REST API.

Each user profile includes the following information:
- **Name**
- **Address**
- **Phone Number**
- **Next of Kin**
- **Next of Kin Phone Number**
- **DNR Status** (Do Not Resuscitate)
- **NFC Tag Available** (If the person has an NFC tag)

---

## 📋 **Features**
- 🧑‍🤝‍🧑 **User Profile Management** (CRUD operations)
- 📜 **Swagger API Documentation** (`/swagger/`)
- 🌐 **API Endpoints** (`/api/users/`)

---

## 🛠️ **Project Setup**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/waitambatha/cloud_firestore
cd cloud_firestore
```

### 2️⃣ **Set up a Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
```

### 3️⃣ **Install Requirements**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ **Run the Development Server**
```bash
python manage.py runserver
```

The server will be available at **http://127.0.0.1:8000/**.

---

## 📚 **API Endpoints**

| **Method** | **Endpoint**           | **Description**        |
|------------|----------------------|-----------------------|
| `GET`      | `/api/users/`          | List all user profiles |
| `POST`     | `/api/users/`          | Create a new profile   |
| `GET`      | `/api/users/{id}/`     | Get profile by ID      |
| `PUT`      | `/api/users/{id}/`     | Update a profile       |
| `DELETE`   | `/api/users/{id}/`     | Delete a profile       |

---

## 🔥 **How to Use**

1. Visit **http://127.0.0.1:8000/swagger/** to view the API documentation.  
2. Access the **User API** at **http://127.0.0.1:8000/api/users/**.  
3. Use the **POST** method to create a new user.  
4. Use the **GET, PUT, DELETE** methods to interact with existing user profiles.  

**Example Payload for POST /api/users/**
```json
{
    "name": "John Doe",
    "address": "1234 Elm Street, Springfield",
    "phone_number": "555-123-4567",
    "next_of_kin": "Jane Doe",
    "next_of_kin_phone_number": "555-987-6543",
    "dnr_status": true,
    "nfc_tag_available": false
}
```

---

## 🛠️ **Project Structure**
```
📂 firestore/
├── 📂 users/
│   ├── 📄 models.py       # UserProfile model
│   ├── 📄 views.py        # ViewSet for UserProfile
│   ├── 📄 serializers.py  # Serializer for UserProfile
│   └── 📄 admin.py        # Register model in Django admin
├── 📂 firestore/
│   ├── 📄 urls.py         # URL configuration
│   ├── 📄 settings.py     # Django project settings
├── 📂 templates/          # HTML templates
├── 📄 manage.py           # Django project entry point
```

---

## 🛠️ **Technologies Used**
- **Django** - For building the web application.
- **Django REST Framework** - To create the REST API.
- **Django Spectacular** - For generating Swagger documentation.

---

## 📘 **Environment Variables**
You may want to create a `.env` file to store sensitive information like database credentials, secret keys, etc.

---


---

## ✍️ **Contributing**
1. Fork the repo and clone it locally.  
2. Create a branch for your feature.  
3. Make your changes and push them to your branch.  
4. Create a Pull Request.  

---

