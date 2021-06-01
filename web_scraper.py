import requests
from bs4 import BeautifulSoup

def get_citation_needed_count(URL):
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    
    return len(citation)

def get_citations_needed_report(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    
    result = ''
    
    for i  in citation:
        result += f'{i.parent.text}\n'
    return result

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
print(get_citations_needed_report(URL))