import requests
from bs4 import BeautifulSoup

class DexScreenerScraper:
    def __init__(self):
        self.base_url = "https://dexscreener.com"

    def scrape_token_data(self, token_address: str) -> dict:
        """Scrape token data from Dexscreener."""
        url = f"{self.base_url}/ethereum/{token_address}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant data (example: price, liquidity, volume)
        price = soup.find("div", {"class": "price"}).text
        liquidity = soup.find("div", {"class": "liquidity"}).text
        volume = soup.find("div", {"class": "volume"}).text

        return {
            "price": price,
            "liquidity": liquidity,
            "volume": volume
        }

class RugCheckScraper:
    def __init__(self):
        self.base_url = "http://rugcheck.xyz/tokens"

    def validate_token(self, token_address: str) -> dict:
        """Validate token using RugCheck."""
        url = f"{self.base_url}/{token_address}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract RugCheck status (example: "Good" or "Bad")
        status = soup.find("div", {"class": "status"}).text

        # Check if supply is bundled
        bundled_supply = "Bundled" in soup.text

        return {
            "status": status,
            "bundled_supply": bundled_supply
        }