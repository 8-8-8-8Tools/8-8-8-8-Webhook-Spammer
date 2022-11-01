import os
import sys
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import init
init()
from colorama import Fore
from tqdm import tqdm
import time
from time import sleep
# https://www.luya.ml/ [Website]
# https://ko-fi.com/luyadevs [Donate]
# https://t.me/bladetools [Telegram]

os.system("title 8-8-8-8 Webhook Spammer")
y = Fore.YELLOW
w = Fore.WHITE

def clear():
    os.system("cls")

title = f"""

                                    #####         #####         #####         #####  
                                   #     #       #     #       #     #       #     # 
                                   #     #       #     #       #     #       #     # 
                                    #####         #####         #####         #####   
                                   #     #       #     #       #     #       #     # 
                                   #     #       #     #       #     #       #     # 
                                    #####         #####         #####         #####  
                                                   
                                          """


clear()
print(title)
print("""
                                             Webhook Spammer - v1.0
                                          https://github.com/8-8-8-8Tools
                                             https://dsc.gg/-8888-
""")

webh = input(w + "[" + y + "+" + w + "] Webhook: ")
amt = input(w + "[" + y + "+" + w + "] Amount: ")
msg = input(w + "[" + y + "+" + w + "] Message: ")
input(f"{w}Press {y}ENTER{w} to start spamming: ")
clear()
print(title)
for i in tqdm(range(int(amt)), desc ="Spamming"):
    webhook = DiscordWebhook(url=webh, content=msg)
    response = webhook.execute()
time.sleep(2)
print("finished")
os.system("py main.py")
sys.exit()
input()