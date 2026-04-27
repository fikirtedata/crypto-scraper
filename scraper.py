import requests
from bs4 import BeautifulSoup
import pandas as pd  # This is the Data Science giant

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
all_books = soup.find_all('article', class_='product_pod')

# We create an empty list to store our "rows" of data
data_list = []

for book in all_books:
    name = book.h3.a['title']
    raw_price = book.find('p', class_='price_color').text
    clean_price = float(raw_price[2:])
    
    # Store the info in a dictionary (like a mini-record)
    data_list.append({
        "Book Title": name,
        "Price (GBP)": clean_price
    })

# --- The Pandas Magic ---
# Convert the list into a "DataFrame" (basically an Excel table in Python)
df = pd.DataFrame(data_list)

# Save it to a CSV file (No extra code needed!)
df.to_csv("books.csv", index=False)

print("Mission Accomplished! Look at your folder for 'books.csv'")