import requests
from bs4 import BeautifulSoup

url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

lst = soup.select('p')

def clean_item(my_item):
    if 'Navigation' in my_item:
        return ''
    if '© Copyright' in my_item:
        return ''
    position = my_item.find('</')
    return my_item[3:position]

for item in lst:
    print(clean_item(str(item)))
