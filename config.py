import os


class Configs:
    DISCORD_CLIENT_ID = os.environ.get("DISCORD_CLIENT_ID")
    DISCORD_CLIENT_SECRET = os.environ.get("DISCORD_CLIENT_SECRET")
    DISCORD_BOT_ID = os.environ.get("DISCORD_BOT_ID")
    DISCORD_GUILD = os.environ.get("DISCORD_GUILD")

    COVID_URL = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?%20"
    COVID_MAIN = "main"
    COVID_COUNTRY = "country"
    PRETEND_BROWSER = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
     }

