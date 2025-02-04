# Mango Export Management Web Application

A Django-based web application for managing mango export orders. This application enables CRUD (Create, Read, Update, Delete) operations for mango export entries with a custom sequential order numbering system that dynamically adjusts when records are modified.

## Features

- **CRUD Operations:** Easily create, view, update, and delete mango export entries.
- **Sequential Order ID:** A custom `order_id` field ensures that numbering remains sequential based on currently available records.
- **Form Validation:** Prevents duplicate mango varieties and ensures required fields are filled.
- **Search Functionality:** Filter mango export records by order ID.
- **Responsive & Attractive UI:** Uses Bootstrap 5 and Google Fonts (Roboto) for a modern, user-friendly interface.

## Technologies Used

- Python 3.x
- Django 5.1.3
- SQLite (default database)
- Bootstrap 5
- Google Fonts (Roboto)
