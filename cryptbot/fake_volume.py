class FakeVolumeDetector:
    def __init__(self, config: dict):
        self.threshold = config["fake_volume_detection"]["threshold"]

    def detect_fake_volume(self, token_data: dict) -> bool:
        """Detect fake volume based on a threshold."""
        # Example: Compare volume to liquidity ratio
        volume_ratio = token_data["volume_24h"] / token_data["liquidity"]
        return volume_ratio > self.threshold