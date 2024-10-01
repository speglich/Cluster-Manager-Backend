# Job Management System - Backend

## Overview
This repository contains the backend code for the Job Management System designed to manage jobs on SLURM clusters. Built with Django and Django REST Framework, this API allows users to submit jobs, monitor their status, and retrieve logs and job history.

## Features
- **Job Submission**: Submit jobs to SLURM with customizable parameters.
- **Job Monitoring**: Check the status of submitted jobs.
- **Log Access**: Retrieve logs for job output and errors.
- **Job History**: View historical data on submitted jobs.

## Technologies Used
- **Django**: Web framework for building the API.
- **Django REST Framework**: Toolkit for building Web APIs.
- **SLURM**: Workload manager for job scheduling.
- **PostgreSQL/MySQL**: Database for storing job information.
- **Docker**: For containerization and easy deployment.

## Requirements
- Python 3.8 or later
- Django 3.2 or later
- Django REST Framework
- PostgreSQL or MySQL
- SLURM installed on the server

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/job-management-system-backend.git
cd job-management-system-backend
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database Settings
Edit the `settings.py` file to configure your database settings. Ensure you have PostgreSQL or MySQL installed and a database created for this project.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',  # or '3306' for MySQL
    }
}
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/api/`.

## API Endpoints
- **Submit Job**: `POST /api/jobs/submit/`
- **List Jobs**: `GET /api/jobs/`
- **View Job**: `GET /api/jobs/<job_id>/`
- **Cancel Job**: `POST /api/jobs/<job_id>/cancel/`
- **Job Logs**: `GET /api/jobs/<job_id>/logs/`
- **Job History**: `GET /api/jobs/history/`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
