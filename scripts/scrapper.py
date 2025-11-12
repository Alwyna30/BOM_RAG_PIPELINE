import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

os.makedirs("data/raw", exist_ok=True)

urls = {
    "home_loan": "https://bankofmaharashtra.bank.in/personal-banking/loans/home-loan",
    "retail_loan":"https://bankofmaharashtra.bank.in/retail-loans",
    "education_loan":"https://bankofmaharashtra.bank.in/educational-loans",
    "car_loan":"https://bankofmaharashtra.bank.in/personal-banking/loans/car-loan",
    "maha_super_flexi_housing_loans":"https://bankofmaharashtra.bank.in/maha-super-flexi-housing-loan-scheme",
    "personal_loan":"https://bankofmaharashtra.bank.in/personal-banking/loans/personal-loan",
    "loan_against_property":"https://bankofmaharashtra.bank.in/loan-against-property",
}

data = []

for loan_type, url in urls.items():
    print(f"\nScraping {loan_type} page...")

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        time.sleep(2)  # Polite delay to avoid blocking

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")

            # Try to locate the main text area
            main_content = soup.find("div", class_="col-md-9") or soup.body

            # Extract visible text and clean it
            text = main_content.get_text(separator=" ", strip=True)

            data.append({
                "loan_type": loan_type,
                "url": url,
                "content": text
            })
            print(f"{loan_type} scraped successfully.")

        else:
            print(f"Failed to fetch {url} (Status Code: {response.status_code})")

    except Exception as e:
        print(f"Error scraping {loan_type}: {e}")

# Step 4: Save results to CSV
if data:
    df = pd.DataFrame(data)
    output_path = "data/raw/bom_loan_data.csv"
    df.to_csv(output_path, index=False)
    print(f"\nScraped data saved to: {output_path}")
else:
    print("No data scraped. Please check the URLs or HTML structure.")