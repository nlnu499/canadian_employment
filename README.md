Canadian Employment Dashboard

Project Overview
The Canadian Employment Dashboard is a Django-based web application developed for the CPRO 2201 Python Programming II course at Red Deer Polytechnic.
The purpose of this project is to analyze Canadian employment data and present it in a clear and interactive way using charts and a web interface.

The application uses a CSV dataset as the initial data source, which is processed and stored in a SQLite database. The stored data is then used to generate visual insights.

Objectives
Work with real-world Canadian employment datasets
Store and retrieve data using a database
Apply Django architecture including models, views, and templates
Create interactive and meaningful data visualizations
Analyze employment trends across different provinces

Features
Initial dataset loaded from a CSV file and stored in a database
Data cleaning and preprocessing before storage
Interactive charts using Chart.js
Employment by Province using bar charts
Employment versus unemployment comparison
Employment distribution using pie charts
Employment trends using line charts
Filtering data by province for better analysis

Technologies Used
Python 3.12
Django 6.0
SQLite database
HTML and CSS
Chart.js for data visualization

How to Run the Project

Step 1: Clone the repository
git clone https://github.com/nlnu499/canadian_employment.git

Step 2: Navigate to the project folder
cd canadian_employment
cd canadian_employment_dashboard

Step 3: Install dependencies
pip install django==6.0

Step 4: Run the server
python manage.py runserver

Step 5: Open in browser
http://127.0.0.1:8000/

Project Structure

The project consists of two main parts:

The main Django project folder contains settings, configuration files, and URL routing.

The dashboard application contains all the core functionality including models, views, templates, and forms.

Templates are used to display the user interface, while models define the database structure and views handle the application logic.

Dataset

The dataset contains Canadian employment statistics including year, month, province, employment values, unemployment rate, employment rate, and participation rate.

The CSV file was used to initially load data into the system. The data is now stored in the SQLite database and used for analysis.

Data Processing

The data was cleaned before storing in the database.
Invalid or missing rows were removed using error handling.
Text values were cleaned using string methods.
Numeric values were converted into appropriate data types such as integers and floats.
Only valid and complete data was stored in the database.

Insights

Ontario has the highest employment due to its population size
Smaller provinces show lower employment values
Employment trends remain relatively stable over time
Employment rate provides a better comparison than total employment

Application Usage

The system loads employment data from the database and displays it through charts and dashboards.
Users can view different visualizations and filter data by province to analyze trends.

Authors

Nikita
Raman
Taran

Course Information

Course: CPRO 2201 Python Programming II
Institution: Red Deer Polytechnic
Term: Winter 2026

Conclusion

This project demonstrates how Django can be used to build a data-driven web application. It combines data processing, database management, and visualization to provide meaningful insights from real-world data.
