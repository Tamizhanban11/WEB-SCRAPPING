import requests
from bs4 import BeautifulSoup
import openpyxl

class Product:
    def __init__(self, code, title):
        self.code = code
        self.title = title

def scrape_houseware():
    category_id = "glassware"
    url = f"https://modernhouseware.com/product-category/{category_id}/"

    # Send HTTP GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    products = []
    count = 1

    # Find product elements
    ul_elements = soup.select(".products")

    for ul in ul_elements:
        li_elements = ul.select("li")

        for product in li_elements:
            title = product.select_one(".woocommerce-loop-product__title")
            code = product.select_one(".prod_number")

            title_text = title.text.strip() if title else "No Title"
            code_text = code.text.strip() if code else "No Code"

            print(f"{count}. Code: {code_text} Product Name: {title_text}")
            products.append(Product(code_text, title_text))
            count += 1

    # Save data to Excel
    save_to_excel(products)

def save_to_excel(products):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Houseware Products"
    
    # Adding headers
    sheet.append(["Code", "Product Name"])

    # Adding product data
    for product in products:
        sheet.append([product.code, product.title])

    # Save the Excel file
    file_name = "houseware_products.xlsx"
    workbook.save(file_name)
    print(f"Data saved to {file_name}")

# Run the scraper
scrape_houseware()
