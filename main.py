import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re
import warnings
warnings.filterwarnings('ignore')

print('Setup Complete!')

no_pages = 2  # Number of Amazon Bestseller pages to scrape

def get_data(pageNo):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "close",
    }

    url = f'https://www.amazon.com/gp/bestsellers/books/ref=zg_bs_pg_{pageNo}?ie=UTF8&pg={pageNo}'
    response = requests.get(url, headers=headers)
    # print(response.content)


    if response.status_code != 200:
        print(f"Failed to retrieve page {pageNo}. Status Code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)

    # Save page HTML for manual inspectionx
    # with open(f"page_{pageNo}.html", "w", encoding="utf-8") as f:
    #     f.write(soup.prettify())

    # Identify book cards
    book_blocks = soup.find_all('div', attrs={'class': 'zg-grid-general-faceout'})
    # print(book_blocks)

    # print(f"Found {len(book_blocks)} book items on page {pageNo}")

    alls = []
    for d in book_blocks:
        all1 = []
        # print (all1)5

        # Book Title
        name_img = d.find('img', alt=True)
        # print(name_img)
        if name_img:
            all1.append(name_img['alt'])
        else:
            all1.append("Unknown Title")

        # Author
        author = d.find('a', attrs={'class':'a-size-small a-link-child'})
        # print(author.text)
        all1.append(author.text.strip())


        # Rating]
        rating = d.find('span', attrs={'class':'a-icon-alt'})
        print(rating.text)
     
        all1.append(rating.text.strip() if rating else "No Rating")



        # Price
        price = d.find('span', attrs={'class':'p13n-sc-price'})
        all1.append(price.text.strip() if price else "Not Available")

        alls.append(all1)

    return alls

# Main Execution
results = []
for i in range(1, no_pages + 1):
    page_data = get_data(i)
    results.extend(page_data)
    time.sleep(3)  # Be polite to Amazon servers

# Create DataFrame
df = pd.DataFrame(results, columns=['Book Name', 'Author', 'Rating', 'Price'])

# Save to CSV
df.to_csv('amazon_products.csv', index=False, encoding='utf-8')
print("Data saved to 'amazon_products.csv'")

df = pd.read_csv("amazon_products.csv")
print(df.head(18))

