import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Power BI Report", layout="wide")

st.title("📊 Power BI Report Task 5")

# Embed Power BI Report
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=7a62d334-e645-434e-9f37-ae6e4139fbfd&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3" # Replace with your public embed URL

components.html(
    f"""
    <iframe title="Power BI Report"
    width="100%" height="650px"
    src="{power_bi_url}"
    frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=700,
)
