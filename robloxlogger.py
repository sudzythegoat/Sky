from discord_webhook import DiscordWebhook
import tkinter
from tkinter import ttk
import 
def send_discord_webhook(webhook_url, message):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    response = webhook.execute()

# Example usage
webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
message = "Hello from Python using discord-webhook library!"
send_discord_webhook(webhook_url, message)