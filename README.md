# Canadian Employment Dashboard

## Overview
The Canadian Employment Dashboard is a Django-based web application developed for the CPRO 2201 course at Red Deer Polytechnic.

The project analyzes Canadian employment data and presents it through interactive charts and a simple web interface. The dataset is initially loaded from a CSV file and stored in a SQLite database for further analysis.

---

## Key Features
- Initial dataset loaded from CSV into database
- Data cleaning and validation before storage
- Interactive visualizations using Chart.js
- Employment comparison across provinces
- Trend analysis over time
- Province-based filtering

---

## Technologies
- Python 3.12
- Django 6.0
- SQLite
- HTML, CSS
- Chart.js

---

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/nlnu499/canadian_employment.git
Navigate to Project Folder
cd canadian_employment
cd canadian_employment_dashboard
Install Dependencies
pip install django==6.0
Run the Application
python manage.py runserver
Open in Browser
http://127.0.0.1:8000/
Dataset

The dataset contains Canadian employment statistics including:

Year and Month
Province
Employment values
Unemployment rate
Employment rate
Participation rate

The CSV file was used to populate the database, which is now used for visualization.

Data Processing
Removed invalid and incomplete rows using error handling
Cleaned text values using string methods
Converted data types into integers and floats
Stored validated data in SQLite database
Insights
Ontario has the highest employment levels
Smaller provinces show lower employment values
Employment trends remain stable across years
Rates provide better comparison than total employment
Project Structure

The project follows Django’s standard structure:

Models handle database structure
Views manage application logic
Templates display the user interface
Authors

Nikita
Raman
Taran

Course Details

CPRO 2201 – Python Programming II
Red Deer Polytechnic
Winter 2026

Conclusion

This project demonstrates how Django can be used to build a data-driven application by combining data processing, database management, and visualization techniques.
