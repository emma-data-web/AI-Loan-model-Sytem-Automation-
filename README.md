# ML Loan Default Prediction API

A machine learning backend for predicting the likelihood of loan default.

The project combines a **LightGBM machine learning model** with a **FastAPI** backend, providing an API through which loan information can be submitted for prediction.

The application is containerized with **Docker** and **Docker Compose**, with **Alembic** used for database migrations.

## Tech Stack

* Python 3.12
* LightGBM
* FastAPI
* Alembic
* SQLAlchemy
* Docker
* Docker Compose
* Poetry

## Architecture

```text
Loan Data
    │
    ▼
LightGBM Model
    │
    │ prediction
    ▼
FastAPI
    │
    ▼
REST API
```

The machine learning model is responsible for generating the loan default prediction, while FastAPI provides the HTTP interface for interacting with the model.

## Features

* Loan default prediction using LightGBM
* REST API built with FastAPI
* Database integration
* Database migrations with Alembic
* Dependency management with Poetry
* Dockerized application
* Docker Compose configuration for local development and deployment

## Project Structure

```text
.
├── app/
│   ├── ...
│   └── ...
├── alembic/
│   ├── versions/
│   └── ...
├── Dockerfile
├── compose.yaml
├── alembic.ini
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Machine Learning Model

The prediction model is built using **LightGBM**, a gradient boosting framework designed for efficient and high-performance machine learning.

The trained model is integrated into the FastAPI application so that predictions can be requested through an API endpoint.

The general prediction flow is:

```text
Client
  │
  │ loan information
  ▼
FastAPI
  │
  ▼
Preprocessing
  │
  ▼
LightGBM Model
  │
  ▼
Default Prediction
  │
  ▼
API Response
```

## Dependency Management

The project uses **Poetry** for Python dependency management.

Install dependencies with:

```bash
poetry install
```

Add a dependency with:

```bash
poetry add <package>
```

Run the application through Poetry:

```bash
poetry run uvicorn app.main:app --reload
```

## Database Migrations

The project uses **Alembic** for managing database schema migrations.

Create a migration:

```bash
poetry run alembic revision --autogenerate -m "migration message"
```

Apply migrations:

```bash
poetry run alembic upgrade head
```

Rollback the latest migration:

```bash
poetry run alembic downgrade -1
```

## Environment Variables

Create a `.env` file containing the configuration required by the application.

For example:

```env
DATABASE_URL=...
SECRET_KEY=...
ALGORITHM=...
ACCESS_TOKEN_EXPIRATION=...
```

Do not commit `.env` files or other secrets to version control.

## Running Locally

Install the project dependencies:

```bash
poetry install
```

Run the FastAPI development server:

```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

## Running with Docker

Build the Docker image:

```bash
docker build -t loan-default-api .
```

Run the container:

```bash
docker run --env-file .env -p 8000:8000 loan-default-api
```

The API can then be accessed at:

```text
http://localhost:8000
```

## Running with Docker Compose

The project includes a Docker Compose configuration.

Start the application:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up --build -d
```

Stop the application:

```bash
docker compose down
```

## API Documentation

Once the application is running, FastAPI's interactive Swagger documentation is available at:

```text
http://localhost:8000/docs
```

ReDoc is available at:

```text
http://localhost:8000/redoc
```

## Purpose

This project demonstrates an end-to-end machine learning backend workflow:

1. Build a loan default prediction model using LightGBM.
2. Integrate the trained model into a FastAPI application.
3. Expose predictions through a REST API.
4. Manage database schema changes with Alembic.
5. Manage Python dependencies with Poetry.
6. Containerize the application with Docker.
7. Use Docker Compose to manage the application environment.
