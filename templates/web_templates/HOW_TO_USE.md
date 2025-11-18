# 🌐 Web App Templates

Build interactive web applications that run in your browser.

## What You Can Build

- **Dashboards** — Display data with charts and graphs
- **Data tools** — Upload, process, and download files
- **Forms** — Collect user input
- **Interactive apps** — Games, calculators, visualizations

---

## Available Templates

### 1. `dashboard.py` — Interactive Dashboard
A complete Streamlit web app with file upload, data display, and tools.

**Features:**
- Upload CSV/Excel files
- Preview data in tables
- Show statistics and info
- Download processed data
- Interactive calculator
- Multiple tabs

**How to use:**

1. **Run the app:**
   ```bash
   streamlit run templates/web_templates/dashboard.py
   ```

2. **Open in browser:**
   - Automatically opens at http://localhost:8501
   - Or manually go to that address

3. **Try it out:**
   - Upload a CSV file
   - Explore the different tabs
   - Use the calculator
   - Check the info section

**Customize it:**
- Change the title and description
- Add new tabs for features
- Modify the calculator or add new tools
- Add charts and visualizations

---

### 2. `simple_form.py` — Simple Form (Example Below)
A minimal web form that collects user input.

---

## Example Ideas

### Simple Ideas (Beginners)
- **Unit Converter** — Convert meters to feet, kg to lbs, etc.
- **BMI Calculator** — Calculate body mass index
- **Tip Calculator** — Calculate restaurant tips
- **Text Counter** — Count words, characters
- **Random Generator** — Generate passwords, numbers

### Medium Ideas
- **Expense Tracker** — Track spending
- **Grade Calculator** — Calculate GPA
- **Shopping List** — Manage shopping items
- **Recipe Book** — Store and display recipes
- **Task Manager** — Simple to-do list

### Advanced Ideas
- **Stock Dashboard** — Show stock prices and charts
- **Weather App** — Display weather forecasts
- **Chat Interface** — Chat with AI
- **Data Analyzer** — Complete data analysis tool
- **Image Editor** — Basic image processing

---

## Quick Tips

### Basic Structure
```python
import streamlit as st

st.title("My App")
st.write("Hello, world!")

name = st.text_input("Your name")
if st.button("Submit"):
    st.success(f"Hello, {name}!")
```

### Common Components

**Text and Headers:**
```python
st.title("Big Title")
st.header("Section Header")
st.write("Normal text")
st.markdown("**Bold** and *italic*")
```

**User Input:**
```python
text = st.text_input("Enter text")
number = st.number_input("Enter number", min_value=0)
choice = st.selectbox("Pick one", ["A", "B", "C"])
agree = st.checkbox("I agree")
```

**Display Data:**
```python
st.dataframe(df)  # Show DataFrame
st.table(df)  # Show static table
st.json(data)  # Show JSON
```

**Charts:**
```python
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)
```

**Layout:**
```python
# Columns
col1, col2 = st.columns(2)
with col1:
    st.write("Left side")
with col2:
    st.write("Right side")

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("First tab content")
```

### Upload Files
```python
file = st.file_uploader("Upload CSV", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
```

### Download Files
```python
csv = df.to_csv(index=False)
st.download_button("Download", csv, "data.csv", "text/csv")
```

---

## Common Issues

### "Port already in use"
```bash
# Use a different port
streamlit run templates/web_templates/dashboard.py --server.port 8502
```

### "Module not found"
```bash
# Install streamlit
pip install streamlit
```

### App doesn't update
- Save your file (Ctrl+S or Cmd+S)
- Click "Rerun" in the browser
- Or enable "Always rerun" in settings

---

## Learn More

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery) — See examples
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Component Gallery](https://streamlit.io/components)

---

**Need help?** Ask your instructor or check the main README.md
