# Little Lemon API Project

### Meta Full-Stack Developer Professional Certificate — Capstone

[![Link to Certificate](https://img.shields.io/badge/Verified-Coursera-blue)](https://www.coursera.org/account/accomplishments/specialization/KAXRBWPHGDMY)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)

## Project Overview
The **Little Lemon API** is a comprehensive back-end system developed as the final requirement for the Meta Full-Stack Professional Certificate. It serves as a restaurant management platform capable of handling user authentication, menu management, and booking systems via a RESTful architecture.

As an aspiring **Data Analyst**, I utilized this project to master the "under-the-hood" mechanics of data: how relational databases are structured, how APIs transmit data, and how Python can be used to automate complex server-side logic.

## Technical Stack
* **Language:** Python (managed via Pipenv)
* **Backend Framework:** Django & Django Rest Framework (DRF)
* **Database Management:** SQLite (Relational Schema Design)
* **Authentication:** Djoser (JWT & Token-based)
* **API Testing:** Insomnia / Postman

## Key Features & Data Logic
* **Relational Database Management:** Designed and implemented schemas to manage relationships between Menu Categories, Items, and Customer Orders.
* **Role-Based Access Control (RBAC):** Configured permission classes to secure data access for Managers, Delivery Crew, and Customers.
* **Filtering & Search:** Implemented server-side logic to allow efficient querying and sorting of the restaurant's menu dataset.
* **Data Integrity:** Integrated Django serializers to validate incoming data and ensure consistency across the database.

## Repository Structure
* `/LittleLemon` - Main project configuration and settings.
* `/LittleLemonAPI` - Application logic including Models, Serializers, and ViewSets.
* `manage.py` - Django administrative command-line utility.
* `Pipfile` & `Pipfile.lock` - Python dependency management files.
* `db.sqlite3` - Local relational database file.

## Installation & Setup
To run this project locally:

1. **Clone the repository:**
```
git clone [https://github.com/realAltamashAli/meta-full-stack-capstone.git](https://github.com/realAltamashAli/meta-full-stack-capstone.git)
```

2. **Install dependencies (using Pipenv):**
```
pipenv install
```

3. **Activate the virtual environment:**
```
pipenv shell
```

4. **Run Migrations:**
```
python manage.py migrate
```

5. **Start the server:**
```
python manage.py runserver
```
## Developed as part of the Meta Professional Certification program.
