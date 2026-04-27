import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
# 1. The Target URL
url = "https://coinmarketcap.com/"
# 2. Add a 'User-Agent' (This is the 'Stealth' skill we talked about)
# This makes the website think you are using a Chrome browser on a Mac
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("Fetching live crypto data...")
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find the table rows (usually <tr> tags)
# Note: Real sites change their code often, so we look for the table
table = soup.find('table', class_='cmc-table')
rows = table.find_all('tr')

crypto_data = []

# 4. Loop through the first 10 rows (skipping the header row)
for row in rows[1:11]:
    cells = row.find_all('td')
    if len(cells) > 1:
        # 1. Name Cleaning: Often the site puts Name + Symbol together (BitcoinBTC)
        # We can try to split it or just take the text
        full_name = cells[2].get_text(separator=" ").split()[0] 
        
        # 2. Price Cleaning: Remove the $ and commas so it's a pure number
        raw_price = cells[3].text
        # We remove '$' and ',' then convert to float
        clean_price = raw_price.replace('$', '').replace(',', '')
        
        crypto_data.append({
            "Name": full_name,
            "Price_USD": float(clean_price)
        })

# 5. Save to CSV
df = pd.DataFrame(crypto_data)
df.to_csv("live_crypto.csv", index=False)

print("Done! Open live_crypto.csv to see the results.")