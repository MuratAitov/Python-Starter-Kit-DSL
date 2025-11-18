"""
Web App Template using Streamlit

This template demonstrates how to build an interactive web application
using Streamlit. Customize it to create dashboards, data tools, or any
interactive web interface.

Run with: streamlit run templates/tool_web_template.py
"""

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings
from src.utils import get_timestamp


def main():
    """Main Streamlit application."""

    # Page configuration
    st.set_page_config(
        page_title=settings.APP_NAME,
        page_icon="🐍",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Title and description
    st.title("🐍 Web Tool Template")
    st.markdown("A starter template for building Streamlit web applications.")

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        user_name = st.text_input("Your Name", value="User")
        theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])

        st.divider()
        st.caption(f"Last updated: {get_timestamp()}")

    # Main content area with tabs
    tab1, tab2, tab3 = st.tabs(["📊 Data", "🔧 Tools", "ℹ️ Info"])

    with tab1:
        st.header("Data Processing")

        st.write(f"Hello, **{user_name}**! 👋")
        st.write("Upload and process your data here.")

        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a CSV file", type=["csv", "xlsx", "txt"]
        )

        if uploaded_file is not None:
            try:
                # Read CSV
                df = pd.read_csv(uploaded_file)

                st.success(f"✅ Loaded {len(df)} rows and {len(df.columns)} columns")

                # Display data
                st.subheader("Preview")
                st.dataframe(df.head(10), use_container_width=True)

                # Statistics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Rows", len(df))
                with col2:
                    st.metric("Total Columns", len(df.columns))
                with col3:
                    st.metric("Memory Usage", f"{df.memory_usage().sum() / 1024:.1f} KB")

                # Show column info
                with st.expander("📋 Column Information"):
                    st.dataframe(
                        pd.DataFrame({
                            "Column": df.columns,
                            "Type": df.dtypes.values,
                            "Non-Null": df.count().values,
                            "Null": df.isnull().sum().values,
                        }),
                        use_container_width=True,
                    )

                # Download processed data
                st.divider()
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Processed CSV",
                    data=csv,
                    file_name="processed_data.csv",
                    mime="text/csv",
                )

            except Exception as e:
                st.error(f"❌ Error loading file: {str(e)}")

        else:
            st.info("👆 Upload a CSV file to get started")

    with tab2:
        st.header("Interactive Tools")

        st.subheader("📊 Sample Chart")
        chart_data = pd.DataFrame({
            'x': range(10),
            'y': [i**2 for i in range(10)],
        })
        st.line_chart(chart_data, x='x', y='y')

        st.divider()

        st.subheader("🔢 Calculator")
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("First Number", value=10.0)
        with col2:
            num2 = st.number_input("Second Number", value=5.0)

        operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

        if st.button("Calculate", type="primary"):
            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"

            st.success(f"Result: **{result}**")

    with tab3:
        st.header("Information")

        st.markdown("""
        ### About This Template

        This is a **Streamlit Web Application Template** that demonstrates:

        - 📁 File uploading and processing
        - 📊 Data visualization
        - 🎨 Interactive widgets
        - 📥 Download functionality
        - 🎯 Multi-tab layout

        ### How to Customize

        1. **Modify this file** to add your own logic
        2. **Add new tabs** for different features
        3. **Import your modules** from `src/`
        4. **Style with Streamlit components**

        ### Useful Streamlit Components

        - `st.button()` - Buttons
        - `st.text_input()` - Text input
        - `st.selectbox()` - Dropdown menus
        - `st.slider()` - Sliders
        - `st.file_uploader()` - File uploads
        - `st.dataframe()` - Data tables
        - `st.chart()` - Charts and plots

        ### Resources

        - [Streamlit Documentation](https://docs.streamlit.io/)
        - [Streamlit Gallery](https://streamlit.io/gallery)
        - [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
        """)

        st.divider()

        # Configuration info
        with st.expander("⚙️ Configuration"):
            st.json({
                "Environment": settings.ENV,
                "Debug": settings.DEBUG,
                "App Name": settings.APP_NAME,
                "Theme": theme,
            })


if __name__ == "__main__":
    main()
