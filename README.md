# 🚖 Uber Data Engineering Pipeline

## 📌 Overview

This project demonstrates a complete **end-to-end data engineering pipeline** built using Python. The pipeline processes Uber trip data, performs data transformation, and loads it into a relational database for analysis and visualization.

The project simulates a **real-world ETL (Extract, Transform, Load) workflow** and implements a **star schema data model** to support efficient querying.

---

## 🎯 Objectives

* Build a scalable ETL pipeline using Python
* Clean and preprocess raw Uber trip data
* Perform feature engineering on datetime and categorical fields
* Design a **star schema** (fact + dimension tables)
* Load transformed data into **PostgreSQL**
* Enable data visualization using **Tableau**

---

## 🛠️ Tech Stack

* **Python (Pandas, SQLAlchemy)**
* **PostgreSQL**
* **Tableau Desktop**
* **Git & GitHub**

---

## 📂 Project Structure

```plaintext
uber-data-pipeline/
├── data/
│   └── uber_data.csv
├── scripts/
│   ├── __init__.py
│   ├── load.py
│   ├── transform.py
│   └── load_to_db.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline Workflow

### 🔹 1. Data Ingestion (Extract)

* Load raw Uber dataset from local CSV using Pandas

### 🔹 2. Data Transformation (Transform)

* Convert datetime columns
* Remove duplicates
* Extract time-based features (hour, day, month, year)
* Create dimension tables:

  * Datetime
  * Passenger Count
  * Payment Type

### 🔹 3. Data Modeling

* Implemented **Star Schema**:

  * **Fact Table** → trip-level data
  * **Dimension Tables** → descriptive attributes

### 🔹 4. Data Loading (Load)

* Load processed data into PostgreSQL using SQLAlchemy

---

## 🧠 Data Model (Star Schema)

<img src=images/uber_data_model.jpeg>


## ▶️ How to Run

### 1. Clone repository

```bash
git clone https://github.com/MohammedTouqeerUrRaiyan/Uber-data-pipeline-project.git
cd uber-data-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

* Create database:

```sql
CREATE DATABASE uber_db;
```

* Update connection string in `load_to_db.py`:

```python
engine = create_engine("postgresql://username:password@127.0.0.1:5432/uber_db")
```

---

### 5. Run pipeline

```bash
python main.py
```

---

## 📊 Output

The pipeline generates:

* Dimension tables
* Fact table
* Structured dataset ready for analytics

---

## 📈 Tableau Integration

* Connect Tableau to PostgreSQL
* Use fact + dimension tables
* Build dashboards such as:

  * Revenue analysis
  * Trip trends by time
  * Payment method distribution

---

## 🚀 Future Improvements

* Add **Apache Airflow** for orchestration
* Integrate with **cloud platforms (AWS/GCP)**
* Optimize queries using indexing
* Handle large-scale data using **Apache Spark**

---

## 💡 Key Highlights

* Built **end-to-end ETL pipeline**
* Implemented **star schema modeling**
* Used **PostgreSQL for data storage**
* Designed for **real-world scalability**

---

## 👤 Author

**Mohammed Touqeer Ur Raiyan**
Data Engineer | Data Analyst

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
