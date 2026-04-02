# Advanced Exploratory Data Analysis (EDA) Suite

## Overview
The **EDA Suite** is a Python library designed to automate the exploratory data analysis process. It provides a structured and reusable framework for quickly generating insights, statistics, and visualizations from new datasets. This project is aimed at data scientists and analysts to reduce manual data exploration time.

---

## Features
- Detects and reports missing values.
- Computes summary statistics for all numeric columns.
- Generates correlation matrix and correlation heatmaps.
- Creates histograms for numeric variables.
- Automatically saves plots for reporting and documentation purposes.
- Fully modular and ready to integrate into pipelines or notebooks.

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/mohammedjeelan112/Advanced-Exploratory-Data-Analysis-EDA-Suite.git
cd eda_suite
````

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

1. **Import the EDA Suite class**

```python
from src.eda import EDASuite
import pandas as pd

# Load dataset
df = pd.read_csv("data/sample.csv")

# Initialize EDA Suite
eda = EDASuite(df)
```

2. **Get basic information**

```python
print(eda.summary_stats())
print(eda.missing_values())
```

3. **Generate correlation matrix and heatmap**

```python
print(eda.correlations())
eda.plot_correlation_heatmap()
```

4. **Generate histograms for numeric columns**

```python
eda.plot_histograms()
```

All plots are saved automatically in the `plots/` directory.

---

## Project Structure

```
eda_suite/
│
├── src/
│   ├── __init__.py
│   └── eda.py          # Core EDA class
│
├── notebooks/
│   └── testing.ipynb   # Example notebook to test functionality
│
├── data/
│   └── sample.csv      # Example dataset
│
├── plots/              # Generated plots saved here
├── requirements.txt
└── README.md
```

---

## Requirements

```
pandas==2.2.3
matplotlib==3.8.2
seaborn==0.12.2
numpy==1.26.5
```

---

## Future Improvements

* Add automatic detection and visualization of categorical variables.
* Generate pairplots for numeric columns.
* Export summary statistics to CSV/Excel for reporting.
* Integrate with Jupyter Notebook widgets for interactive analysis.

---

## License

MIT License
