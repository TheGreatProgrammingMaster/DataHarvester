import requests
from bs4 import BeautifulSoup
# User input for what to search for
search_query = input("Enter what you want to search for: ")
# Make a request to a search engine
url = "https://www.google.com/search?q=" + search_query
response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract data based on HTML tags
    for item in soup.find_all('a'):
        print(item.get_text())
else:
    print("Failed to fetch the webpage")
