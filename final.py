import streamlit as st
import streamlit.components.v1 as components

# Set up page configuration
st.set_page_config(page_title="Power BI Reports", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Select Power BI Report")
task = st.sidebar.radio("Choose a report:", [
    "Task 1", "Task 2", "Task 3", "Task 4", "Task 5","Task 6","Task 7"
])

# Power BI Report URLs (Replace with actual embed links)
report_urls = {
    "Task 1": "https://app.powerbi.com/reportEmbed?reportId=00438ae7-d1ae-4c72-957a-211bb9ebdc08&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3",
    "Task 2": "https://app.powerbi.com/reportEmbed?reportId=6d40669b-a606-49ba-8e1e-b712cca5988d&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3",
    "Task 3": "https://app.powerbi.com/reportEmbed?reportId=e9827fd6-1545-40b3-9388-d5dce6156d15&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3",
    "Task 4": "https://app.powerbi.com/reportEmbed?reportId=e9827fd6-1545-40b3-9388-d5dce6156d15&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3",
    "Task 5": "https://app.powerbi.com/reportEmbed?reportId=7a62d334-e645-434e-9f37-ae6e4139fbfd&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3",
    "Task 6": "https://app.powerbi.com/reportEmbed?reportId=ef1268cf-67e8-42f1-8510-76e0796035d1&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3",
    "Task 7": "https://app.powerbi.com/reportEmbed?reportId=9b5ea70b-1b6c-4a55-89ad-24bf7f68fa1e&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3"
}

# Display Selected Power BI Report
st.title(f"📊 Power BI Report - {task}")
st.write("Below is the embedded Power BI report:")

components.html(
    f"""
    <iframe title="Power BI Report"
    width="100%" height="650px"
    src="{report_urls[task]}"
    frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=700,
)
