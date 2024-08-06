import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Define the URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_Indian_people'  # Replace with the actual URL

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

# Initialize an empty list to collect data
data = []

# Parse the HTML to find the relevant sections
for item in soup.find_all('li'):
    name_tag = item.find('a')
    if name_tag:
        name = name_tag.text.strip()
        img_tag = item.find('a')
        img_url = 'https:' + img_tag['href'] if img_tag else 'No Image'
        description = item.find_next_sibling('p').text.strip() if item.find_next_sibling('p') else 'No Description'
        
        # Download the image
        img_path = download_image(img_url) if img_url != 'No Image' else 'No Image'
        
        data.append({'Name': name, 'Image Path': img_path, 'Description': description})

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('indian_personalities.csv', index=False)
