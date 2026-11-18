# Attendance Management System

A self-hosted attendance management system built with:

- Python
- FastAPI
- MySQL 8.4
- Nginx
- Docker
- Docker Compose
- HTML, CSS and JavaScript

## Requirements

- Git
- Docker Desktop
- Windows 10/11 with WSL 2 support

## Installation

1. Clone the repository:

   git clone YOUR_GITHUB_REPOSITORY_URL

2. Enter the project directory:

   cd my-website

3. Create your environment file:

   Copy-Item .env.example .env

4. Edit .env and set your own passwords and JWT secret.

5. Start the application:

   docker compose up --build -d

6. Open the website:

   http://localhost:8080

## Stop the application

docker compose down

## View running containers

docker compose ps

## View logs

docker compose logs -f

## Rebuild the application

docker compose up --build -d
