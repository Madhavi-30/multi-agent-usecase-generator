from research_agent import fetch_company_info
from usecase_agent import generate_use_cases
from resource_collector import collect_datasets
from genai_solution_agent import suggest_genai_tools

def main():
    company = "InstaResz Business Services Pvt. Ltd"
    print("[1] Fetching company/industry information...")
    industry_info = fetch_company_info(company)
    print("\n[2] Generating use cases based on research...")
    use_cases = generate_use_cases(industry_info)
    print("\n[3] Finding relevant datasets for each use case...")
    datasets = collect_datasets(use_cases)
    print("\n[4] Suggesting internal GenAI tools...")
    tools = suggest_genai_tools()

    print("\n--- Industry Research ---")
    for info in industry_info: print("-", info)
    print("\n--- Use Cases ---")
    for uc in use_cases: print("-", uc)
    print("\n--- Datasets ---")
    for k, v in datasets.items(): print(f"- {k}: {v}")
    print("\n--- GenAI Tools ---")
    for t in tools: print("-", t)

if __name__ == "__main__":
    main()
