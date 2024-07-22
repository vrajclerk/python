import requests
from bs4 import BeautifulSoup
import sqlite3

# URL of the website to scrape
url = 'https://en.wikipedia.org/wiki/Abdul_Qaiyum_Ansari'

# Send a GET request to the URL
response = requests.get(url)

# Parse the content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('historical_personality.db')
c = conn.cursor()

# Create a table to store the data
c.execute('''
    CREATE TABLE IF NOT EXISTS personalities (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        image_url TEXT
    )
''')

# Function to extract and store data
def extract_and_store_data(soup):
    personalities = soup.find_all('div', class_='grid-item')

    for person in personalities:
        name = person.find('h3').text.strip()
        description = person.find('p').text.strip()
        image = person.find('img')['src']

        # Insert data into the database
        c.execute('''
            INSERT INTO personalities (name, description, image_url)
            VALUES (?, ?, ?)
        ''', (name, description, image))

    # Commit the changes
    conn.commit()

# Extract and store data
extract_and_store_data(soup)

# Close the database connection
conn.close()

print("Data has been successfully scraped and stored in the database.")
