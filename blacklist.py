class BlacklistManager:
    def __init__(self, config: dict):
        self.coin_blacklist = config["blacklists"]["coin_blacklist"]
        self.dev_blacklist = config["blacklists"]["dev_blacklist"]

    def is_blacklisted(self, token_data: dict) -> bool:
        """Check if token or developer is blacklisted."""
        if token_data["token_address"] in self.coin_blacklist:
            return True
        if token_data["developer_address"] in self.dev_blacklist:
            return True
        return False