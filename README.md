
📘 Amazon Bestseller Books Web Scraper

This project scrapes the Amazon Bestseller Books page and extracts data like Title, Author, Rating, and Price, and stores it into a CSV file using Python.


---

✨ Features :

✅ Scrapes:

📖 Book Title

✍ Author

⭐ Rating

💰 price



✅ Stores :

Extracted data is saved in a CSV file (amazon_products.csv)


✅ User-Friendly :

Adds polite delay between requests (time.sleep(3))

Handles missing data gracefully

Displays total books found per page


🧰 Tools & Libraries Used :

requests – for sending HTTP requests

BeautifulSoup – for parsing HTML content

pandas – to create and save data in CSV

time, warnings, re – for delays, error handling, and cleanup



---

📁 Files Included :

File Name	Description

web-scrap-main.py	Main scraping Python script
amazon_products.csv	Output file containing scraped data
README.md	Project documentation (this file)


⚙ How It Works :

1. Sends a request to Amazon’s Bestseller Books page


2. Parses the HTML content using BeautifulSoup


3. Extracts title, author, rating, and price for each book


4. Loops through multiple pages (default: 2 pages)


5. Saves all results to amazon_products.csv


6. Displays the first 18 rows as a sample preview



📌 Learning Outcome :

Through this project, I strengthened my understanding of:

Web scraping fundamentals

HTML element parsing

Working with real-time online data

Data cleaning and storage using Pandas
