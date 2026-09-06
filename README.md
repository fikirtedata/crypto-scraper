# Cryptocurrency Market Web Scraper

A Python web scraping utility built with **BeautifulSoup** and **Requests** to extract real-time cryptocurrency metrics, clean financial data, and export structured datasets for analysis.

---

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: BeautifulSoup4, Requests, Pandas
- **Environment**: Google Colab / Jupyter Notebook

---

## 🔑 Key Features
- **Live Data Scraping**: Sends HTTP requests to fetch live market listings for top cryptocurrencies.
- **Data Extraction**: Extracts asset names, current trading prices, and 24-hour volume changes.
- **CSV Export**: Cleanly parses raw HTML into a structured Pandas DataFrame and exports it to a `.csv` file.

---

## 🚀 How to Run
1. Clone or download this repository.
2. Ensure `pandas`, `requests`, and `beautifulsoup4` are installed:
   ```bash
   pip install pandas requests beautifulsoup4
