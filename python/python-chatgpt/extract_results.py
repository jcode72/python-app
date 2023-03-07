import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Get the page
url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
r = requests.get(url)

# Parse the page
soup = BeautifulSoup(r.text, 'html.parser')

# Get the headers
headers = soup.find_all('h1')

# Create a translator
translator = Translator()

# Translate
translated_headers = [translator.translate(header.text, dest='es').text for header in headers]

# Create the output file
with open('output.html', 'w') as f:
    for header in translated_headers:
        f.write('<h1>{}</h1>\n'.format(header))
