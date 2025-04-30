import streamlit as st
from research_agent import fetch_company_info
from usecase_agent import generate_use_cases
from resource_collector import collect_datasets
from genai_solution_agent import suggest_genai_tools

st.set_page_config(page_title="AI Use Case Generator", layout="centered")
st.title("🤖 Multi-Agent AI Use Case Generator")

company = st.text_input("Enter Company Name", "InstaResz Business Services Pvt. Ltd")

if st.button("🔍 Run Agents"):
    with st.spinner("Fetching company/industry information..."):
        industry_info = fetch_company_info(company)
        st.success("Industry research complete.")
        st.subheader("🔎 Industry Research")
        for info in industry_info:
            st.write("-", info)

    with st.spinner("Generating use cases..."):
        use_cases = generate_use_cases(industry_info)
        st.success("Use case generation complete.")
        st.subheader("💡 AI/ML/GenAI Use Cases")
        for uc in use_cases:
            st.write("•", uc)

    with st.spinner("Collecting datasets..."):
        datasets = collect_datasets(use_cases)
        st.success("Dataset collection complete.")
        st.subheader("📊 Datasets")
        for k, v in datasets.items():
            st.markdown(f"**{k}**: [Link]({v})")

    with st.spinner("Suggesting GenAI tools..."):
        tools = suggest_genai_tools()
        st.success("Tool suggestions complete.")
        st.subheader("🛠️ Suggested GenAI Tools")
        for tool in tools:
            st.write("•", tool)
