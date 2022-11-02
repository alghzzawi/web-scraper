import requests
from bs4 import BeautifulSoup
import json

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def get_citations_needed_count(soup):
    """
    this function take the soup of page content 
    and count the Citation needed in a wikipedia page
    """
    citations= soup.find_all('a',title="Wikipedia:Citation needed")
    print(f'the number of citations needed is {len(citations)}')


def get_citations_needed_report(soup):
    """
    this function print all the paragraph thet have Citation needed
    """

    citations= soup.find_all('a',title="Wikipedia:Citation needed")
    all_citations=[]
    for citation in citations:
        cita = citation.find_parents('p')[0].text.strip()

        print(cita , '\n--------------------')



get_citations_needed_count(soup)
get_citations_needed_report(soup)
