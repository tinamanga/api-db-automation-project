<div align="center">

# 🚀 API DB Automation Project

### Production-Ready Backend API built with FastAPI, PostgreSQL, SQLAlchemy & Docker

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?logo=githubactions)
![License](https://img.shields.io/badge/License-MIT-green)

A scalable backend REST API demonstrating authentication, authorization,
clean architecture, Docker, CI/CD and modern backend engineering best practices.

</div>

---

# Table of Contents

- Features
- Architecture
- Technology Stack
- Project Structure
- Getting Started
- Environment Variables
- Database
- Docker
- Authentication
- API Endpoints
- Testing
- CI/CD
- Future Improvements
- Screenshots
- Contributing
- License
- Author

---

# Features

## Authentication

- User Registration
- User Login
- JWT Authentication
- Password Hashing (bcrypt)
- Current User Endpoint

---

## User Management

- View User
- Update User
- List Users
- Search Users
- Filter Users
- Pagination
- Sorting

---

## Security

- JWT Tokens
- Role Based Access Control
- Admin-only Routes
- Protected Endpoints
- Environment Variables
- Password Hashing
- SQL Injection Protection

---

## Database

- PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations

---

## Developer Experience

- Docker
- Docker Compose
- GitHub Actions CI
- Pytest
- Clean Architecture
- Service Layer Pattern

---

# Architecture

```
                Client

                  │

          HTTP Requests

                  │

            FastAPI Routes

                  │

          Authentication Layer

                  │

          Service Layer (Business Logic)

                  │

          SQLAlchemy ORM

                  │

             PostgreSQL
```

---

# Technology Stack

| Technology | Usage |
|------------|-------|
| Python 3.12 | Programming Language |
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database Migrations |
| Pydantic v2 | Validation |
| JWT | Authentication |
| Passlib | Password Hashing |
| Docker | Containerization |
| GitHub Actions | CI/CD |
| Pytest | Testing |

---

# Project Structure

```
api-db-automation-project
│
├── backend
│   │
│   ├── app
│   │   ├── api
│   │   ├── auth
│   │   ├── core
│   │   ├── database
│   │   ├── exceptions
│   │   ├── middleware
│   │   ├── models
│   │   ├── schemas
│   │   ├── services
│   │   ├── utils
│   │   └── main.py
│   │
│   ├── migrations
│   ├── tests
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── .github
│   └── workflows
│       └── ci.yml
│
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/tinamanga/api-db-automation-project.git

cd api-db-automation-project
```

---

## Create Virtual Environment

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
cd backend

pip install -r requirements.txt
```

---

# Environment Variables

Create

```
backend/.env
```

Example

```env
APP_NAME=API DB Automation
APP_VERSION=1.0.0

DEBUG=True

HOST=0.0.0.0
PORT=8000

SECRET_KEY=your-secret-key

JWT_SECRET_KEY=your-jwt-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

DATABASE_URL=postgresql://api_user:password@localhost:5432/api_db_automation
```

---

# Database Migration

Create migrations

```bash
alembic revision --autogenerate -m "Initial migration"
```

Run migrations

```bash
alembic upgrade head
```

---

# Run Locally

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Background

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

# Authentication Flow

```
Register

↓

Login

↓

Receive JWT Token

↓

Authorize

↓

Access Protected Endpoints
```

---

# API Endpoints

## Authentication

| Method | Endpoint |
|----------|----------------|
| POST | /auth/register |
| POST | /auth/login |

---

## Users

| Method | Endpoint |
|---------|----------------|
| GET | /users |
| GET | /users/me |
| GET | /users/{id} |
| PUT | /users/{id} |

Supports

- Pagination

```
?page=1&limit=10
```

Search

```
?search=john
```

Filter

```
?role=admin
```

Sort

```
?sort_by=email&order=asc
```

---

# Sample Response

Success

```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "access_token": "...",
    "token_type": "bearer"
  }
}
```

Error

```json
{
  "success": false,
  "error": "Unauthorized"
}
```

---

# Running Tests

Run all tests

```bash
pytest
```

Coverage

```bash
pytest --cov=app
```

---

# CI/CD

GitHub Actions automatically

- Installs dependencies
- Starts PostgreSQL
- Runs Tests
- Validates Pull Requests
- Validates Pushes

Workflow

```
Push

↓

GitHub Actions

↓

Install Dependencies

↓

Start PostgreSQL

↓

Run Pytest

↓

Pass ✅
```

---

# Screenshots

Create a folder

```
screenshots/
```

Add screenshots such as:

```
docs.png
login.png
register.png
users.png
docker.png
github-actions.png
```

Example

```markdown
![Swagger Docs](screenshots/docs.png)

![GitHub Actions](screenshots/github-actions.png)
```

---

# Future Improvements

- Email Verification
- Refresh Tokens
- Password Reset
- Rate Limiting
- Redis Cache
- Celery Background Tasks
- Audit Logs
- User Soft Delete
- OpenTelemetry Monitoring
- Kubernetes Deployment
- AWS Deployment
- Nginx Reverse Proxy

---

# Contributing

```bash
Fork Repository

↓

Create Feature Branch

↓

Commit Changes

↓

Push Branch

↓

Open Pull Request
```

---

# License

Licensed under the MIT License.

---

# Author

## Christina Manga

Backend Software Engineer

GitHub

https://github.com/tinamanga

LinkedIn

https://linkedin.com/in/christina-manga-aa314a370

Email

christinamanga28@gmail.com

---

<div align="center">

⭐ If you found this project useful, consider giving it a star!

Built with ❤️ using FastAPI, PostgreSQL, Docker & GitHub Actions.

</div>