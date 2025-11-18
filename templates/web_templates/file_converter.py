"""
File Converter Web App

Convert between CSV and Excel files in your browser.
Perfect example of file upload/download functionality.

Run: streamlit run templates/web_templates/file_converter.py
"""

import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="File Converter", page_icon="🔄")

st.title("🔄 CSV ↔️ Excel Converter")
st.write("Upload a file and convert it to another format")

st.divider()

# File uploader
uploaded_file = st.file_uploader(
    "Upload your file",
    type=["csv", "xlsx", "xls"],
    help="Upload a CSV or Excel file to convert"
)

if uploaded_file:
    # Get file extension
    file_ext = uploaded_file.name.split(".")[-1].lower()

    try:
        # Read the file
        if file_ext == "csv":
            df = pd.read_csv(uploaded_file)
            input_type = "CSV"
            output_type = "Excel"
        else:  # xlsx or xls
            df = pd.read_excel(uploaded_file)
            input_type = "Excel"
            output_type = "CSV"

        # Show success
        st.success(f"✅ Loaded {input_type} file: **{uploaded_file.name}**")

        # Show preview
        st.subheader("Preview")
        st.dataframe(df.head(10), use_container_width=True)

        # Show stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Rows", len(df))
        with col2:
            st.metric("Columns", len(df.columns))
        with col3:
            memory_kb = df.memory_usage(deep=True).sum() / 1024
            st.metric("Size", f"{memory_kb:.1f} KB")

        st.divider()

        # Convert button
        st.subheader(f"Convert to {output_type}")

        if output_type == "Excel":
            # Convert CSV to Excel
            if st.button(f"Convert to Excel", type="primary", use_container_width=True):
                # Create Excel file in memory
                output = BytesIO()
                df.to_excel(output, index=False, engine='openpyxl')
                output.seek(0)

                # Download button
                st.download_button(
                    label="📥 Download Excel File",
                    data=output,
                    file_name=uploaded_file.name.replace('.csv', '.xlsx'),
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    use_container_width=True
                )
                st.success("✅ Converted! Click download button above.")

        else:  # Convert to CSV
            if st.button(f"Convert to CSV", type="primary", use_container_width=True):
                # Convert to CSV
                csv = df.to_csv(index=False).encode('utf-8')

                # Download button
                st.download_button(
                    label="📥 Download CSV File",
                    data=csv,
                    file_name=uploaded_file.name.rsplit('.', 1)[0] + '.csv',
                    mime='text/csv',
                    use_container_width=True
                )
                st.success("✅ Converted! Click download button above.")

    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")
        st.info("Make sure your file is a valid CSV or Excel file")

else:
    st.info("👆 Upload a CSV or Excel file to get started")

st.divider()

# Tips
with st.expander("💡 How This Works"):
    st.markdown("""
    This app demonstrates:

    - **File Upload:** `st.file_uploader()`
    - **Reading Data:** `pd.read_csv()` and `pd.read_excel()`
    - **Converting:** Save with different format
    - **File Download:** `st.download_button()`

    **Try these improvements:**
    - Add more file formats (JSON, XML)
    - Let users filter/edit data before converting
    - Add data validation
    - Show more detailed statistics
    """)

st.caption("Built with Streamlit & Pandas • Python Starter Kit")
