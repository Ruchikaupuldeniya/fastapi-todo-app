# 🚀 FastAPI To-Do Application

<h3 align="center">A RESTful Task Management API built with Python & FastAPI</h3>

<p align="center">
  A backend application designed to manage users and their tasks through clean RESTful APIs, database integration, and structured backend architecture.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic"/>
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" alt="Swagger"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-Backend%20Development-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
</p>

---

## 📌 Overview

**FastAPI To-Do Application** is a backend REST API project developed using Python and FastAPI.

The application provides functionality to manage users and their associated tasks. It demonstrates essential backend development concepts, including RESTful API design, CRUD operations, relational database integration, request validation, and modular project organization.

The project is designed to strengthen practical knowledge of modern Python backend development.

## ✨ Key Features

| Feature | Description |
|---|---|
| 👤 User Management | Create and retrieve user information |
| 📝 Task Management | Create and manage individual tasks |
| 🔗 User-Task Relationship | Associate tasks with their respective users |
| ➕ Create Operations | Add new users and tasks |
| 📖 Read Operations | Retrieve users and task information |
| ✏️ Update Operations | Update existing task details |
| 🗑️ Delete Operations | Remove tasks |
| 🔍 Data Validation | Validate request data using Pydantic |
| 🗄️ Database Integration | Store application data in MySQL/MariaDB |
| 📚 API Documentation | Interactive API documentation using Swagger UI |

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- Pydantic

### Database
- MySQL / MariaDB
- XAMPP
- PyMySQL

### API Development & Testing
- REST API
- Swagger UI
- Postman

### Development Tools
- Visual Studio Code
- Git
- GitHub

## 🏗️ Project Architecture

The application follows a modular backend structure to organize application logic and improve maintainability.

```text
fastapi-todo-app/
│
├── app/
│   ├── main.py
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   └── crud/
│
├── database/
│   └── schema.sql
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: The structure above illustrates the intended organization. Update it to match the actual repository files.*

## 🔗 API Endpoints

The application provides RESTful endpoints for user and task management.

### User Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Create a new user |
| GET | `/users/{user_id}` | Retrieve a user |

### Task Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/{user_id}/tasks` | Create a task for a user |
| GET | `/users/{user_id}/tasks` | Retrieve a user's tasks |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/users/{user_id}/tasks/{task_id}` | Retrieve a specific task |
| PUT | `/users/{user_id}/tasks/{task_id}` | Update a task |
| PATCH | `/users/{user_id}/tasks/{task_id}` | Partially update a task |
| DELETE | `/users/{user_id}/tasks/{task_id}` | Delete a task |

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Ruchikaupuldeniya/fastapi-todo-app.git
```

### 2. Navigate to the Project Directory

```bash
cd fastapi-todo-app
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file using `.env.example` as a reference.

Add your local database configuration using the variable names expected by the application.

**Important:** Never upload your actual `.env` file or database credentials to GitHub.

### 7. Database Configuration

- Start Apache and MySQL from XAMPP.
- Open phpMyAdmin.
- Create the required database.
- Import the SQL script from `database/schema.sql`.
- Configure the database connection in the application.

### 8. Run the Application

Start the FastAPI server using the appropriate application entry point.

For example, if the entry point is `app/main.py`:

```bash
uvicorn app.main:app --reload
```

## 📖 API Documentation

Once the application is running, access the interactive API documentation.

| Documentation | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

Swagger UI allows developers to explore, execute, and test API endpoints directly from the browser.

## 📸 Screenshots

Screenshots of the API documentation, request/response examples, and database operations will be added here.

## 🎯 Learning Objectives

Through this project, I am developing practical experience in:

- Building RESTful APIs using FastAPI.
- Understanding HTTP methods and API request/response handling.
- Implementing CRUD operations.
- Connecting Python applications with relational databases.
- Managing relationships between database entities.
- Validating request data using Pydantic.
- Organizing backend applications using modular architecture.
- Testing and documenting APIs.

## 🔮 Future Improvements

- Authentication and Authorization.
- JWT-based user authentication.
- Improved error handling and logging.
- Automated API testing.
- Docker containerization.
- API deployment.

## 👩‍💻 Author

**Ruchika Harshajith Upuldeniya**

BICT Undergraduate | AI/ML Engineer Intern | Backend Development Enthusiast

<p align="left">
  <a href="https://github.com/Ruchikaupuldeniya">
    <img src="https://img.shields.io/badge/GitHub-Ruchikaupuldeniya-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
  </a>
</p>

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>

<p align="center">
  <b>Built with Python, FastAPI, and a passion for learning. 🚀</b>
</p>
