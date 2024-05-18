# Video Creator Django Project

This project is a Django-based web application for creating videos with running text. It uses Docker and Docker Compose for containerization.

---
## Prerequisites

- Docker
- Docker Compose


## Getting Started
### Clone the repository
```sh
git clone https://github.com/what1sloove/video-creator.git
cd video-creator
```
### Build and run the application using Docker Compose
```sh
docker-compose up --build
```
### Migrations
To apply migrations, use the following command inside the Docker container:
```sh
docker-compose run web python manage.py migrate
```
### Access the application
The application will be running at http://localhost:8000.

---
## Performed by

Vladislav Gavrikov