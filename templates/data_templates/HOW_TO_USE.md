# 📊 Data Analysis Templates

Analyze spreadsheets, clean data, create charts, and generate reports.

## What You Can Build

- **Data reports** — Analyze CSV/Excel files
- **Data cleaning tools** — Fix messy data
- **Visualizations** — Create charts and graphs
- **Statistical analysis** — Calculate averages, trends, etc.

---

## Available Templates

### 1. `data_analysis.ipynb` — Complete Data Analysis
A Jupyter notebook with data loading, cleaning, analysis, and visualization.

**Features:**
- Load CSV and Excel files
- Clean missing data
- Calculate statistics
- Create charts
- Export results

**How to use:**

1. **Put your data in the `data/raw/` folder**
   - CSV files (`.csv`)
   - Excel files (`.xlsx`)

2. **Open Jupyter:**
   ```bash
   jupyter notebook
   ```

3. **Navigate to this template:**
   - Go to `templates/data_templates/`
   - Open `data_analysis.ipynb`

4. **Run the cells:**
   - Click on a cell
   - Press Shift+Enter to run it
   - Or click "Run" button

5. **Customize it:**
   - Change the filename to your file
   - Modify the analysis steps
   - Add your own calculations
   - Create different charts

**What's inside:**
- **Section 1:** Load data
- **Section 2:** Explore data (preview, info, stats)
- **Section 3:** Clean data (handle missing values)
- **Section 4:** Analyze data (grouping, calculations)
- **Section 5:** Visualize (charts and graphs)
- **Section 6:** Export results

---

## Example Ideas

### Simple Ideas (Beginners)
- **Grade Calculator** — Calculate class averages
- **Expense Report** — Analyze spending
- **Sales Summary** — Sum up sales data
- **Survey Results** — Count responses
- **Attendance Tracker** — Track attendance

### Medium Ideas
- **Budget Analyzer** — Monthly budget breakdown
- **Product Sales** — Bestsellers and trends
- **Customer Analysis** — Customer demographics
- **Inventory Report** — Stock levels
- **Performance Metrics** — KPI dashboards

### Advanced Ideas
- **Trend Forecasting** — Predict future values
- **Correlation Analysis** — Find relationships
- **Statistical Testing** — Hypothesis tests
- **Data Cleaning Pipeline** — Clean complex data
- **Automated Reports** — Generate PDF reports

---

## Quick Tips

### Load Your Data
```python
import pandas as pd

# Load CSV
df = pd.read_csv('data/raw/your_file.csv')

# Load Excel
df = pd.read_excel('data/raw/your_file.xlsx')

# Preview
df.head()  # First 5 rows
df.tail()  # Last 5 rows
```

### Explore Data
```python
df.info()  # Column types and counts
df.describe()  # Statistics
df.columns  # Column names
len(df)  # Number of rows
```

### Clean Data
```python
# Remove missing values
df = df.dropna()

# Fill missing values
df['column'] = df['column'].fillna(0)

# Remove duplicates
df = df.drop_duplicates()
```

### Analyze Data
```python
# Calculate average
average = df['column'].mean()

# Group and sum
df.groupby('category')['value'].sum()

# Filter rows
df[df['age'] > 18]
```

### Create Charts
```python
import matplotlib.pyplot as plt

# Line chart
df.plot(x='date', y='value', kind='line')

# Bar chart
df.plot(x='category', y='count', kind='bar')

# Show plot
plt.show()
```

### Export Results
```python
# Save to CSV
df.to_csv('data/processed/results.csv', index=False)

# Save to Excel
df.to_excel('data/processed/results.xlsx', index=False)
```

---

## Common Issues

### "File not found"
- Make sure file is in `data/raw/` folder
- Check the filename (case-sensitive!)
- Use the correct path

### "Module not found"
```bash
pip install pandas numpy matplotlib jupyter
```

### "Data looks wrong"
- Check file encoding (try `encoding='utf-8'`)
- Check separator (try `sep=';'` or `sep='\t'`)
- Preview file first with `df.head()`

### Charts don't show
```python
# Add this at the top of notebook
%matplotlib inline

# Or use
import matplotlib.pyplot as plt
plt.show()
```

---

## Useful Pandas Commands

### View Data
```python
df.head(10)  # First 10 rows
df.tail(10)  # Last 10 rows
df.sample(5)  # 5 random rows
df.shape  # Rows and columns
```

### Select Data
```python
df['column_name']  # One column
df[['col1', 'col2']]  # Multiple columns
df[df['age'] > 18]  # Filter rows
df.loc[0:5]  # Rows 0 to 5
```

### Calculate
```python
df['column'].sum()  # Total
df['column'].mean()  # Average
df['column'].median()  # Middle value
df['column'].max()  # Maximum
df['column'].min()  # Minimum
df['column'].count()  # Count values
```

### Group Data
```python
df.groupby('category')['value'].sum()
df.groupby('category')['value'].mean()
df.groupby(['cat1', 'cat2']).size()
```

---

## Learn More

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

---

**Need help?** Ask your instructor or check the main README.md
