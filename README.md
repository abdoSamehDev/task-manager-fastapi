# Task Manager

## Overview

Task Manager is a web application built with FastAPI and PostgreSQL. This application allows users to manage tasks, including creating, updating, and deleting tasks. It also supports user authentication and authorization.

## Features

- User registration and authentication
- Task creation, retrieval, updating, and deletion
- JWT-based authentication
- PostgreSQL database integration
- Dockerized setup for easy deployment

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/abdoSamehDev/task-manager-fastapi.git
cd task_manager
```

### 2. Clone the Repository

Create a .env file in the app directory and add the following variables:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
DATABASE_URL=postgres://postgres:yourpassword@db:5432/postgres
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace yourpassword and your_secret_key with your own values.

### 3. Build and Run with Docker

```sh
docker-compose up --build
```

This will build the Docker images and start the containers. The application will be available at http://localhost:8000.

## API Documentation

The API documentation is available at http://localhost:8000/docs (Swagger UI) and http://localhost:8000/redoc (ReDoc).

## Usage

### 1. Register a New User

Send a POST request to `/` with the following payload:

```json
{
  "email": "youremail@example.com",
  "password": "yourpassword"
}
```

### 2. Authenticate

Send a POST request to `/token` with the following payload:

```json
{
  "username": "youremail@example.com",
  "password": "yourpassword"
}
```

You will receive an access token that you can use to authenticate subsequent requests.

### 3. Create a Task

Send a POST request to `/tasks` with the following payload:

```json
{
  "title": "Your Task Title",
  "descriptiom": "Your Task Description"
}
```

Include the access token in the Authorization header:

```makefile
Authorization: Bearer your_access_token
```

## Development

### 1. Install Dependencies

if you want to run the application without Docker, install the dependencies

```sh
pip install -r requirements.txt
```

### 2. Run the Application

```sh
uvicorn app.main:app --reload
```

The application will be available at http://localhost:8000.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
