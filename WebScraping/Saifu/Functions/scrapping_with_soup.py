from bs4 import BeautifulSoup
import requests
import os
import sys


def usingBeautifulSoup():
    url = 'https://www.monster.com/jobs/search/?q=Senior-Software-Developer&where=New-york'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    # element by id ResultsContainer
    results = soup.find(id='ResultsContainer')
    # Find Elements by HTML Class Name
    job_elements = results.find_all('section', class_='card-content')
    print(len(job_elements))
    for job_element in job_elements:
        company_element = job_element.find('div', class_='company')
        if company_element is not None:
            print(company_element.text)
