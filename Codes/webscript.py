import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):

    response = requests.get(url)  #request Send to Website

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information from the HTML (modify as needed)
        data = {
            'title': soup.title.string,
            'paragraphs': [p.text for p in soup.find_all('p')],
            'links': [link.get('href') for link in soup.find_all('a')],
            # Add more data as needed
        }

        return data
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    # Specify the URL of the website you want to scrape
    target_url = 'https://developer.android.com/'

    # Call the function to scrape the website
    scraped_data = scrape_website(target_url)

    # Check if data was successfully scraped
    if scraped_data:
        # Write the data to a JSON file
        with open('output.json', 'w', encoding='utf-8') as json_file:
            json.dump(scraped_data, json_file, ensure_ascii=False, indent=2)
        print('Data successfully scraped and stored in output.json.')