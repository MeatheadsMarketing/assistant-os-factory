import streamlit as st

def run_ui():
    st.title("Remove Duplicate Rows from CSV Dataset")
    st.write("This utility assists in removing duplicate rows from a CSV dataset. It operates based on one or more selected columns, providing the flexibility to define what constitutes a duplicate. Users have the option to keep either the first or the last occurrence of the duplicate rows, based on their specific requirements.")
    # Add UI logic here

if __name__ == '__main__':
    run_ui()
