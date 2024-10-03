# Book Manager API

Welcome to the Book Manager API, a RESTful application built with Django and Django REST Framework. This API allows users to efficiently manage books and their associated authors, providing functionalities to create, retrieve, update, and delete records.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing the API](#testing-the-api)
- [License](#license)

## Features

- **Manage Authors**: Create, retrieve, update, and delete author records.
- **Manage Books**: Create, retrieve, update, and delete book records.
- **Associations**: Books can be linked to authors, allowing for organized data management.

## Technologies

- **Django**: A high-level Python web framework that encourages rapid development.
- **Django REST Framework**: A powerful toolkit for building Web APIs in Django.
- **SQLite**: A lightweight database engine used for development.

## Installation

Follow these steps to set up the Book Manager API locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/book_manager.git
   cd book_manager

2. **Set up a virtual environment**:
	```bash
	python -m venv venv
	source venv/bin/activate  # Use `venv\Scripts\activate` on Windows


3.	**Install the required packages**:
	```bash
	pip install -r requirements.txt


4.	**Apply database migrations**:
	```bash
	python manage.py migrate


5.	**(Optional) Create a superuser to access the Django admin panel**:
	```bash
	python manage.py createsuperuser


6.	**Run the development server**:
	```bash
	python manage.py runserver



Your API should now be accessible at http://localhost:8000/api/.

#Usage

##API Endpoints

The following endpoints are available in the API:

##Books

	•	GET /api/books/ - List all books.
	•	POST /api/books/ - Create a new book.
	•	GET /api/books/<int:pk>/ - Retrieve a specific book by its ID.
	•	PUT /api/books/<int:pk>/ - Update a specific book by its ID.
	•	DELETE /api/books/<int:pk>/ - Delete a specific book by its ID.

Authors

	•	GET /api/authors/ - List all authors.
	•	POST /api/authors/ - Create a new author.
	•	GET /api/authors/<int:pk>/ - Retrieve a specific author by their ID.
	•	PUT /api/authors/<int:pk>/ - Update a specific author by their ID.
	•	DELETE /api/authors/<int:pk>/ - Delete a specific author by their ID.

#Testing the API

You can test the API endpoints using tools like curl, Postman, or any REST client of your choice. Below are some example commands to help you get started.

##Example with curl

	•	Create a new author:
 	```bash
	curl -X POST http://localhost:8000/api/authors/ \
	-H "Content-Type: application/json" \
	-d '{"name": "Author Name"}'


Create a new book:

curl -X POST http://localhost:8000/api/books/ \
-H "Content-Type: application/json" \
-d '{"title": "Book Title", "author": 1, "isbn": "1234567890123"}'


	•	Update a book:

curl -X PUT http://localhost:8000/api/books/1/ \
-H "Content-Type: application/json" \
-d '{"title": "Updated Book Title", "author": 1, "isbn": "9876543210987"}'


	•	Retrieve a specific book:

curl -X GET http://localhost:8000/api/books/1/


	•	Delete a book:

curl -X DELETE http://localhost:8000/api/books/1/



License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to modify any section to better fit your project or personal style. This README should give users a clear understanding of your project, how to set it up, and how to interact with the API!
