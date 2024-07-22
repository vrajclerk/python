import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Define the URL of the Wikipedia page
url = 'https://en.m.wikipedia.org/wiki/Category:Indian_independence_activists'  # Replace with the actual URL

# Function to download image
def download_image(img_url, folder='images'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    img_response = requests.get(img_url)
    img_name = img_url.split("/")[-1]
    img_path = os.path.join(folder, img_name)
    with open(img_path, 'wb') as file:
        file.write(img_response.content)
    return img_path

# Send a request to fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the relevant sections
data = []
for item in soup.find_all('div', class_='mw-parser-output'):
    name = item.find('a', class_='mw-redirect')
    if name:
        name = name.text.strip()
        img_tag = item.find('img')
        img_url = 'https:' + img_tag['src'] if img_tag else 'No Image'
        description = item.find('p').text.strip() if item.find('p') else 'No Description'
        
        # Download the image
        img_path = download_image(img_url) if img_url != 'No Image' else 'No Image'
        
        data.append({'Name': name, 'Image Path': img_path, 'Description': description})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('indian_personalities.csv', index=False)
