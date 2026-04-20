 Canadian Employment Dashboard
 Project Overview

The Canadian Employment Dashboard is a Django-based web application developed as part of the CPRO 2201 – Python Programming II course at Red Deer Polytechnic.

This project allows users to upload a CSV dataset, store it in a database, and visualize Canadian employment statistics through interactive charts. The goal is to demonstrate how data can be processed and presented in a meaningful way using web technologies.

** Objectives**
Work with real-world Canadian employment datasets (CSV format)
Store and retrieve data using an SQLite database
Apply Django architecture (models, views, templates, forms)
Create clear and interactive data visualizations
Analyze employment trends and generate insights
** Features**
Upload employment data using a CSV file
Automatically clean and store data in SQLite database
Interactive charts using Chart.js:
Employment by Province (Bar Chart)
Employment vs Unemployment (Comparison Chart)
Employment Distribution (Pie Chart)
Employment Trend (Line Chart)
Data cleaning and validation
Dynamic filtering by province
Insight generation based on data
** Technologies Used**
Python 3.12
Django 6.0
SQLite Database
HTML, CSS
Chart.js (via CDN)
** How to Run the Project**
1. Clone the Repository
git clone https://github.com/nlnu499/canadian_employment.git
2. Navigate to the Project Folder
cd canadian_employment
cd canadian_employment_dashboard
3. Install Dependencies
pip install django==6.0
4. Run the Server
python manage.py runserver
5. Open in Browser
http://127.0.0.1:8000/
**Project Structure**
canadian_employment_dashboard/

├── dashboard/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── dashboard.html
│   │   ├── province.html
│   │   ├── distribution.html
│   │   ├── trend.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│
├── canadian_employment_dashboard/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── db.sqlite3
├── employment_dataset.csv
├── manage.py
├── README.md
** Dataset**

The dataset contains Canadian employment statistics, including:

Year
Month
Province
Employment (Millions)
Unemployment Rate (%)
Employment Rate (%)
Participation Rate (%)

The database (db.sqlite3) is already populated using this dataset.

 **Data Processing**
Removed invalid or missing rows using try-except
Cleaned text values using .strip()
Converted data types using int() and float()
Ignored incorrect or incomplete data
Stored cleaned data into the SQLite database
** Insights**
Ontario has the highest employment due to its large population
Smaller provinces show lower employment values
Employment trends remain relatively stable over time
Employment rate provides a better comparison than total employment
** Demo**

The application allows users to:

Upload a CSV dataset
Store data in the database
View interactive charts and dashboard
Filter data dynamically by province
**Authors**
Nikita
Raman
Taran
** Course Information**
Course: CPRO 2201 – Python Programming II
Institution: Red Deer Polytechnic
Term: Winter 2026
** Conclusion**

This project demonstrates how Django can be used to build a complete data-driven web application. It combines data processing, database management, and interactive visualization to provide meaningful insights from real-world datasets.
