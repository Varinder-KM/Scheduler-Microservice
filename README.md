# Scheduler Microservice

## Overview
This project is a microservice built using Django and Celery that allows for job scheduling and management. The service provides API endpoints to create, list, and retrieve details of scheduled jobs. It is designed to handle a large volume of requests and is scalable to meet high-performance requirements.


## Features
* Job Scheduling: Schedule jobs with customizable intervals (e.g., daily, weekly, monthly).
* API Endpoints:
  * GET /jobs: List all scheduled jobs.
  * GET /jobs/:id: Retrieve details of a specific job by ID.
  * POST add_job/: Create a new job.
* Database Integration: Store job details such as job name, last run timestamp, next run timestamp, and scheduling interval.
* Scalability: Designed to handle up to 10,000 users, 1,000 services, and 6,000 API requests per minute.

## Technologies Used
* Django: Web framework for building the API endpoints and managing the database.
* Celery: Distributed task queue for job scheduling and execution.
* Redis: In-memory data structure store, used as a message broker for Celery.
* SQLite: Default database for development (can be replaced with PostgreSQL or MySQL in production).

## Prerequisites
* Python 3.8+
* Redis server
* Django 3.2+
* Celery 5.2+
* Virtualenv (optional, but recommended)



## Installation
1. Clone the Repository

``git clone https://github.com/your-username/scheduler-microservice.git``

``cd scheduler-microservice``

2. Set Up a Virtual Environment
   
``python -m venv venv``

``source venv/bin/activate``

3. Install Dependencies
``pip install -r requirements.txt``

4. Configure Environment Variables
Create a .env file in the root directory and add the following environment variables:

``SECRET_KEY=your-secret-key``

``DEBUG=True``

``CELERY_BROKER_URL=redis://127.0.0.1:6379/0``

``CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/0
``

5. Apply Migrations

``python manage.py migrate``

6. Start the Redis Server
Ensure Redis is installed and running:
``redis-server``

7. Start the Celery Worker
``celery -A scheduler_service worker --loglevel=info``

8. Start the Celery Beat Scheduler
``celery -A scheduler_service beat --loglevel=info``

9. Run the Django Development Server
``python manage.py runserver``



## API Endpoints
* List All Jobs
``GET /jobs``

* Retrieve Job Details by ID
``GET /jobs/:id``

* Create a New Job
``POST /add_jobs/``

* Sample Request Body
``{
    "job_name": "Send Weekly Report",
    "schedule_interval": "weekly"
}``
