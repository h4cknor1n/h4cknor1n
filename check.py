import random
import string
import os
import requests
import proxygen
from itertools import cycle
import base64
from random import randint

tokens = []
token = "ODAwNzk0NDY2MzY1MjEwNjk0.YAXVSg.GfBt_QD6Y2vZ3yIwlbAfq4kMZ1E"

proxies = proxygen.get_proxies()
proxy_pool = cycle(proxies)
proxy = next(proxy_pool)

current_path = os.path.dirname(os.path.realpath(__file__))

url = "https://discordapp.com/api/v6/users/@me/library"

header = {
    "Content-Type": "application/json",
    "authorization": token
}
r = requests.get(url, headers=header, proxies={"http": proxy})
print(token)
if r.status_code == 200:
    print(u"\u001b[32;1m[+] Token Works!\u001b[0m")
    f = open(current_path+"/"+"workingtokens.txt", "a")
    f.write(token+"\n")
    f.close
elif "rate limited." in r.text:
    print("[-] You are being rate limited.")
else:
    print(u"\u001b[31m[-] Invalid Token.\u001b[0m")
# tokens.remove(token)