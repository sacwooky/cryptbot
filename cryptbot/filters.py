from datetime import datetime, timedelta

class TokenFilters:
    def __init__(self, config: dict):
        self.min_liquidity = config["filters"]["min_liquidity"]
        self.min_age_days = config["filters"]["min_age_days"]
        self.max_market_cap = config["filters"]["max_market_cap"]
        self.volume_threshold = config["filters"]["volume_threshold"]

    def apply_filters(self, token_data: dict) -> bool:
        """Apply filters to token data."""
        # Liquidity filter
        if token_data["liquidity"] < self.min_liquidity:
            return False

        # Age filter
        min_age = datetime.utcnow() - timedelta(days=self.min_age_days)
        if token_data["created_at"] > min_age:
            return False

        # Market cap filter
        if token_data["market_cap"] > self.max_market_cap:
            return False

        # Volume filter
        if token_data["volume_24h"] < self.volume_threshold:
            return False

        return True