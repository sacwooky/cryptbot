from scraper import RugCheckScraper

class RugCheckValidator:
    def __init__(self):
        self.scraper = RugCheckScraper()

    def validate_token(self, token_address: str) -> dict:
        """Validate token using RugCheck."""
        return self.scraper.validate_token(token_address)