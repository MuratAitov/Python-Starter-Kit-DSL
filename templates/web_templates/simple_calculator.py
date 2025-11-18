"""
Simple Calculator Web App

A very basic Streamlit app perfect for beginners.
Shows how to use inputs, buttons, and display results.

Run: streamlit run templates/web_templates/simple_calculator.py
"""

import streamlit as st

# Page setup
st.set_page_config(page_title="Simple Calculator", page_icon="🔢")

# Title
st.title("🔢 Simple Calculator")
st.write("A beginner-friendly calculator app")

st.divider()

# Input section
st.subheader("Enter Numbers")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0, step=0.1)

with col2:
    num2 = st.number_input("Second Number", value=0.0, step=0.1)

# Operation selection
st.subheader("Choose Operation")

operation = st.radio(
    "Pick one:",
    ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide"],
    horizontal=True
)

st.divider()

# Calculate button
if st.button("Calculate", type="primary", use_container_width=True):

    if operation == "➕ Add":
        result = num1 + num2
        st.success(f"✅ Result: {num1} + {num2} = **{result}**")

    elif operation == "➖ Subtract":
        result = num1 - num2
        st.success(f"✅ Result: {num1} - {num2} = **{result}**")

    elif operation == "✖️ Multiply":
        result = num1 * num2
        st.success(f"✅ Result: {num1} × {num2} = **{result}**")

    elif operation == "➗ Divide":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
        else:
            result = num1 / num2
            st.success(f"✅ Result: {num1} ÷ {num2} = **{result}**")

st.divider()

# Tips section
with st.expander("💡 How This Works"):
    st.markdown("""
    This simple app shows you:

    - `st.number_input()` - Get numbers from user
    - `st.radio()` - Let user pick one option
    - `st.button()` - Create clickable buttons
    - `st.success()` - Show green success message
    - `st.error()` - Show red error message

    **Try customizing it:**
    - Add more operations (square root, power, etc.)
    - Change the colors and layout
    - Add a history of calculations
    - Save results to a file
    """)

# Footer
st.caption("Built with Streamlit • Python Starter Kit")
