import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Power BI Report", layout="wide")

st.title("📊 Power BI Report Task 7")

# Embed Power BI Report
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=9b5ea70b-1b6c-4a55-89ad-24bf7f68fa1e&autoAuth=true&ctid=0ed51ad7-52cc-4234-b54a-76b82d40b5c3" # Replace with your public embed URL

components.html(
    f"""
    <iframe title="Power BI Report"
    width="100%" height="650px"
    src="{power_bi_url}"
    frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=700,
)
