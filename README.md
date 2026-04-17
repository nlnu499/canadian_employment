# 🇨🇦 Canadian Employment Dashboard

##  Project Overview

The **Canadian Employment Dashboard** is a Django-based web application developed for **CPRO 2201 – Python Programming II** at Red Deer Polytechnic.

This application allows users to upload a CSV dataset, store it in a database, and visualize Canadian employment statistics using interactive charts.

---

##  Objectives

* Work with real-world Canadian datasets (CSV)
* Store and retrieve data using SQLite database
* Implement Django architecture (models, views, templates, forms)
* Create meaningful data visualizations
* Analyze employment trends and generate insights

---

##  Features

*  Upload CSV dataset
*  Store cleaned data in SQLite database
*  Interactive charts using Chart.js:

  * Employment by Province (Bar Chart)
  * Employment vs Unemployment (Comparison Chart)
  * Employment Distribution (Pie Chart)
  * Employment Trend (Line Chart)
  
*  Data cleaning and preprocessing
*  Insight generation from data
*  Filter data by province (dynamic updates)

---

##  Technologies Used

* **Python 3.12**
* **Django 6.0**
* **SQLite Database**
* **HTML, CSS**
* **Chart.js (CDN)**

---

##  How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/nlnu499/canadian_employment.git
```

### 2. Navigate to Project Folder

```bash
cd canadian_employment_dashboard
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run the Server

```bash
python manage.py runserver
```

### 5. Open in Browser

```
http://127.0.0.1:8000/
```

---

##  Project Structure

```
canadian_employment_dashboard/
│
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
```

---

##  Dataset

The dataset contains Canadian employment statistics including:

* Year
* Month
* Province
* Employment (Millions)
* Unemployment Rate (%)
* Employment Rate (%)
* Participation Rate (%)

The database (`db.sqlite3`) is already populated using this dataset.

---

##  Data Processing

* Removed invalid rows using `try-except`
* Cleaned text using `.strip()`
* Converted values using `int()` and `float()`
* Ignored missing or incorrect values
* Stored cleaned data in SQLite database

---

##  Insights

* Ontario has the highest employment due to its large population
* Smaller provinces show lower employment values
* Employment trends remain relatively stable across years
* Employment rate provides better comparison than total employment

---

## Demo

The application allows users to:

* Upload a CSV dataset
* Store data into the database
* View interactive charts
* Filter data dynamically by province

---

##  Authors

* Nikita
* Raman
* Taran

---

##  Course Information

* **Course:** CPRO 2201 – Python Programming II
* **Institution:** Red Deer Polytechnic
* **Term:** Winter 2026

---

##  Conclusion

This project demonstrates how Django can be used to build a complete data-driven web application using real-world datasets, database integration, and interactive visualization tools.

---
