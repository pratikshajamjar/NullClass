import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Power BI Report", layout="wide")

st.title("📊 Power BI Report Task 3")

# Embed Power BI Report
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=e9827fd6-1545-40b3-9388-d5dce6156d15&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3"  # Replace with your public embed URL

components.html(
    f"""
    <iframe title="Power BI Report"
    width="100%" height="650px"
    src="{power_bi_url}"
    frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=700,
)
