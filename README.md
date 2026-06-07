# Bike-Sharing Usage Pattern Analysis

In-depth analysis of bike-sharing usage patterns based on **season**, **workday vs. holiday**, and **time of day**. Includes exploratory data analysis (EDA), advanced trend analysis, and an interactive Streamlit dashboard.

## Key Insights

1. **Season & Workday Patterns** — ridership peaks in spring and summer; weekdays consistently outperform weekends
2. **Time-of-Day Peaks** — usage spikes at 8 AM and 5 PM, aligning with commuting hours; drops significantly at night

## Features

- **Exploratory Data Analysis (EDA)** — distribution, correlation, and outlier analysis across variables like temperature and weather
- **Usage Pattern Visualization** — breakdown by season, workday/holiday, and hour of day
- **Advanced Analysis** — temperature impact, seasonal trends, and weather condition effects
- **Interactive Dashboard** — filter by season and workday to drill into specific patterns

## Project Structure

```
├── notebook.ipynb          # Full analysis: data wrangling, EDA, visualizations
├── dashboard/
│   └── dashboard.py        # Streamlit interactive dashboard
├── data/
│   ├── day.csv             # Daily bike-sharing data
│   └── hour.csv            # Hourly bike-sharing data
├── requirements.txt        # Python dependencies
└── url.txt                 # Deployed Streamlit app link
```

## Getting Started

```bash
pip install -r requirements.txt
```

### Run Jupyter Notebook

```bash
jupyter notebook notebook.ipynb
```

### Run Streamlit Dashboard

```bash
streamlit run dashboard/dashboard.py
```

## Tech Stack

- Python 3.x · Pandas · NumPy
- Matplotlib · Seaborn
- Streamlit
