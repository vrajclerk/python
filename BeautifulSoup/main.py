import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/The_Greatest_Indian'

# Send a GET request to the URL
response = requests.get(url)

# Parse the content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Function to extract the main content of the page
def extract_content(soup):
    # Find the main content div
    content_div = soup.find('div', {'class': 'mw-parser-output'})
    
    # Extract headings and paragraphs
    data = {}
    heading = None  # Initialize heading to None
    for element in content_div.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'ol']):
        if element.name.startswith('h'):
            heading = element.text.strip()
            data[heading] = []
        elif element.name == 'p':
            paragraph = element.text.strip()
            if heading:
                data[heading].append(paragraph)
        elif element.name in ['ul', 'ol']:
            list_items = [li.text.strip() for li in element.find_all('li')]
            if heading:
                data[heading].extend(list_items)
    
    return data

# Extract content from the page
content = extract_content(soup)

# Print the extracted content
for heading, texts in content.items():
    print(f'{heading}:')
    for text in texts:
        print(f'  {text}')
    print('\n')
