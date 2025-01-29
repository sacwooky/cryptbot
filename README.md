# CryptBot

CryptBot is a bot designed for analyzing and trading crypto tokens.

## Features
- Scrapes data from DexScreener
- Filters tokens based on market criteria
- Detects fake trading volume
- Checks tokens against RugCheck
- Sends trade signals via Telegram

## Installation

### Using Docker
1. Clone this repository:
   ```sh
   git clone https://github.com/sacwooky/cryptbot.git
   cd cryptbot
   ```
2. Build and run the Docker container:
   ```sh
   docker build -t sacwooky/cryptbot .
   docker run -d --name cryptbot --env-file .env sacwooky/cryptbot
   ```

### Using Docker Compose
1. Ensure `docker-compose` is installed.
2. Run the following command:
   ```sh
   docker-compose up -d
   ```

## Configuration
Set the required environment variables in a `.env` file or through Unraid UI:
```sh
POSTGRES_HOST=your_postgres_host
POSTGRES_PORT=5432
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

## Running on Unraid
1. Copy `unraid/my_cryptbot.xml` to your Unraid app templates.
2. Configure the container settings in Unraid.
3. Start the container and monitor logs via Unraid UI.

## License
This project is licensed under the MIT License.

## Support
For issues and feature requests, visit: [GitHub Issues](https://github.com/sacwooky/cryptbot/issues).
