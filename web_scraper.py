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
    # print(citation)
    citation_list = []
    counter = 0
    
    for i  in citation:
        if counter == 0:
            citation_list.append(i.parent.text)
            counter = 1
        else:
            if i.parent.text in citation_list:
                continue
            else:
                citation_list.append(i.parent.text)
                counter = counter + 1
        # print(citation_list[counter-1])
        
    return(citation_list[counter-1])

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
get_citations_needed_report(URL)