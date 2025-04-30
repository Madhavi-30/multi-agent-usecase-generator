import requests
from bs4 import BeautifulSoup

def fetch_company_info(company_name):
    # Basic DuckDuckGo search to simulate research
    query = f"{company_name} company overview industry"
    url = f"https://duckduckgo.com/html/?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = [a.text for a in soup.find_all('a') if a.text and 'http' not in a.text][:5]
    return results
