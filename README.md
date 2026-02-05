# FastAPI Clean Architecture

Professional REST API (AUTH + CRUD) built with FastAPI, focused on best practices used in corporate backend development.

## Features

- Basic user CRUD
- Password hashing
- Automated tests
- Docker support
- Clean modular architecture

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- Pytest
- Docker / Docker Compose

## Architecture

This project demonstrates a clean architecture structure:
- Separation of concerns
- Easy to extend
- Testable modules
- Company-style code layout

## Architecture Overview
- FastAPI for REST APIs
- MySQL for transactional data
- MongoDB for audit logs
- JWT authentication
- Clean separation between API, services and repositories

## Getting Started

To build and run the app:

```bash
docker-compose up --build
