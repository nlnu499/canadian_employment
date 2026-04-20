Canadian Employment Dashboard

Overview
The Canadian Employment Dashboard is a Django-based web application developed for the CPRO 2201 course at Red Deer Polytechnic.

This project analyzes Canadian employment data and presents it using interactive charts. The dataset was initially loaded from a CSV file and stored in a SQLite database, which is used for all analysis and visualization.

--------------------------------------------------

Key Features
- Dataset loaded from CSV and stored in database
- Data cleaning and validation
- Interactive charts using Chart.js
- Employment comparison across provinces
- Trend analysis over time
- Filtering by province

--------------------------------------------------

Technologies
Python 3.12
Django 6.0
SQLite
HTML and CSS
Chart.js

--------------------------------------------------

How to Run

Step 1:
git clone https://github.com/nlnu499/canadian_employment.git

Step 2:
cd canadian_employment
cd canadian_employment_dashboard

Step 3:
pip install django==6.0

Step 4:
python manage.py runserver

Step 5:
Open browser and go to:
http://127.0.0.1:8000/

--------------------------------------------------

Project Structure

canadian_employment/
│
├── canadian_employment_dashboard/
│   ├── settings.py        # project configuration
│   ├── urls.py            # main routing
│   ├── asgi.py
│   └── wsgi.py
│
├── dashboard/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── dashboard.html
│   │   ├── province.html
│   │   ├── distribution.html
│   │   └── trend.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py           # handles CSV input
│   ├── models.py          # database structure
│   ├── urls.py            # app routing
│   └── views.py           # application logic
│
├── db.sqlite3             # database file
├── employment_dataset.csv # initial dataset
├── manage.py              # project entry point
└── README.md

Dataset
The dataset includes:
Year
Month
Province
Employment (Millions)
Unemployment Rate
Employment Rate
Participation Rate

The CSV file was used to populate the database. The application now uses stored data for visualization.

--------------------------------------------------

Data Processing
- Removed invalid or missing rows
- Cleaned text values
- Converted data into correct types
- Stored cleaned data in SQLite database

--------------------------------------------------

Insights
- Ontario has the highest employment
- Smaller provinces show lower values
- Trends remain stable over time
- Rates provide better comparison than totals

--------------------------------------------------

Project Structure
The project follows Django structure:
Models handle database
Views handle logic
Templates handle UI

--------------------------------------------------

Authors
Nikita
Raman
Taran

--------------------------------------------------

Course Details
CPRO 2201 Python Programming II
Red Deer Polytechnic
Winter 2026


--Youtube link https://youtu.be/0PtUUnMDiSk?si=sh8wbwLxF_WzK8DB


--------------------------------------------------

Conclusion
This project shows how Django can be used to build a data-driven web application using real data, database storage, and visualization.
