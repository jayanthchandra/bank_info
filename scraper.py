import requests
import wget
import os

from bs4 import BeautifulSoup, SoupStrainer

url = 'https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009'

file_types = ['.xls', '.xlsx', '.csv']

for file_type in file_types:

    response = requests.get(url)

    for link in BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if file_type in link['href']:
                full_path = url + link['href']
                down=link['href'][:4]+'s'+link['href'][4:]
                wget.download(down)