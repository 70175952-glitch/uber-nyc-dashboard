# 🚖 Uber NYC Pickups — EDA Dashboard

**Course:** Exploratory Data Analysis
**Instructor:** Ali Hassan Sherazi
**Dataset:** Kaggle – Uber Pickups NYC (600K+ records, Apr–Sep 2014)

---

## 📁 Project Structure

```
dashboard_project/
├── data/
│   └── uber-raw-data-apr14.csv     ← Dataset (DO NOT rename)
├── notebooks/
│   └── analysis.ipynb              ← Exploratory Data Analysis
├── app.py                          ← Main Streamlit dashboard
├── charts.py                       ← All 10 chart functions
├── filters.py                      ← Data loading & filter logic
├── requirements.txt                ← Python dependencies
└── README.md                       ← This file
```

---

## ⚙️ Installation & Setup

### Step 1 — Clone / Extract the project
```bash
unzip dashboard_project.zip
cd dashboard_project
```

### Step 2 — Create a virtual environment (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Download the dataset
1. Go to [Kaggle – Uber Pickups NYC](https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city)
2. Download `uber-raw-data-apr14.csv`
3. Place it inside the `data/` folder — **do NOT rename it**

### Step 5 — Run the dashboard
```bash
streamlit run app.py
```

The dashboard opens automatically at `http://localhost:8501`

---

## 📊 Charts Included

| # | Chart Type   | Description                                      |
|---|--------------|--------------------------------------------------|
| 1 | Pie Chart    | Proportional share of trips per dispatch base    |
| 2 | Histogram    | Frequency distribution of pickups by hour        |
| 3 | Line Chart   | Hourly pickup trend across 24 hours              |
| 4 | Bar Chart    | Pickups comparison by day of week                |
| 5 | Scatter Plot | Geospatial lat/lon of NYC pickups (colour=hour)  |
| 6 | Box Plot     | Hour-of-day spread & outliers per base           |
| 7 | Heatmap      | Correlation matrix of numeric features           |
| 8 | Area Chart   | Cumulative pickups over time                     |
| 9 | Count Plot   | Trip count frequency per dispatch base           |
|10 | Violin Plot  | Hour density distribution per base               |

---

## 🔽 Sidebar Filters

All filters are **linked to every chart** — charts update simultaneously.

| Filter                 | Type                  | Column          |
|------------------------|-----------------------|-----------------|
| 🔍 Search              | Text input            | Base            |
| 📅 Date Range          | Date picker           | Date/Time       |
| 🏢 Dispatch Base       | Multi-select          | Base            |
| 🕐 Hour of Day         | Range slider (0–23)   | Hour            |
| 📆 Day of Week         | Multi-select          | DayOfWeek       |
| ↺ Reset All Filters   | Button                | All columns     |

---

## 💡 Key Insights

- **Peak hours** are between 17:00–19:00 (evening rush) and around 02:00 (nightlife)
- **Friday & Saturday** have the highest pickup volumes
- **Manhattan** concentrates the majority of all pickups (lat 40.72–40.78)
- **Base B02617** accounts for the largest share of dispatches
- **Hour** shows the strongest correlation with trip activity patterns

---

## 🛠 Tech Stack

| Tool        | Role                          |
|-------------|-------------------------------|
| Python 3.x  | Core language                 |
| Pandas      | Data loading, cleaning, EDA   |
| NumPy       | Numerical operations          |
| Matplotlib  | Core chart rendering          |
| Seaborn     | Statistical visualizations    |
| Streamlit   | Interactive dashboard frontend|

---

## 📌 Important Notes

- Do **NOT** rename the dataset file
- All 10 chart types from the project brief are implemented
- Dashboard is fully responsive with sidebar filter panel
- Code is modular: `charts.py` and `filters.py` are separate modules
