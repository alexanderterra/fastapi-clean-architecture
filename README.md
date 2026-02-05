![CI](https://github.com/alexanderterra/fastapi-clean-architecture/actions/workflows/ci.yml/badge.svg)

# FastAPI Clean Architecture

Professional backend project built with **FastAPI**, following clean architecture principles and real-world enterprise patterns.

This repository is intended as a **portfolio-grade example**, demonstrating how production-ready APIs are structured, secured and documented.

---

## Features

- REST API built with FastAPI
- JWT authentication (access token)
- Clean separation between API, services and repositories
- MySQL for transactional data
- MongoDB for audit logs
- Docker & Docker Compose ready
- Automated tests
- Versioned API (`/api/v1`)
- Health check endpoint for monitoring

---

## Tech Stack

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **MySQL**
- **MongoDB**
- **JWT (python-jose)**
- **Docker / Docker Compose**
- **Pytest**

---

## Architecture Overview

This project follows a **clean architecture–inspired structure**:

```text
app/
├── api/            # HTTP layer (FastAPI routers)
├── core/           # Security, config and shared dependencies
├── db/             # Database connections (MySQL / MongoDB)
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas
├── repositories/   # Data access layer
├── services/       # Business logic
└── main.py         # Application entry point
```

### Why this approach?

- Easy to test
- Easy to extend
- Clear responsibility per layer
- Matches patterns used in real companies

---

## Authentication

Authentication is based on **JWT access tokens**.

### Endpoints

| Method | Endpoint             | Description              |
|------:|----------------------|--------------------------|
| POST  | `/api/v1/auth/register` | Register new user        |
| POST  | `/api/v1/auth/login`    | Authenticate user        |
| GET   | `/api/v1/users/`        | Get users                |
| GET   | `/api/v1/users/me`      | Get current user profile |

All protected endpoints require:
- Authorization: Bearer <access_token>
- Passwords are hashed using **bcrypt**.

---

## Databases

### MySQL
Used for:
- Users
- Core transactional data

### MongoDB
Used for:
- Audit logs
- Authentication events
- Non-relational data

This hybrid approach reflects real-world system design.

---

## Environment Configuration

Create a `.env` file based on the example below:

```env
DATABASE_URL=mysql+pymysql://user:password@localhost/app
MONGODB_URI=mongodb://localhost:27017
SECRET_KEY=super-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
---

## Running With Docker

Command:

docker-compose up --build

API URL:
http://localhost:8000

Swagger / OpenAPI:
http://localhost:8000/docs

---

## Running Tests

Command:

pytest

Tests include:
- Authentication flow
- User registration
- Protected endpoints

---

## Health Check

Endpoint:
GET /health

Response:
{ "status": "ok" }

Used for:
- Docker health checks
- Kubernetes liveness/readiness probes
- Monitoring systems

---

## Project Intent

This repository is not a tutorial.

It is a professional demonstration project designed to:
- Showcase backend architecture skills
- Demonstrate JWT authentication and security
- Reflect how real APIs are structured in production
- Serve as a reference for technical interviews

Code from real commercial projects is intentionally omitted due to confidentiality.

---

## GIT Flow

- main : protected branch, stable versions only
- dev : development branch
- feature/* : feature branches

All changes go through Pull Requests.

---

## License

MIT
