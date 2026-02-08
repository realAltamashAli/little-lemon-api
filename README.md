# Little Lemon API

### Meta Full-Stack Developer Professional Certificate — Capstone

[![Meta Certified](https://img.shields.io/badge/Certified-Meta-0668E1?logo=meta&logoColor=white)](https://www.coursera.org/account/accomplishments/specialization/KAXRBWPHGDMY)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## Project Overview
The **Little Lemon API** is a comprehensive back-end system developed as the final requirement for the Meta Full-Stack Professional Certificate. It serves as a restaurant management platform capable of handling user authentication, menu management, and booking systems via a RESTful architecture.

I developed this API to deepen my expertise in data lifecycle management. This project served as a deep dive into relational database architecture, the mechanics of API data transmission, and the use of Python for building automated, server-side data logic.

## Technical Stack
* **Language:** Python (managed via Pipenv)
* **Backend Framework:** Django & Django Rest Framework (DRF)
* **Database Management:** SQLite (Relational Schema Design)
* **Authentication:** Djoser (JWT & Token-based)
* **API Testing:** Pipenv / Insomnia / Postman

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

## Core Competencies Demonstrated
* **Database Architecture:** Understanding how to structure tables for optimal data retrieval.
* **Backend Automation:** Using Python to handle logic that would otherwise require manual data entry.
* **System Security:** Implementing industry-standard authentication to protect sensitive data records.
* **Environment Management:** Professional use of Pipenv for dependency isolation.

## Developed as part of the Meta Professional Certification program.
