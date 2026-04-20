Canadian Employment Dashboard

Project Overview
The Canadian Employment Dashboard is a Django-based web application developed for the CPRO 2201 course at Red Deer Polytechnic.
It analyzes Canadian employment data and presents it using interactive charts.

Objectives
Work with real-world datasets
Store and manage data using a database
Apply Django structure (models, views, templates)
Create data visualizations
Analyze employment trends

Features
Initial dataset loaded from CSV and stored in SQLite database
Data cleaning and preprocessing
Interactive charts (bar, pie, line)
Employment analysis by province
Trend visualization over time

Technologies Used
Python 3.12
Django 6.0
SQLite
HTML and CSS
Chart.js

How to Run

Step 1: Clone the repository

git clone https://github.com/nlnu499/canadian_employment.git

Step 2: Navigate to the project

cd canadian_employment
cd canadian_employment_dashboard

Step 3: Install dependencies

pip install django==6.0

Step 4: Run the server

python manage.py runserver

Step 5: Open in browser

http://127.0.0.1:8000/

Dataset
The dataset includes year, month, province, employment values, and rates.
It was used to populate the database, which is now used for analysis.

Data Processing
Invalid data removed using error handling
Text cleaned using string methods
Values converted to correct data types
Cleaned data stored in SQLite

Insights
Ontario has the highest employment
Smaller provinces show lower values
Trends remain stable over time

Authors
Nikita
Raman
Taran

Course Information
CPRO 2201 Python Programming II
Red Deer Polytechnic
Winter 2026

Conclusion
This project demonstrates how Django can be used to build a data-driven application with database integration and visualization.
