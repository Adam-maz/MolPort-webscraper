import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


filepath = input("Put filepath (without quotation marks) for .csv file: ")
data = pd.read_csv(filepath)
df = pd.DataFrame(data)
urls = df["Link"].to_list()


class MolportScraping:
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.results = []

    def scrape_url(self, url):
        try:
            self.driver.get(url)
            smiles_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.col-6.col-lg-9.text-break") ###Make sure with the use of the DevTools, that this string
                )                                                      ###matches criteria of Your search
            )
            smiles = smiles_element.text
            molport_id = url.split("/")[-1].split("?")[0]
            self.results.append({"Id": molport_id, "SMILES": smiles})

        except Exception as e:
            print(f"Error scraping URL {url}: {e}")
            self.results.append({"Id": url, "SMILES": None})

    def scrape_all(self, urls):
        for idx, url in enumerate(urls, 1):
            print(f"{idx}) Scraping: {url}")
            self.scrape_url(url)

    def save_results(self, output_filepath):
        results_df = pd.DataFrame(self.results)
        results_df.to_csv(output_filepath, index=False)
        print(f"Results saved to {output_filepath}")

    def quit(self):
        self.driver.quit()


def main():
    scraper = MolportScraping()
    scraper.scrape_all(urls)
    output_filepath = os.path.join(
        os.path.dirname(filepath), "scraping_results.csv"
    )
    scraper.save_results(output_filepath)
    scraper.quit()


if __name__ == "__main__":
    main()
